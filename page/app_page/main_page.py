# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 19:57
# @Author:tyh
# @File  :main_page.py
# @Phone :13926528314
# ================================================
from common.app_base_page import AppBasePage


class MainPage(AppBasePage):
    """
    主图模块
    """
    B_SEARCH_BOX = ["com.baidu.BaiduMap:id/tv_searchbox_home_text", "输入框按钮"]
    I_SEARCH_INPUT = ["com.baidu.BaiduMap:id/tvSearchBoxInput", "搜索输入框"]
    B_SEARCH = ["com.baidu.BaiduMap:id/tvSearchButton", "搜索按钮"]

    def goto_search_page(self, text):
        """
        进入搜索模块
        :return:
        """
        self.action(self.B_SEARCH_BOX).action(self.I_SEARCH_INPUT, text).action(self.B_SEARCH)
