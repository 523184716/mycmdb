#coding:utf-8

import urllib
import urllib2

class Postdata:
    """
      默认接口不接受cookie
    """

    def __init__(self, url, data):
        self.url = url
        self.data = urllib.urlencode(data)

    def get_request(self, header={}):
        self.request = urllib2.Request(self.url, data=self.data, headers=header)

    def get_response(self):
        self.response = urllib2.urlopen(self.request)
        result = self.response.read()
        return result

