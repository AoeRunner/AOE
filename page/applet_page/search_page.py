# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/4 21:40
# @Author:tyh
# @File  :search_page.py
# @Phone :13926528314
# ================================================
from common.app_base_page import AppBasePage


class SearchPage(AppBasePage):
    """
    搜索模块
    """
    B_INPUT_TEXT = ["text", "搜地点", "搜索输入框"]
    B_INPUT_SEARCH = ["text", "搜索", "搜索按钮"]

    def search_text(self, input_text="厦门北站"):
        """
        输入框搜索
        :param input_text:
        :return:
        """
        self.input_text(input_text).action(self.B_INPUT_SEARCH)
        return self
