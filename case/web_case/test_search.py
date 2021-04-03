# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 11:16
# @Author:tyh
# @File  :test_search.py
# @Phone :13926528314
# ================================================
import allure
import pytest

from common.test_web_base_case import TestWebBaseCase
from utils.utils_handle import utils


@allure.feature("搜索类")
class TestSearch(TestWebBaseCase):
    """
    添加成员
    """

    @pytest.mark.parametrize(["content"], utils.parse_yaml("web_data", "search_data.yaml"))
    @allure.story("搜索方法")
    def test_search_content(self, content):
        """
        测试添加
        :param content: 搜索内容
        :return:
        """
        self.main_page.goto_search_page().search(content)

