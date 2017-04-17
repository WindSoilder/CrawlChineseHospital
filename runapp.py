from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from tornado import gen

from CrawlChineseHospital.app.spiders.HospitalSpider3A import HospitalSpider3A
from CrawlChineseHospital.app.SpiderRunner import Runner

@gen.coroutine
def main():
    runner = Runner(HospitalSpider3A('7216'))
    yield runner.run()
    
    ########################################
    #client = AsyncHTTPClient()
    #spider = HospitalSpider3A()
    #print("in main")
    #print(type(spider.crawl3AHospital(client)))
    #response = yield spider.crawl3AHospital(client)
    #spider.parse(response)
    #################################################

IOLoop.current().run_sync(main)

