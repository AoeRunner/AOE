# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 16:51
# @Author:tyh
# @File  :conftest.py
# @Phone :13926528314
# ================================================
from typing import List


def pytest_collection_modifyitems(session, config, items: List):
    for item in items:
        # item.name 用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # item.nodeid 用例的路径
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
