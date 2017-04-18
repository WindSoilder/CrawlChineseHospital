from collections import Iterable

from tornado import gen

from .spiders.HospitalSpider3A import HospitalSpider3A
from .spiders.HospitalSpider2A import HospitalSpider2A

class Runner:
    '''
    Spider runner, along with item filters and pipelines
    filters will filter item which not match requirement
    and pipelines will do something to item, like save it to database, or output item information to console
    '''
    def __init__(self, spider, filters = [], pipelines = []):
        self.spider = spider
        self.filters = filters
        self.pipelines = pipelines

    @gen.coroutine
    def run(self):
        response = yield self.spider.start_request()
        item_generator = self.spider.parse(response)
        final_items = []

        if isinstance(item_generator, Iterable):
            for item in item_generator:
                check_success = self._filter_check(item)
                if check_success:
                    final_items.append(item)
                    self._go_through_pipeline(item)

        return final_items

    def _filter_check(self, item):
        # this method is sync, how to make it async
        # just,,,,in the bottom level, how to make this filter check function async
        for filter in self.filters:
            if filter(item):
                return False
        return True

    def _go_through_pipeline(self, item):
        for pipeline in self.pipelines:
            pipeline(item)
