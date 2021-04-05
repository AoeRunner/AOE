# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 11:56
# @Author:tyh
# @File  :utils_handle.py
# @Phone :13926528314
# ================================================
import os
import re

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

    def assert_result(self, result, **kwargs):
        """
        对result进行解析
        :param result:
        :param kwargs:
        :return:
        """
        for k, v in kwargs.items():
            if type(v) == list:
                # 列表里的每个元素均为一个字典
                for i in range(len(v)):
                    for k1, v1 in v[i].items():
                        value1 = result[k][i][k1]
                        if type(value1) == str:
                            value1 = re.sub(r'(\\u[a-zA-Z0-9]{4})',
                                            lambda x: x.group(1).encode("utf-8").decode("unicode-escape"), value1)
                        self.log.info(f"预期结果{k1}={v1}, 实际结果{k1}={value1}")
                        assert value1 == v1, f"预期结果{k1}={v1}, 实际结果{k1}={value1}"
            else:
                value = result[k]
                if type(value) == str:
                    value = re.sub(r'(\\u[a-zA-Z0-9]{4})',
                                   lambda x: x.group(1).encode("utf-8").decode("unicode-escape"), value)
                self.log.info(f"预期结果{k}={v}, 实际结果{k}={value}")
                assert value == v, f"预期结果{k}={v}, 实际结果{k}={value}"


utils = UtilsHandle()
