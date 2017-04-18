from urllib import parse
from lxml import html

from .SpiderBase import Spider

class ProvinceIDSpider(Spider):
    '''
    A spider to crawl province id
    the crawl result will be used for send information to fetch hospital information
    '''
    base_url = "https://www.hqms.org.cn"
    path = "/usp/roster/index.jsp"
    start_url = parse.urljoin(base_url, path)

    def parse(self, response):
        x_element = html.document_fromstring(response.body.decode('utf-8'))
        father_option_xpath = '//select[@class="province_select"]/option'
        province_names = x_element.xpath(father_option_xpath + '/text()')
        province_ids = x_element.xpath(father_option_xpath + '/@value')

        for i in range(len(province_ids)):
            if province_ids[i]:
                yield (province_names[i], province_ids[i])
