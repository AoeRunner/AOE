# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/5 15:38
# @Author:tyh
# @File  :test_location_search.py
# @Phone :13926528314
# ================================================
import allure
import pytest

from common.test_base_case import TestBaseCase
from page.api_page.location_search_api import LocationSearchApi
from utils.utils_handle import utils


@allure.feature("地点检索测试类")
class TestLocationSearch(TestBaseCase):
    """
    地点检索测试类
    """
    yaml_data = utils.parse_yaml("api_data", "api_data.yaml")

    @classmethod
    def setup_class(cls):
        super(TestLocationSearch, cls).setup_class()
        cls.location_search_api = LocationSearchApi()

    @allure.story("测试行政区划区域检索")
    @pytest.mark.parametrize(["query", "region", "output"], yaml_data["test_regional_search"])
    def test_regional_search(self, query, region, output):
        """
        测试行政区划区域检索
        :return:
        """
        r = self.location_search_api.regional_search(query, region, output)
        utils.assert_result(r, status=0, message="ok", result_type="poi_type", results=[{'name': query}])

    @allure.story("测试圆形区域检索")
    @pytest.mark.parametrize(["query", "location", "output"], yaml_data["test_circular_region_retrieval"])
    def test_circular_region_retrieval(self, query, location, output):
        """
        测试圆形区域检索
        :return:
        """
        r = self.location_search_api.circular_region_retrieval(query, location, output)
        utils.assert_result(r, status=0, message="ok", result_type="poi_type", results=[{'name': query}])
