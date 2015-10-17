# -*- coding: utf-8 -*-

import logging

from cached_property import cached_property_with_ttl

from .exceptions import BadTouchUnkownKeyException
from .http import BadTouchHttp
from .key import KEYS


log = logging.getLogger(__name__)


class BadTouch(object):
    def __init__(self, device, http=BadTouchHttp):
        self._device = device
        self._http = http(base_url="http://{}:8090".format(self._device))

    @cached_property_with_ttl(ttl=5 * 60)
    def info(self):
        return self._http.get("/info")["info"]

    @property
    def now_playing(self):
        return self._http.get("/now_playing")["nowPlaying"]

    @cached_property_with_ttl(ttl=60)
    def presets(self):
        return self._http.get("/presets")["presets"]["preset"]

    @property
    def volume(self):
        return self._http.get("/volume")["volume"]

    @volume.setter
    def volume(self, level):
        self._http.post("/volume", data="<volume>{}</volume>".format(level))

    @property
    def bass(self):
        return self._http.get("/bass")["bass"]

    @bass.setter
    def bass(self, level):
        self._http.post("/bass", data="<bass>{}</bass>".format(level))

    @cached_property_with_ttl(ttl=60)
    def bass_capabilities(self):
        return self._http.get("/bassCapabilities")["bassCapabilities"]

    @cached_property_with_ttl(ttl=60)
    def sources(self):
        return self._http.get("/sources")["sources"]["sourceItem"]

    @property
    def key(self):
        raise BadTouchUnkownKeyException()

    @key.setter
    def key(self, button):
        button = button.upper()
        if button not in KEYS:
            raise BadTouchUnkownKeyException()

        log.debug("press {}".format(button))
        self._http.post("/key", data="<key state='press' sender='Gabbo'>{}</key>".format(button))
        log.debug("release {}".format(button))
        self._http.post("/key", data="<key state='release' sender='Gabbo'>{}</key>".format(button))
