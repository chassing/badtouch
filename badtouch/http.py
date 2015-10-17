# -*- coding: utf-8 -*-

import requests
import xmltodict


class BadTouchHttp(object):
    def __init__(self, base_url):
        self._base_url = base_url

    def _resp2dict(self, response):
        return xmltodict.parse(response.text)

    def get(self, path):
        return self._resp2dict(requests.get(self._base_url + path))
