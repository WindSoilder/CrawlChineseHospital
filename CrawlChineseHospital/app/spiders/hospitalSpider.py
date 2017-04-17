import urllib

from tornado.ioloop import IOLoop
from tornado import gen

class HospitalSpider:
    server_name = "https://www.hqms.org.cn/"
    server_path = "/usp/roster/rosterInfo.jsp?"
    crawl_url = urllib.parse.urljoin(server_name, server_path)
    _query_argument = None

    @gen.coroutine
    def crawl(self, url):
        raise NotImplementedError()

    @property
    def query_argument(self):
        if _query_argument is None:
            raise TypeError("The property value of query_argument must not be none!")

    @query_argument.setter
    def query_argument(self, value):
        if type(value) == dict:
            self._query_argument = urllib.parse.urlencode(value)
        elif type(value) == str:
            self._query_argument = value
        else:
            raise TypeError("must assign dict or string object to query_argument property")

class HospitalSpider3A(HospitalSpider):
    query_argument = {'provinceId': '7216', 'htype': '', 'hgrade': '1', 'hclass': '1', 'hname': ''}

    @gen.coroutine
    def crawl3AHospital(self, client):
        serverName = "https://www.hqms.org.cn/"
        serverPath = "usp/roster/rosterInfo.jsp?"
        url = serverName + serverPath + urllib.parse.urlencode(self.__class__.query_argument)
        
        response = yield client.fetch(url)
        return response

    def parse(self, response):
        print(response.body.decode('utf-8'))
