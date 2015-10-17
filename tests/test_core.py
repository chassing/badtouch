# -*- coding: utf-8 -*-

import pytest
from dpath.util import get

from badtouch import KEYS
from badtouch.exceptions import BadTouchUnkownKeyException


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


@pytest.mark.parametrize("key", KEYS)
def test_key(vcr, bt, key):
    with vcr.use_cassette("key"):
        bt.key = key


def test_select_key_unknown_key(bt):
    with pytest.raises(BadTouchUnkownKeyException):
        bt.key = "DOES_NOT_EXISTS"


@pytest.mark.parametrize("key, expected", [
    ("@id", "1"),
    ("ContentItem/@source", "INTERNET_RADIO"),
    ("ContentItem/@location", "28754"),
    ("ContentItem/@sourceAccount", ""),
    ("ContentItem/@isPresetable", "true"),
    ("ContentItem/itemName", "radio TOP 40 Electro"),
])
def test_presets(vcr, bt, key, expected):
    with vcr.use_cassette("presets"):
        assert len(bt.presets) == 6
        p = bt.presets[0]
        assert get(p, key) == expected


@pytest.mark.parametrize("key, expected", [
    ("targetvolume", "30"),
    ("actualvolume", "30"),
    ("muteenabled", 'false'),
])
def test_volume_read(vcr, bt, key, expected):
    with vcr.use_cassette("vol_read"):
        assert get(bt.volume, key) == expected


@pytest.mark.parametrize("level", [
    (0,),
    (50,),
    (100,),
])
def test_volume_write(vcr, bt, level):
    with vcr.use_cassette("vol_write"):
        bt.volume = level


@pytest.mark.parametrize("key, expected", [
    ("targetbass", "0"),
    ("actualbass", "0"),
])
def test_bass_read(vcr, bt, key, expected):
    with vcr.use_cassette("bass_read"):
        assert get(bt.bass, key) == expected


@pytest.mark.parametrize("level", [
    (-5,),
    (0,),
    (10,),
])
def test_bass_write(vcr, bt, level):
    with vcr.use_cassette("bass_write"):
        bt.bass = level


@pytest.mark.parametrize("key, expected", [
    ("bassAvailable", "true"),
    ("bassMin", "-9"),
    ("bassMax", "0"),
    ("bassDefault", "0"),
])
def test_bass_capabilities(vcr, bt, key, expected):
    with vcr.use_cassette("bass_capabilities"):
        assert get(bt.bass_capabilities, key) == expected


@pytest.mark.parametrize("key, expected", [
    ("@source", "INTERNET_RADIO"),
    ("@status", "READY"),
])
def test_sources(vcr, bt, key, expected):
    with vcr.use_cassette("sources"):
        assert len(bt.sources) == 2
        assert get(bt.sources[0], key) == expected
