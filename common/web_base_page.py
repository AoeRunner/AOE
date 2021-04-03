# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/30 19:36
# @Author:tyh
# @File  :web_base_page.py
# @Phone :13926528314
# ================================================
import os
import shelve
import time
from typing import List

import allure
from airtest_selenium.proxy import WebChrome
from selenium.webdriver.common.by import By

from utils import mydbs_dir
from utils.log_handle import CommonLog


class WebBasePage:
    """
    web基础page,实现web基础方法，用于其他page继承
    """
    log = CommonLog("WebBasePage").add_handle()
    base_url = "https://map.qq.com/"

    def __init__(self, driver: WebChrome = None):
        """
        初始化driver
        :param driver:
        """
        self.driver = driver

    def find(self, value):
        """
        查到元素，全部使用cssSelector定位方式
        :param value: 定位值
        :return:
        """
        with shelve.open(f"{mydbs_dir}/screenshot_dir") as db:
            screenshot_dir = db["screenshot_dir"]
        time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        file_path = os.path.join(screenshot_dir, f"{time_stamp}_{value[1]}.png")
        # 截图
        self.driver.screenshot(file_path)
        # 日志中增加截图
        allure.attach.file(f"{file_path}", f"{value[1]}", attachment_type=allure.attachment_type.PNG)
        return self.driver.find_element(By.CSS_SELECTOR, value[0])

    def finds(self, value):
        """
        查到元素，全部使用cssSelector定位方式
        :param value: 定位值
        :return:
        """
        return self.driver.find_elements(By.CSS_SELECTOR, value[0])

    def judge(self, value: List):
        """
        判断元素，元素存在返回1，不存在返回0
        :param value: 定位值
        :return:
        """
        try:
            self.log.info(f"判断{value[1]}是否存在")
            self.find(value)
        except Exception as err:
            self.log.error(f"未找到{value[1]}", err)
            return 0
        else:
            return 1

    def action(self, value: List, text=None):
        """
        控件操作，默认进行按钮点击，当传入text时进行输入操作
        :param value: 定位值
        :param text: 输入值
        :return:
        """
        if text:
            self.log.info(f"{value[1]}--输入--{text}")
            self.find(value).send_keys(text)
        else:
            self.log.info(f"点击--{value[1]}")
            self.find(value).click()
        return self
