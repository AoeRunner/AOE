# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/4 12:22
# @Author:tyh
# @File  :test_app_base_case.py
# @Phone :13926528314
# ================================================
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from common.test_base_case import TestBaseCase
from page.app_page.main_page import MainPage
from page.applet_page.main_page import AppletMainPage


class TestAppBaseCase(TestBaseCase):
    """
    app初始化
    """
    @classmethod
    def setup_class(cls):
        cls.app_package = "com.baidu.BaiduMap"
        # 自动初始化设备
        # auto_setup(__file__, devices=["Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP)"])
        cls.dev1 = connect_device("Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP)")
        cls.log.info(f"connect_device: {cls.dev1}")
        cls.poco = AndroidUiautomationPoco(device=cls.dev1, use_airtest_input=True, screenshot_each_action=False)

    def setup(self):
        super(TestAppBaseCase, self).setup()
        start_app(self.app_package)
        self.main_page = MainPage(self.poco)

    def teardown(self):
        super(TestAppBaseCase, self).teardown()
        stop_app(self.app_package)


class TestAppletBaseCase(TestBaseCase):
    """
    app初始化
    """
    @classmethod
    def setup_class(cls):
        cls.app_package = "com.tencent.mm"
        # 自动初始化设备
        # auto_setup(__file__, devices=["Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP)"])
        cls.dev1 = connect_device("Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP)")
        cls.log.info(f"connect_device: {cls.dev1}")
        cls.poco = AndroidUiautomationPoco(device=cls.dev1, use_airtest_input=True, screenshot_each_action=False)

    def setup(self):
        super(TestAppletBaseCase, self).setup()
        start_app(self.app_package)
        self.main_page = AppletMainPage(self.poco)

    def teardown(self):
        super(TestAppletBaseCase, self).teardown()
        stop_app(self.app_package)