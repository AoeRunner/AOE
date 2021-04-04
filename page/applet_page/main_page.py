# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/4 19:06
# @Author:tyh
# @File  :main_page.py
# @Phone :13926528314
# ================================================
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from common.app_base_page import AppBasePage
from page.applet_page.search_page import SearchPage


class AppletMainPage(AppBasePage):
    """
    主图模块
    """
    B_BAIDU_MAP = ["text", "百度地图", "百度地图图标按钮"]
    B_INPUT = ["text", "搜地点", "输入框按钮按钮"]

    def __init__(self, poco: AndroidUiautomationPoco = None):
        super(AppletMainPage, self).__init__(poco=poco)
        self.move().action(self.B_BAIDU_MAP)

    def goto_search_page(self):
        """
        进入百度地图搜索页面
        :return:
        """
        self.action(self.B_INPUT)
        return SearchPage()
