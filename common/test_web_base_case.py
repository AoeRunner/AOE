# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 11:00
# @Author:tyh
# @File  :test_web_base_case.py
# @Phone :13926528314
# ================================================
import os
import shelve

from airtest_selenium.proxy import WebChrome

from common.test_base_case import TestBaseCase
from page.web_page.main_page import MainPage
from utils import root_dir, mydbs_dir

# BASEURL = "https://work.weixin.qq.com/wework_admin/frame#index"
BASEURL = "https://map.baidu.com"


class TestWebBaseCase(TestBaseCase):
    """
    web测试初始化
    """

    def setup(self):
        super(TestWebBaseCase, self).setup()
        self.driver = WebChrome()
        self.driver.implicitly_wait(5)
        self.driver.get(BASEURL)
        # 使用cookie打开浏览器
        with shelve.open(f"{mydbs_dir}/cookies") as db:
            # coo = self.driver.get_cookies()
            # db["cookies"] = coo
            cookies = db["cookies"]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
                continue
            self.driver.add_cookie(cookie)
        self.driver.get(BASEURL)
        self.log.info("进入主界面")
        self.main_page = MainPage(self.driver)

    def teardown(self):
        super(TestWebBaseCase, self).teardown()
        self.log.info("关闭浏览器")
        self.driver.quit()
