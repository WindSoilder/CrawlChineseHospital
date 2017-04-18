import sys

from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from tornado import gen

from CrawlChineseHospital.app.spiders.HospitalSpider3A import HospitalSpider3A
from CrawlChineseHospital.app.SpiderRunner import Runner
from CrawlChineseHospital.app.spiders.ProvinceIDSpider import ProvinceIDSpider
from CrawlChineseHospital.app.pipelines.OutputToConsolePipeline import OutputToConsolePipeline
from CrawlChineseHospital.app.filters.CityNameFilter import CityNameFilter

@gen.coroutine
def main(province_name):
    def get_province_id(province_name):
        '''
        given province name as well as crawled province id items
        argument:
                province_name - the name of province, which can be Chinese or pinying format
        return: province_id
        '''
        return '7216'
        inner_dict = {}
        province_chinese_name = inner_dict.get(province_name, province_name)

    province_idrunner = Runner(ProvinceIDSpider())
    crawl_items = yield province_idrunner.run()
    crawl_items = dict(crawl_items)
    province_id = get_province_id(province_name)
    hospital_runner = Runner(HospitalSpider3A(province_id), pipelines=[OutputToConsolePipeline()])
    yield hospital_runner.run()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("you should run this program with one argument to indicate province name")
        print("e.g: python queryHospital.py 广东")
        print("or: python queryHospital.py GuangDong")
    else:
        province_name = sys.argv[1]
        IOLoop.current().run_sync(lambda : main(province_name))
