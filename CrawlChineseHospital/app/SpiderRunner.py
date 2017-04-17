from tornado import gen

from .spiders.HospitalSpider3A import HospitalSpider3A
from .spiders.HospitalSpider2A import HospitalSpider2A

class Runner:
    def __init__(self, spider):
        self.spider = spider

    @gen.coroutine
    def run(self):
        response = yield self.spider.start_request()
        for item in self.spider.parse(response):
            print(item)

        
