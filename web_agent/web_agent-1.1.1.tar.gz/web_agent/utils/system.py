#!/usr/bin/env python

import os
import sys
import re
import time
import socket
import yaml
from subprocess import Popen, PIPE, STDOUT
from utils import log


def execute(cmd, cmdline=True, console=True, interrupt=True):
    """
    Execute shell command
    """
    cmd = " ".join(cmd) if isinstance(cmd, list) else cmd
    if cmdline:
        print("# {cmd}".format(cmd=cmd))

    if "linux" in sys.platform:
        proc = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True, close_fds=True)
    else:
        proc = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    output = ""
    while True:
        line = proc.stdout.readline().decode("utf-8", "ignore")
        if line:
            if console:
                sys.stdout.write(line)
                sys.stdout.flush()
            output += line

        if proc.poll() is not None and line == "":
            break
    status = proc.returncode

    if status and interrupt:
        raise RuntimeError("{} failed!".format(cmd))

    return status, output


def get_ip_address():
    """Get ip address of host"""
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('8.8.8.8', 80))
        ip_address = sock.getsockname()[0]
    finally:
        if sock:
            sock.close()
    return ip_address


def get_multi_ip_address():
    address = list()
    add_info = socket.getaddrinfo(socket.gethostname(), None)
    for item in add_info:
        if ':' not in item[4][0]:
            log.INFO('Find ip address::' + item[4][0])
            address.append(item[4][0])
    return address


def get_host_name():
    name = socket.gethostname()
    return name


def get_root_path():
    root_path = os.path.join(os.path.dirname(__file__), "..")
    return root_path


def get_expect_version(tool_name):
    conf = os.path.join(get_root_path(), "configuration", "version.yaml")
    with open(conf) as file_:
        cont = file_.read()
    cf_ = yaml.load(cont)
    version_ = cf_[tool_name]
    return version_


def version_check(tool):
    act_version = tool.get_version()
    exp_version = get_expect_version(tool.name)
    log.INFO("%s actual version:%s , expect version:%s", tool.name, act_version, exp_version)
    ret = True if act_version == exp_version else False
    return ret


def get_time_stamp():
    return time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))


def nexus_or_nvme_device():
    cmd = "lsblk"
    _, outs = execute(cmd)
    if "nvme" in outs:
        ret = "nvme"
    elif "nexus" in outs:
        ret = "nexus"
    else:
        ret = None
    return ret


def decorate_exception(func):
    def func_wrapper(*args, **kwargs):
        try:
            ret = func(*args, **kwargs)
        except Exception as e:
            print(e)
            ret = False
        return ret
    return func_wrapper


def get_platform():
    platform = os.environ.get('platform', '')
    if platform == "oakgate":
        slot_type = "oakgate"
    elif platform == "linux":
        slot_type = "linux"
    else:
        if "win" in sys.platform.lower():
            slot_type = "oakgate"
        else:
            slot_type = "linux"
    return slot_type


ROOT_PATH = get_root_path()

