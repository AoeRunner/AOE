# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/1 22:52
# @Author:tyh
# @File  :decorator_handle.py
# @Phone :13926528314
# ================================================
import threading

from utils.log_handle import CommonLog

log = CommonLog("decorator_handle").add_handle()


def log_find(func):
    """
    查找按钮修饰器
    :param func:
    :return:
    """
    def func_fun(*args, **kwargs):
        log.info(f"查找{args[0]}")
        func(*args, **kwargs)
    return func_fun


def log_action(func):
    """
    日志打印修饰器
    :param func:
    :return:
    """
    def func_fun(*args, **kwargs):
        if len(args) == 2:
            log.info(f"点击{args[0][1]}")
        else:
            log.info(f"在{args[0][1]}中输入{args[1]}")
        func(*args, **kwargs)
    return func_fun


def thread_run(func):
    """
    线程修饰器方法，用于将普通方法转换成线程执行
    :param func:
    :return:
    """
    def func_fun(*args, **kwargs):
        thread_tts = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread_tts.start()
        thread_tts.join()
    return func_fun

