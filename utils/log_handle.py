# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/29 22:03
# @Author:tyh
# @File  :log_handle.py
# @Phone :13926528314
# ================================================
import logging
import os
import time

from utils import root_dir


class CommonLog(object):
    """
    封装logging模块
    """

    def __init__(self, name="common_log", level: logging = logging.INFO):
        """
        实例化logging
        :param name: 日志名称
        :param level: 日志级别
        """
        # self.fmt = "%(asctime)s %(name)s %(filename)s %(module)s %(funcName)s %(lineno)d %(message)s"
        self.fmt = "%(asctime)s %(name)s %(lineno)d %(message)s"
        self.name = name
        self.level = level
        self.formatter = logging.Formatter(self.fmt)

    def create_logger(self):
        """
        创建一个logger，并设置日志级别
        :return:
        """
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)
        return logger

    def create_handle(self):
        """
        创建所需要的handel，并指定输出格式
        :return:
        """
        time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        log_dir = os.path.join(root_dir, "log", f"{time_stamp}.log")
        file_write = logging.FileHandler(log_dir, encoding="utf-8")
        file_write.setFormatter(self.formatter)
        file_print = logging.StreamHandler()
        file_print.setFormatter(self.formatter)
        return file_write, file_print

    def add_handle(self):
        """
        为handle添加日志处理器
        :return:
        """
        logger = self.create_logger()
        create_handle = self.create_handle()
        logger.addHandler(create_handle[0])
        logger.addHandler(create_handle[1])
        return logger
