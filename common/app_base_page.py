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
from typing import List, Tuple

import allure
from airtest.core.api import snapshot, text, swipe, shell
from airtest.core.helper import G
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from utils import mydbs_dir
from utils.log_handle import CommonLog


class AppBasePage:
    """
    app基础page,实现app基础方法，用于其他page继承
    """
    log = CommonLog("AppBasePage").add_handle()

    def __init__(self, poco: AndroidUiautomationPoco = None):
        """
        初始化driver
        """
        self.log.info("初始化poco")
        self.poco = poco

    def snap_shot(self, value: List):
        """
        截图
        :param value:
        :return:
        """
        with shelve.open(f"{mydbs_dir}/screenshot_dir") as db:
            screenshot_dir = db["screenshot_dir"]
        time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        file_path = os.path.join(screenshot_dir, f"{time_stamp}_{value[1]}.png")
        self.log.info(f"截图--{file_path}")
        # 截图
        snapshot(filename=file_path)
        # 日志中增加截图
        allure.attach.file(f"{file_path}", f"{value[1]}", attachment_type=allure.attachment_type.PNG)

    def find(self, value: List):
        """
        根据定位值查找元素
        :param value: 定位值
        :return:
        """
        # self.snap_shot(value)
        loc_type = value[0]
        loc_text = value[1]
        loc_msg = value[2]
        self.log.info(f"查找--{loc_msg}")
        if loc_type == "name":
            return self.poco(loc_text)
        elif loc_type == "text":
            return self.poco(text=loc_text)
        elif loc_type == "resourceId":
            return self.poco(resourceId=loc_text)

    def action(self, value: List, input_text=None):
        """
        元素操作，默认进行点击，存在input_text时进行输入操作
        :param value:
        :param input_text:
        :return:
        """
        if input_text is None:
            self.find(value).click()
            self.log.info(f"点击--{value[2]}")
        else:
            self.find(value).set_text(input_text)
            self.log.info(f"输入--{input_text}")
        return self

    def input_text(self, input_text):
        """
        使用airtest输入
        :return:
        """
        self.log.info(f"输入--{input_text}")
        text(input_text)
        return self

    def move(self):
        """
        移动
        :param start:
        :param end:
        :return:
        """
        swipe((550, 250), (550, 1200))
        return self
