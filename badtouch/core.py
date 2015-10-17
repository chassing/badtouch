# -*- coding: utf-8 -*-

from cached_property import cached_property_with_ttl

from .http import BadTouchHttp


class BadTouch(object):
    def __init__(self, device, http=BadTouchHttp):
        self._device = device
        self._http = http(base_url="http://{}:8090".format(self._device))

    @cached_property_with_ttl(ttl=5 * 60)
    def info(self):
        return self._http.get("/info")["info"]
