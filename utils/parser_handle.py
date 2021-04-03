# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 17:13
# @Author:tyh
# @File  :parser_handle.py
# @Phone :13926528314
# ================================================
import argparse


class ParseHandle:
    """
    命令行解析工具
    """
    def __init__(self):
        # 构造解析器对象
        self.parse = argparse.ArgumentParser(description='Process some integers')

    def caps_handle(self):
        """
        caps_handle,初始化app时传入的参数
        :return:
        """
        # 添加caps_handle参数组对象
        self.parse.add_argument_group("caps_handle")
        # 添加参数
        self.parse.add_argument('--platformName', type=str, default="Android")
        self.parse.add_argument('--deviceName', type=str, default="wework")
        self.parse.add_argument('--appPackage', type=str, default="com.tencent.wework")
        self.parse.add_argument('--appActivity', type=str, default=".launch.LaunchSplashActivity")
        self.parse.add_argument('--noReset', type=str, default="true", help="不清空缓存启动app")
        self.parse.add_argument('--waitForIdleTimeout', type=int, default=0, help="设置等待页面空闲状态的时间为0s")
        return self.parse.parse_args()

    def runner_handle(self):
        """
        runner_handle,运行用例时穿的参数
        :return:
        """
        # 添加runner_handle参数组对象
        self.parse.add_argument_group("runner_handle")
        # 添加参数
        self.parse.add_argument('--cases', type=str)
        return self.parse.parse_args()

    def remote_handle(self):
        """
        remote_handle,启动服务器及端口号
        :return:
        """
        # 添加runner_handle参数组对象
        self.parse.add_argument_group("remote_handle")
        # 添加参数
        self.parse.add_argument('--host', type=str, default="localhost")
        self.parse.add_argument('--port', type=int, default=4723)
        return self.parse.parse_args()


parse_handle = ParseHandle()

if __name__ == '__main__':
    parse_handle = ParseHandle().runner_handle()
    print(parse_handle)
    name = parse_handle.cases
    print(name)