# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)

from .exceptions import BadTouchUnkownKeyException


PLAY = "PLAY"
PAUSE = "PAUSE"
STOP = "STOP"
PREV_TRACK = "PREV_TRACK"
NEXT_TRACK = "NEXT_TRACK"
THUMBS_UP = "THUMBS_UP"
THUMBS_DOWN = "THUMBS_DOWN"
BOOKMARK = "BOOKMARK"
POWER = "POWER"
MUTE = "MUTE"
VOLUME_UP = "VOLUME_UP"
VOLUME_DOWN = "VOLUME_DOWN"
PRESET_1 = "PRESET_1"
PRESET_2 = "PRESET_2"
PRESET_3 = "PRESET_3"
PRESET_4 = "PRESET_4"
PRESET_5 = "PRESET_5"
PRESET_6 = "PRESET_6"
AUX_INPUT = "AUX_INPUT"
SHUFFLE_OFF = "SHUFFLE_OFF"
SHUFFLE_ON = "SHUFFLE_ON"
REPEAT_OFF = "REPEAT_OFF"
REPEAT_ONE = "REPEAT_ONE"
REPEAT_ALL = "REPEAT_ALL"
PLAY_PAUSE = "PLAY_PAUSE"
ADD_FAVORITE = "ADD_FAVORITE"
REMOVE_FAVORITE = "REMOVE_FAVORITE"

KEYS = [
    PLAY, PAUSE, STOP, PREV_TRACK, NEXT_TRACK, THUMBS_UP, THUMBS_DOWN, BOOKMARK, POWER, MUTE, VOLUME_UP,
    VOLUME_DOWN, PRESET_1, PRESET_2, PRESET_3, PRESET_4, PRESET_5, PRESET_6, AUX_INPUT, SHUFFLE_OFF, SHUFFLE_ON,
    REPEAT_OFF, REPEAT_ONE, REPEAT_ALL, PLAY_PAUSE, ADD_FAVORITE, REMOVE_FAVORITE
]


class Key(object):
    def __init__(self, bt):
        self.bt = bt

    def __getattr__(self, attr):
        """ create for each possible soundtouch key a class method as shortcut
        """
        if attr in [k.lower() for k in KEYS]:
            return lambda: self.bt.select_key(attr.upper())
        raise AttributeError()

    def send_key(self, key):
        if key not in KEYS:
            raise BadTouchUnkownKeyException()

        log.debug("press {}".format(key))
        self.bt._http.post("/key", data="<key state='press' sender='Gabbo'>{}</key>".format(key))
        log.debug("release {}".format(key))
        return self.bt._http.post("/key", data="<key state='release' sender='Gabbo'>{}</key>".format(key))
