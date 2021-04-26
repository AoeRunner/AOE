# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/5 14:26
# @Author:tyh
# @File  :api_base_page.py
# @Phone :13926528314
# ================================================
import requests

from utils.log_handle import CommonLog


class BaseApi:
    """
    api基类，用于被各模块接口继承
    """
    log = CommonLog("ApiBaseApi").add_handle()

    def __init__(self):
        """
        初始化基础url,并实例化Session()
        """
        self.base_url = "http://api.map.baidu.com"
        self.s = requests.Session()
        self.s.params = {"ak": ""}

    def send(self, method, url, **kwargs):
        """
        发送请求
        :param method: 请求方法
        :param url: 元组
        :param kwargs: 字典
        :return:
        """
        result = ""
        self.log.info(f"接口url:{url}")
        self.log.info(f"接口参数url:{kwargs}")
        if method == 1:
            self.log.info("即将发起GET请求")
            result = self.s.request("GET", url, params=kwargs)
        elif method == 2:
            self.log.info("即将发起POST请求")
            result = self.s.request("POST", url, json=kwargs)
        elif method == 3:
            self.log.info("即将发起PUT请求")
            result = self.s.request("PUT", url, data=kwargs)
        elif method == 4:
            self.log.info("即将发起DEFLECT请求")
            result = self.s.request("DEFLECT", url, params=kwargs)
        result = result.json()
        self.log.info(f"返回result:{result}")
        return result
