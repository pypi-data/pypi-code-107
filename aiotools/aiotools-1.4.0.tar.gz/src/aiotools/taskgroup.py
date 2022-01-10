#
# This source file is part of the EdgeDB open source project.
#
# Copyright 2016-present MagicStack Inc. and the EdgeDB authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# This file is included in the aiotools open source project
# given that EdgeDB's Apache 2.0 license is compatible with
# aiotools' MIT license.
# The original source code is taken from:
# https://github.com/edgedb/edgedb-python/blob/bcbe005/edgedb/_taskgroup.py

import asyncio
try:
    from contextvars import ContextVar
    has_contextvars = True
except ImportError:
    has_contextvars = False
import functools
import itertools
import textwrap
import traceback
import weakref

from .compat import current_task, get_running_loop


__all__ = [
    'MultiError',
    'TaskGroup',
    'TaskGroupError',
]


if has_contextvars:
    current_taskgroup: ContextVar['TaskGroup'] = ContextVar('current_taskgroup')
    __all__.append('current_taskgroup')


class TaskGroup:
    """
    Provides a guard against a group of tasks spawend via its :meth:`create_task`
    method instead of the vanilla fire-and-forgetting :meth:`asyncio.create_task`.

    See the motivation and rationale in `the trio's documentation
    <https://trio.readthedocs.io/en/stable/reference-core.html#nurseries-and-spawning>`_.
    """

    def __init__(self, *, name=None):
        if name is None:
            self._name = f'tg-{_name_counter()}'
        else:
            self._name = str(name)

        self._entered = False
        self._exiting = False
        self._aborting = False
        self._loop = get_running_loop()
        self._parent_task = None
        self._parent_cancel_requested = False
        self._tasks = weakref.WeakSet()
        self._unfinished_tasks = 0
        self._errors = []
        self._base_error = None
        self._on_completed_fut = None

    def get_name(self):
        return self._name

    def __repr__(self):
        msg = f'<TaskGroup {self._name!r}'
        if self._tasks:
            msg += f' tasks:{len(self._tasks)}'
        if self._unfinished_tasks:
            msg += f' unfinished:{self._unfinished_tasks}'
        if self._errors:
            msg += f' errors:{len(self._errors)}'
        if self._aborting:
            msg += ' cancelling'
        elif self._entered:
            msg += ' entered'
        msg += '>'
        return msg

    async def __aenter__(self):
        if self._entered:
            raise RuntimeError(
                f"TaskGroup {self!r} has been already entered")
        self._entered = True

        self._parent_task = current_task()

        if self._parent_task is None:
            raise RuntimeError(
                f'TaskGroup {self!r} cannot determine the parent task')
        self._patch_task(self._parent_task)
        if has_contextvars:
            self._current_taskgroup_token = current_taskgroup.set(self)
        return self

    async def __aexit__(self, et, exc, tb):
        self._exiting = True
        propagate_cancelation = False

        if (exc is not None and
                self._is_base_error(exc) and
                self._base_error is None):
            self._base_error = exc

        if et is asyncio.CancelledError:
            if self._parent_cancel_requested:
                # Only if we did request task to cancel ourselves
                # we mark it as no longer cancelled.
                self._parent_task.__cancel_requested__ = False
            else:
                propagate_cancelation = True

        if et is not None and not self._aborting:
            # Our parent task is being cancelled:
            #
            #    async with TaskGroup() as g:
            #        g.create_task(...)
            #        await ...  # <- CancelledError
            #
            if et is asyncio.CancelledError:
                propagate_cancelation = True

            # or there's an exception in "async with":
            #
            #    async with TaskGroup() as g:
            #        g.create_task(...)
            #        1 / 0
            #
            self._abort()

        # We use while-loop here because "self._on_completed_fut"
        # can be cancelled multiple times if our parent task
        # is being cancelled repeatedly (or even once, when
        # our own cancellation is already in progress)
        while self._unfinished_tasks:
            if self._on_completed_fut is None:
                self._on_completed_fut = self._loop.create_future()

            try:
                await self._on_completed_fut
            except asyncio.CancelledError:
                if not self._aborting:
                    # Our parent task is being cancelled:
                    #
                    #    async def wrapper():
                    #        async with TaskGroup() as g:
                    #            g.create_task(foo)
                    #
                    # "wrapper" is being cancelled while "foo" is
                    # still running.
                    propagate_cancelation = True
                    self._abort()

            self._on_completed_fut = None

        assert self._unfinished_tasks == 0
        self._on_completed_fut = None  # no longer needed
        if has_contextvars:
            current_taskgroup.reset(self._current_taskgroup_token)

        if self._base_error is not None:
            raise self._base_error

        if propagate_cancelation:
            # The wrapping task was cancelled; since we're done with
            # closing all child tasks, just propagate the cancellation
            # request now.
            raise asyncio.CancelledError()

        if et is not None and et is not asyncio.CancelledError:
            self._errors.append(exc)

        if self._errors:
            # Exceptions are heavy objects that can have object
            # cycles (bad for GC); let's not keep a reference to
            # a bunch of them.
            errors = self._errors
            self._errors = None

            me = TaskGroupError('unhandled errors in a TaskGroup',
                                errors=errors)
            raise me from None

    def create_task(self, coro):
        if not self._entered:
            raise RuntimeError(f"TaskGroup {self!r} has not been entered")
        if self._exiting:
            raise RuntimeError(f"TaskGroup {self!r} is awaiting in exit")
        task = self._loop.create_task(coro)
        task.add_done_callback(self._on_task_done)
        self._unfinished_tasks += 1
        self._tasks.add(task)
        return task

    def _is_base_error(self, exc):
        assert isinstance(exc, BaseException)
        return not isinstance(exc, Exception)

    def _patch_task(self, task):
        # In Python 3.8 we'll need proper API on asyncio.Task to
        # make TaskGroups possible. We need to be able to access
        # information about task cancellation, more specifically,
        # we need a flag to say if a task was cancelled or not.
        # We also need to be able to flip that flag.

        def _task_cancel(task, orig_cancel):
            task.__cancel_requested__ = True
            return orig_cancel()

        if hasattr(task, '__cancel_requested__'):
            return

        task.__cancel_requested__ = False
        # confirm that we were successful at adding the new attribute:
        assert not task.__cancel_requested__

        orig_cancel = task.cancel
        task.cancel = functools.partial(_task_cancel, task, orig_cancel)

    def _abort(self):
        self._aborting = True

        for t in self._tasks:
            if not t.done():
                t.cancel()

    def _on_task_done(self, task):
        self._unfinished_tasks -= 1
        assert self._unfinished_tasks >= 0

        if self._exiting and not self._unfinished_tasks:
            if not self._on_completed_fut.done():
                self._on_completed_fut.set_result(True)

        if task.cancelled():
            return

        exc = task.exception()
        if exc is None:
            return

        self._errors.append(exc)
        if self._is_base_error(exc) and self._base_error is None:
            self._base_error = exc

        if self._parent_task.done():
            # Not sure if this case is possible, but we want to handle
            # it anyways.
            self._loop.call_exception_handler({
                'message': f'Task {task!r} has errored out but its parent '
                           f'task {self._parent_task} is already completed',
                'exception': exc,
                'task': task,
            })
            return

        self._abort()
        if not self._parent_task.__cancel_requested__:
            # If parent task *is not* being cancelled, it means that we want
            # to manually cancel it to abort whatever is being run right now
            # in the TaskGroup.  But we want to mark parent task as
            # "not cancelled" later in __aexit__.  Example situation that
            # we need to handle:
            #
            #    async def foo():
            #        try:
            #            async with TaskGroup() as g:
            #                g.create_task(crash_soon())
            #                await something  # <- this needs to be canceled
            #                                 #    by the TaskGroup, e.g.
            #                                 #    foo() needs to be cancelled
            #        except Exception:
            #            # Ignore any exceptions raised in the TaskGroup
            #            pass
            #        await something_else     # this line has to be called
            #                                 # after TaskGroup is finished.
            self._parent_cancel_requested = True
            self._parent_task.cancel()


class MultiError(Exception):
    """
    Represents a collection of errors raised inside a task group.
    Callers may iterate over the errors using the ``__erros__`` attribute.
    """

    def __init__(self, msg, *args, errors=()):
        if errors:
            types = set(type(e).__name__ for e in errors)
            msg = f'{msg}; {len(errors)} sub errors: ({", ".join(types)})'
            for er in errors:
                msg += f'\n + {type(er).__name__}: {er}'
                if er.__traceback__:
                    er_tb = ''.join(traceback.format_tb(er.__traceback__))
                    er_tb = textwrap.indent(er_tb, ' | ')
                    msg += f'\n{er_tb}\n'
        super().__init__(msg, *args)
        self.__errors__ = tuple(errors)

    def get_error_types(self):
        return {type(e) for e in self.__errors__}

    def __reduce__(self):
        return (type(self), (self.args,), {'__errors__': self.__errors__})


class TaskGroupError(MultiError):
    """
    An alias to :exc:`MultiError`.
    """
    pass


_name_counter = itertools.count(1).__next__
