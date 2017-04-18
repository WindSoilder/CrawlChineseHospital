from collections import Iterable

from tornado import gen

from .spiders.HospitalSpider3A import HospitalSpider3A
from .spiders.HospitalSpider2A import HospitalSpider2A

class Runner:
    def __init__(self, spider, filters = [], pipelines = []):
        self.spider = spider
        self.filters = filters
        self.pipelines = pipelines

    @gen.coroutine
    def run(self):
        response = yield self.spider.start_request()
        item_generator = self.spider.parse(response)

        if isinstance(item_generator, Iterable):
            for item in item_generator:
                check_success = self._filter_chcek(item)
            if check_success:
                self._go_through_pipeline(item)

    def _filter_check(self, item):
        pass

    def _go_through_pipeline(self, item):
        pass
