# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/3 17:12
# @Author:tyh
# @File  :case_runner.py
# @Phone :13926528314
# ================================================
import os
import shelve
import time

import pytest

from utils import root_dir, mydbs_dir
from utils.cmd_handle import cmd_handle
from utils.log_handle import CommonLog
from utils.parser_handle import parse_handle


class CaseRunner:
    """
    web应用启动器
    """
    log = CommonLog("CaseRunner").add_handle()

    def __init__(self, cases):
        """
        初始化cases
        :param cases: 运行用例
        """
        self.cases = cases
        self.main_dir = ""

    def run(self):
        """
        运行测试用例并生成报告
        :return:
        """
        time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.main_dir = os.path.join(root_dir, "report", f"{time_stamp}")

        # 创建主任务目录
        if not os.path.exists(self.main_dir):
            # 使用os.makedirs()方法创建多层目录
            os.makedirs(self.main_dir)
            self.log.info(f"报告目录创建成功: {self.main_dir}")
        else:
            self.log.info("报告目录已存在！！！")

        # 创建log目录,并保存
        # log_dir = os.path.join(self.main_dir, "log")
        # with shelve.open(f"{mydbs_dir}/log_dir") as db:
        #     db["log_dir"] = log_dir

        # 创建截图目录,并保存,非接口测试才需要截图
        if self.cases.find("api") == 0:
            screenshot_dir = os.path.join(self.main_dir, "screenshot")
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            else:
                self.log.info("报告目录已存在！！！")
            with shelve.open(f"{mydbs_dir}/screenshot_dir") as db:
                db["screenshot_dir"] = screenshot_dir

        # 运行用例
        report_dir = os.path.join(self.main_dir, "report")
        pytest.main([self.cases, "--alluredir", f"{report_dir}"])

        # 生成报告
        html_dir = os.path.join(report_dir, "html")
        cmd = f"allure generate {report_dir} -o {html_dir} --clean"
        cmd_handle.cmd_start(cmd)


if __name__ == '__main__':
    # runner_args = parse_handle.runner_handle()
    # cases = runner_args.cases
    cases = os.path.join(root_dir, "case", "api_case", "test_location_search.py")
    CaseRunner(cases).run()
