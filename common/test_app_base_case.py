# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/4 12:22
# @Author:tyh
# @File  :test_app_base_case.py
# @Phone :13926528314
# ================================================
from airtest.core.api import *

from common.test_base_case import TestBaseCase
from page.app_page.main_page import MainPage


class TestAppBaseCase(TestBaseCase):
    """
    app初始化
    """
    @classmethod
    def setup_class(cls):
        cls.app_package = "com.baidu.BaiduMap"

    def setup(self):
        super(TestAppBaseCase, self).setup()

        auto_setup(__file__)  # 自动初始化设备

        start_app(self.app_package)
        self.main_page = MainPage()

    def teardown(self):
        super(TestAppBaseCase, self).teardown()
        stop_app(self.app_package)
