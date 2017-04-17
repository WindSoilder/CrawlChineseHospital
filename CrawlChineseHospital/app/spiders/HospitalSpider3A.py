import json
from urllib import parse

from tornado import gen
from tornado.httpclient import AsyncHTTPClient

from .HospitalSpider import CommomHospitalSpider
from ..item import HospitalInforItem

class HospitalSpider3A(CommomHospitalSpider):
    CommomHospitalSpider.query_dict['hgrade'] = '1'

    def __init__(self, province_id):
        province_id = province_id
        self.query_dict['provinceID'] = province_id
        self.start_url += '?' + parse.urlencode(self.query_dict)

    def parse(self, response):
        response_items = json.loads(response.body.decode('utf-8'))
        for response_item in response_items:
            item = HospitalInforItem(response_item['provinceId'],
                                     response_item['hType'],
                                     response_item['hGrade'],
                                     response_item['hName'])
            yield item

    def _get_provinceID(self, provinceName):
        return '7216'
