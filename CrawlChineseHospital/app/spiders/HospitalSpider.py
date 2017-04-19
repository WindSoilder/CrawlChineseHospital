import json
from urllib import parse

from .SpiderBase import Spider

from ..item import HospitalInforItem

class HospitalSpider(Spider):
    base_url = "https://www.hqms.org.cn"
    path = "/usp/roster/rosterInfo.jsp"
    start_url = parse.urljoin(base_url, path)
    query_dict = {}


class CommomHospitalSpider(HospitalSpider):
    '''
    An abstract class
    A commom hospital spider base on hospital spider
    This spider will fetch for class A, all type hospital
    If you want to specific special class, or different hospital type
    Please take class which is subclass of HospitalSpider
    '''
    query_dict = {
        "provinceId": None,
        "htype": '',
        "hgrade": None,
        "hclass": '1',
        "hname": ''
    }

    def __init__(self, province_id):
        self.query_dict['provinceId'] = province_id
        self.start_url += '?' + parse.urlencode(self.query_dict)

    def parse(self, response):
        response_items = json.loads(response.body.decode('utf-8'))
        for response_item in response_items:
            item = HospitalInforItem(response_item['provinceId'],
                                     response_item['hType'],
                                     response_item['hGrade'],
                                     response_item['hName'])
            yield item
    
