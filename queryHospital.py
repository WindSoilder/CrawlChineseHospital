import sys

from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from tornado import gen

from CrawlChineseHospital.app.SpiderRunner import Runner
from CrawlChineseHospital.app.ProvinceData import ProvinceInformation
from CrawlChineseHospital.app.filters.CityNameFilter import CityNameFilter
from CrawlChineseHospital.app.pipelines.OutputToConsolePipeline import OutputToConsolePipeline
from CrawlChineseHospital.app.spiders.HospitalSpiderFactory import HospitalSpiderFactory
from CrawlChineseHospital.app.spiders.ProvinceIDSpider import ProvinceIDSpider

description_string = '''
You should run this program with 1 to 2 arguments to indicate province name and hospital grade.
Hospital grade should be 2 or 3.
example:
        python queryHospital.py Guangdong 2
This command will query all grade 2 class A hospital in Guangdong province
        python queryHospital.py Hebei 3
This command will query all grade 3 class A hospital in Hebei province
If you don't specify hospital grade or the value is not 2 or 3, the grade value will go to default 3
'''

@gen.coroutine
def main(province_name, grade_num):
    def get_province_id(province_name):
        '''
        given province name as well as crawled province id items
        argument:
                province_name - the name of province, which can be Chinese or pinying format
        return: province_id
        '''
        province_chinese_name = ProvinceInformation.get(province_name, province_name)
        return crawl_items[province_chinese_name]

    province_idrunner = Runner(ProvinceIDSpider())
    crawl_items = yield province_idrunner.run()
    crawl_items = dict(crawl_items)
    province_id = get_province_id(province_name)
    hospital_runner = Runner(HospitalSpiderFactory.create_hospital_spider(grade_num, province_id),
                             pipelines=[OutputToConsolePipeline()])
    yield hospital_runner.run()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(description_string)
    else:
        province_name = sys.argv[1]
        if len(sys.argv) == 3 and \
           (sys.argv[2] == '2' or sys.argv[2] == '3') :
            grade_num = sys.argv[2]
        else:
            grade_num = 3
        IOLoop.current().run_sync(lambda : main(province_name, grade_num))
