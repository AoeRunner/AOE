# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 10:54
# @Author:tyh
# @File  :test_base_case.py
# @Phone :13926528314
# ================================================
import os
import time

from utils import root_dir
from utils.log_handle import CommonLog


class TestBaseCase:
    """
    单元测试基类，用于用例执行前的初始化操作
    """
    log = CommonLog("TestBaseCase").add_handle()

    @classmethod
    def setup_class(cls):
        """
        所有用例执行前的操作
        :return:
        """
        cls.log.info("========setup_class===========")

    def setup(self):
        """
        单个用例执行前的操作
        :return:
        """
        self.log.info("========setup=================")
        time_stamp = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        self.log.info(f"哦，我的王母娘娘啊,请站稳扶好,即将运行用例: {time_stamp}")

    def teardown(self):
        """
        单个测试用例执行后的操作
        :return:
        """
        self.log.info("========teardown==============")

    @classmethod
    def teardown_class(cls):
        """
        所有测试用例执行后的操作
        :return:
        """
        cls.log.info("========teardown_class========")
