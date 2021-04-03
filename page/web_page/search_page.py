# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 19:11
# @Author:tyh
# @File  :search_page.py
# @Phone :13926528314
# ================================================
import allure

from common.web_base_page import WebBasePage


class SearchPage(WebBasePage):
    """
    搜索模块
    """
    B_SEARCH_INPUT = [".searchbox-content-common", "搜索输入框"]
    B_SEARCH = ["#search-button", "搜索按钮"]
    B_ALL_RESTAURANTS = [".botn-line", "所有餐厅按钮"]
    B_SEARCH_RESULT = [".n-blue", "搜索结果"]

    @allure.step("搜索")
    def search(self, content):
        """
        跳转至添加成员界面
        :return:
        """
        restaurants = self.action(self.B_SEARCH_INPUT, content).action(self.B_SEARCH).find(self.B_SEARCH_RESULT)
        self.log.info(restaurants.text)
