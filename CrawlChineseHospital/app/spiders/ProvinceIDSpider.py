from urllib import parse
from lxml import html

from .SpiderBase import Spider

class ProvinceIDSpider(Spider):
    base_url = "https://www.hqms.org.cn"
    path = "/usp/roster/index.jsp"
    start_url = parse.urljoin(base_url, path)

    def parse(self, response):
        x_element = html.document_fromstring(response.body.decode('utf-8'))
        
    

