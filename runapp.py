from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from tornado import gen

from CrawlChineseHospital.app.spiders.HospitalSpider3A import HospitalSpider3A
from CrawlChineseHospital.app.SpiderRunner import Runner
from CrawlChineseHospital.app.spiders.ProvinceIDSpider import ProvinceIDSpider
from CrawlChineseHospital.app.pipelines.OutputToConsolePipeline import OutputToConsolePipeline

@gen.coroutine
def main():
    #runner = Runner(HospitalSpider3A('7216'))
    runner = Runner(ProvinceIDSpider(), pipelines=[OutputToConsolePipeline()])
    crawl_items = yield runner.run()
    ########################################
    #client = AsyncHTTPClient()
    #spider = HospitalSpider3A()
    #print("in main")
    #print(type(spider.crawl3AHospital(client)))
    #response = yield spider.crawl3AHospital(client)
    #spider.parse(response)
    #################################################

if __name__ == '__main__':
    IOLoop.current().run_sync(main)

