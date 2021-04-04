# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/4 21:47
# @Author:tyh
# @File  :search_page.py
# @Phone :13926528314
# ================================================
from common.app_base_page import AppBasePage


class SearchPage(AppBasePage):
    """
    搜索模块
    """

    I_SEARCH_INPUT = ["name", "com.baidu.BaiduMap:id/tvSearchBoxInput", "搜索输入框"]
    B_SEARCH = ["name", "com.baidu.BaiduMap:id/tvSearchButton", "搜索按钮"]

    def search_text(self, input_text="厦门北站"):
        """
        输入框搜索
        :param input_text:
        :return:
        """
        self.input_text(input_text).action(self.B_SEARCH)
        return self
