# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 17:16
# @Author:tyh
# @File  :cmd_handle.py
# @Phone :13926528314
# ================================================
import subprocess

from utils.log_handle import CommonLog


class CmdHandle:
    """
    cmd命令执行工具
    """
    log = CommonLog("CmdHandle").add_handle()

    def __init__(self):
        pass

    def cmd_start(self, cmd):
        """
        cmd命令基础方法
        :param cmd:
        :return:
        """
        self.log.info(f"cmd : {cmd}")
        sub_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        cmd_result = sub_process.stdout.readline()
        return cmd_result

    def cmd_adb_start(self, cmd, device=None):
        """
        adb命令方法
        :param cmd:
        :param device: 设备devices
        :return:
        """
        if device is not None:
            cmd = f"adb -s {device} {cmd}"
        else:
            cmd = f"adb {cmd}"
        self.log.info(f"cmd_adb : {cmd}")
        return self.cmd_start(cmd)

    def cmd_adb_shell_start(self, cmd, device=None):
        """
        adb shell命令方法
        :param cmd:
        :param device: 设备devices
        :return:
        """
        self.log.info(f"cmd_adb : {cmd}")
        cmd = f"shell {cmd}"
        return self.cmd_adb_start(cmd, device=device)


cmd_handle = CmdHandle()