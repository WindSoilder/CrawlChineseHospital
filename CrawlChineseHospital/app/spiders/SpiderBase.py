from tornado import gen
from tornado.httpclient import AsyncHTTPClient

class Spider:
    start_url = None
    http_client = AsyncHTTPClient()

    @gen.coroutine
    def start_request(self):
        response = yield self.http_client.fetch(self.start_url)
        return response

    def parse(self, response):
        raise NotImplementedError()
            
