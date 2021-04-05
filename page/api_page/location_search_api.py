# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/5 14:31
# @Author:tyh
# @File  :location_search_api.py
# @Phone :13926528314
# ================================================
import allure

from common.api_base_page import BaseApi


class LocationSearchApi(BaseApi):
    """
    地点检索
    返回码	英文描述	定义	常见原因
    0	ok	正常	服务请求正常召回
    2	Parameter Invalid	请求参数非法	必要参数拼写错误或漏传（如query和tag请求中均未传入）
    3	Verify Failure	权限校验失败
    4	Quota Failure	配额校验失败	服务当日调用次数已超限，请前往API控制台提升（请优先进行开发者认证）
    5	AK Failure	ak不存在或者非法	未传入ak参数；ak已被删除（可前往回收站恢复）；
    """

    @allure.step("行政区划区域检索")
    def regional_search(self, query, region, output):
        """
        行政区划区域检索
        :param query: 检索关键字。行政区划区域检索不支持多关键字检索。如果需要按POI分类进行检索，请将分类通过query参数进行设置，如query=美食
        :param region: 检索行政区划区域，可输入行政区划名或对应cityCode
        :param output: 输出格式为json或者xml
        :return:
        """
        regional_url = f"{self.base_url}/place/v2/search"
        return self.send(1, regional_url, query=query, region=region, output=output)

    @allure.step("圆形区域检索")
    def circular_region_retrieval(self, query, location, output):
        """
        圆形区域检索
        :param query: 检索关键字。圆形区域检索和矩形区域内检索支持多个关键字并集检索，不同关键字间以$符号分隔，最多支持10个关键字检索。
        如:”银行$酒店”,如果需要按POI分类进行检索，请将分类通过query参数进行设置，如query=美食
        :param location: 圆形区域检索中心点，不支持多个点,"38.76623,116.43213"
        :param output: 	输出格式为json或者xml
        :return:
        """
        regional_url = f"{self.base_url}/place/v2/search"
        return self.send(1, regional_url, query=query, region=location, output=output)
