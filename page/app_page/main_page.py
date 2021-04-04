# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 19:57
# @Author:tyh
# @File  :main_page.py
# @Phone :13926528314
# ================================================
from common.app_base_page import AppBasePage
from page.app_page.search_page import SearchPage


class MainPage(AppBasePage):
    """
    主图模块
    """
    B_SEARCH_BOX = ["name", "com.baidu.BaiduMap:id/tv_searchbox_home_text", "输入框按钮"]

    def goto_search_page(self):
        """
        进入搜索模块
        :return:
        """
        self.action(self.B_SEARCH_BOX)
        return SearchPage()
