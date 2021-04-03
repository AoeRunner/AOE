# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/30 22:55
# @Author:tyh
# @File  :main_page.py
# @Phone :13926528314
# ================================================
import allure

from common.web_base_page import WebBasePage
from page.web_page.search_page import SearchPage


class MainPage(WebBasePage):
    """
    主页模块
    """
    B_INPUT = [".searchbox-content-common", "输入框按钮"]

    @allure.step("跳转至添加成员界面")
    def goto_search_page(self):
        """
        跳转至添加成员界面
        :return:
        """
        self.action(self.B_INPUT)
        return SearchPage(self.driver)
