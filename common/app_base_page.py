# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 22:54
# @Author:tyh
# @File  :app_base_page.py
# @Phone :13926528314
# ================================================
import os
import shelve
import time
from typing import List

import allure
from airtest.core import api
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from utils import mydbs_dir
from utils.log_handle import CommonLog


class AppBasePage:
    """
    app基础page,实现app基础方法，用于其他page继承
    """
    log = CommonLog("AppBasePage").add_handle()

    def __init__(self):
        """
        初始化driver
        """
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    def snap_shot(self, value: List):
        """
        截图
        :param value:
        :return:
        """
        with shelve.open(f"{mydbs_dir}/screenshot_dir") as db:
            screenshot_dir = db["screenshot_dir"]
        time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        file_path = os.path.join(screenshot_dir, f"{time_stamp}_{value[1]}.jpg")
        self.log.info(f"截图--{file_path}")
        # 截图
        api.snapshot(file_path)
        # 日志中增加截图
        allure.attach.file(f"{file_path}", f"{value[1]}", attachment_type=allure.attachment_type.JPG)

    def action(self, value: List, text=None):
        """
        控件操作，默认进行按钮点击，当传入text时进行输入操作
        :param value: 定位值
        :param text: 输入值
        :return:
        """
        self.snap_shot(value)
        if text:
            self.log.info(f"{value[1]}--输入--{text}")
            self.poco(value[0]).set_text(text)
        else:
            self.log.info(f"点击--{value[1]}")
            self.poco(value[0]).click()
        return self
