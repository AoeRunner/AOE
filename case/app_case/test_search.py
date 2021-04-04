# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/4 15:32
# @Author:tyh
# @File  :test_search.py
# @Phone :13926528314
# ================================================
import allure

from common.test_app_base_case import TestAppBaseCase


@allure.feature("搜索测试类")
class TestSearch(TestAppBaseCase):
    """
    搜索测试类
    """

    def test_search(self):
        self.main_page.goto_search_page("加油站")