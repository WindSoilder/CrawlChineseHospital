from urllib import parse

from .SpiderBase import Spider

class HospitalSpider(Spider):
    base_url = "https://www.hqms.org.cn"
    path = "/usp/roster/rosterInfo.jsp"
    start_url = parse.urljoin(base_url, path)
    query_dict = {}


class CommomHospitalSpider(HospitalSpider):
    query_dict = {
        "provinceID": None,
        "htype": '',
        "hgrade": None,
        "hclass": '1',
        "hname": ''
    }
    
