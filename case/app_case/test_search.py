# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/4 15:32
# @Author:tyh
# @File  :test_search.py
# @Phone :13926528314
# ================================================
import allure
import pytest

from common.test_app_base_case import TestAppBaseCase
from utils.utils_handle import utils


@allure.feature("搜索测试类")
class TestSearch(TestAppBaseCase):
    """
    搜索测试类
    """

    @pytest.mark.parametrize(["input_text"], utils.parse_yaml("web_data", "search_data.yaml"))
    @allure.story("搜索方法")
    def test_search(self, input_text):
        self.main_page.goto_search_page().search_text(input_text=input_text)
