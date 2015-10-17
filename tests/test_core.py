# -*- coding: utf-8 -*-

import pytest
from dpath.util import get


@pytest.mark.parametrize("key, expected", [
    ("@deviceID", "000C8A8A33FD"),
    ("name", "Bose Portable"),
    ("type", "SoundTouch Portable"),
    ("margeAccountUUID", "2842201"),
])
def test_info(vcr, bt, key, expected):
    with vcr.use_cassette("info"):
        assert get(bt.info, key) == expected


@pytest.mark.parametrize("key, expected", [
    ("@source", "INTERNET_RADIO"),
    ("stationName", "Antenne Bayern"),
    ("playStatus", "PLAY_STATE"),
    ("description", "MP3  128 kbps  Ismaning Germany,  Wir lieben Bayern. Wir lieben die Hits."),
    ("stationLocation", "Ismaning Germany"),
    ("ContentItem/itemName", "Antenne Bayern"),
    ('ContentItem/@source', "INTERNET_RADIO"),
    ('ContentItem/@location', "13771"),
    ('ContentItem/@sourceAccount', ""),
    ('ContentItem/@isPresetable', "true"),
])
def test_now_playing_antenne_is_playing(vcr, bt, key, expected):
    with vcr.use_cassette("antenne_is_playing"):
        assert get(bt.now_playing, key) == expected


@pytest.mark.parametrize("key, expected", [
    ("@source", "STANDBY"),
    ("ContentItem/@source", "STANDBY"),
])
def test_now_playing_nothing_is_playing(vcr, bt, key, expected):
    with vcr.use_cassette("nothing_is_playing"):
        assert get(bt.now_playing, key) == expected
