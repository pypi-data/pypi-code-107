#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""[summary]
"""
from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Union  # noqa TYP001

import click

if TYPE_CHECKING:
    from energinetml import Project

from energinetml.core.model import (
    Model,
    ModelImportError,
    ModelNotClassError,
    ModelNotInheritModel,
    TrainedModel,
    import_model_class,
)


def discover_project(project_cls: Project, required: bool = True) -> str:
    """[summary]

    Args:
        project_cls (Project): [description]
        required (bool, optional): [description]. Defaults to True.

    Returns:
        str: [description]
    """

    def _project_from_path_callback(
        ctx: click.Context, param: click.Parameter, value: str
    ) -> str:
        """[summary]

        Args:
            ctx (click.Context): [description]
            param (click.Parameter): [description]
            value (str): [description]

        Raises:
            click.Abort: [description]

        Returns:
            str: [description]
        """
        try:
            return project_cls.from_directory(value)
        except project_cls.NotFound:
            if required:
                click.echo(
                    (
                        "Could not find a project in this folder "
                        f"(or any of its parents): {value}"
                    )
                )

                click.echo(
                    (
                        "I am looking for a folder which contains a file "
                        f"named '{project_cls.CONFIG_FILE_NAME}' - either in the "
                        "folder itself or in one of its parent folders."
                    )
                )

                click.echo(
                    "Specify which project to use by providing the "
                    "-p/--path parameter."
                )

                raise click.Abort()

    return click.option(
        "--path",
        "-p",
        "project",
        default=".",
        type=click.Path(dir_okay=True, resolve_path=True),
        help="Project directory path (default: current directory)",
        callback=_project_from_path_callback,
    )


def discover_model(
    required: bool = True, load_model: bool = True, param_name: str = "model"
) -> None:
    """[summary]

    Args:
        required (bool, optional): [description]. Defaults to True.
        load_model (bool, optional): [description]. Defaults to True.
        param_name (str, optional): [description]. Defaults to "model".
    """

    def _model_from_path_callback(
        ctx: click.Context, param: click.Parameter, model_file_path: str
    ) -> Model:
        """[summary]

        Args:
            ctx (click.Context): [description]
            param (click.Parameter): [description]
            value (str): [description]

        Raises:
            click.Abort: [description]

        Returns:
            Model: [description]
        """
        # Does model module exist?
        if not os.path.isdir(model_file_path):
            click.echo(("Could not find this folder: %s") % model_file_path)

            click.echo(("I am looking for a folder which contains a python module."))

            click.echo(
                ("Specify which model to use by providing the " "-p/--path parameter.")
            )

            raise click.Abort()

        try:
            model_class = import_model_class(model_file_path)
        except ModelImportError:
            # Imported script does not have a "model" attribute
            click.echo(
                f"Failed to import your model class from module: {model_file_path}"
            )

            click.echo(
                'Make sure you refer your model class and name it "model". '
                'Do this by defining a global variable named "model" in your '
                "module, and point it to your model class."
            )

            click.echo("")
            click.echo("Example:")
            click.echo("")
            click.echo("    class MyModel(Model):")
            click.echo("        ...")
            click.echo("")
            click.echo("    model = MyModel")
            click.echo("")

            raise click.Abort()
        except ModelNotClassError:
            # Imported "model" attribute is not a Class type
            click.echo(
                f"Failed to import your model class from module: {model_file_path}"
            )

            click.echo(
                'When you define the "model" object in your model script, '
                "make sure not to instantiate it."
            )

            click.echo("")
            click.echo("Example of doing it correct:")
            click.echo("")
            click.echo("    class MyModel(Model):")
            click.echo("        ...")
            click.echo("")
            click.echo("    model = MyModel")

            click.echo("")
            click.echo("Example of doing it WRONG:")
            click.echo("")
            click.echo("    class MyModel(Model):")
            click.echo("        ...")
            click.echo("")
            click.echo("    model = MyModel()  # Notice the instantiation")
            click.echo("")

            raise click.Abort()
        except ModelNotInheritModel:
            # Imported "model" attribute does not inherit from Model
            click.echo(
                f"Failed to import your model class from module: {model_file_path}"
            )

            click.echo("The model you are referring to does not inherit from Model.")

            click.echo("")
            click.echo("Example of doing it correct:")
            click.echo("")
            click.echo("    from energinetml import Model")
            click.echo("")
            click.echo("    class MyModel(Model):  # Notice the inheritance")
            click.echo("        ...")
            click.echo("")
            click.echo("    model = MyModel")
            click.echo("")

            raise click.Abort()

        try:
            return model_class.from_directory(model_file_path)
        except Model.NotFound:
            if required:
                click.echo(
                    (
                        "Could not find a configuration in this folder "
                        f"(or any of its parents): {model_file_path}"
                    )
                )

                click.echo(
                    (
                        "I am looking for a folder which contains a file "
                        f"named {Model.CONFIG_FILE_NAME} - either in the "
                        "folder itself or in one of its parent folders."
                    )
                )

                click.echo(
                    (
                        "Specify which model to use by providing the "
                        "-p/--path parameter."
                    )
                )

                raise click.Abort()

    return click.option(
        "--path",
        "-p",
        "model",
        default=".",
        type=click.Path(dir_okay=True, resolve_path=True),
        help="Model directory path (default: current directory)",
        callback=_model_from_path_callback,
    )


def discover_trained_model(
    required: bool = True, load_model: bool = True, param_name: str = "trained_model"
) -> Union[str, TrainedModel]:
    """[summary]

    Args:
        required (bool, optional): [description]. Defaults to True.
        load_model (bool, optional): [description]. Defaults to True.
        param_name (str, optional): [description]. Defaults to "trained_model".

    Returns:
        Union[str, TrainedModel]: [description]
    """

    def _project_from_path_callback(
        ctx: click.Context, param: click.Parameter, value: str
    ) -> Union[str, TrainedModel]:
        """[summary]

        Args:
            ctx (click.Context): [description]
            param (click.Parameter): [description]
            value (str): [description]

        Raises:
            click.Abort: [description]

        Returns:
            Union[str, TrainedModel]: [description]
        """
        if value is not None:
            fp = value
        elif ctx.params.get("model"):
            fp = ctx.params["model"].trained_model_path
        elif required:
            click.echo(
                "Could not determine path to trained model file. "
                "Specify one by providing the -m/--model-file parameter."
            )
            raise click.Abort()
        else:
            return None

        if not os.path.isfile(fp):
            click.echo(f"Trained model not found: {fp}")
            if value is None:
                click.echo("Specify one by providing the -m/--model-file parameter.")
            raise click.Abort()

        if not load_model:
            return fp
        else:
            try:
                return TrainedModel.load(fp)
            except TrainedModel.Invalid:
                click.echo(f"Failed to load trained model: {fp}")
                raise click.Abort()

    return click.option(
        "--model-file",
        "-m",
        param_name,
        default=None,
        type=click.Path(file_okay=True, resolve_path=True),
        help="Trained model file",
        callback=_project_from_path_callback,
    )
