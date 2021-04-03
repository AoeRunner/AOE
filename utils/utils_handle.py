# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 11:56
# @Author:tyh
# @File  :utils_handle.py
# @Phone :13926528314
# ================================================
import os

import yaml

from utils import root_dir
from utils.log_handle import CommonLog


class UtilsHandle:
    """
    基础方法
    """
    log = CommonLog("UtilsHandle").add_handle()

    def parse_yaml(self, *path):
        self.log.info(path)
        yaml_path = os.path.join(root_dir, "data")
        for p in path:
            yaml_path = os.path.join(yaml_path, p)
        self.log.info(yaml_path)
        return yaml.safe_load(open(yaml_path, encoding='UTF-8'))


utils = UtilsHandle()