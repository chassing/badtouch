# -*- coding: utf-8 -*-

import logging
import requests
import xmltodict

log = logging.getLogger(__name__)


class BadTouchHttp(object):
    def __init__(self, base_url):
        self._base_url = base_url

    def _resp2dict(self, response):
        log.debug(response.text)
        return xmltodict.parse(response.text, encoding="utf-8")

    def get(self, path):
        return self._resp2dict(requests.get(self._base_url + path))

    def post(self, path, data):
        return self._resp2dict(requests.post(self._base_url + path, data=data))
