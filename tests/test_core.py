# -*- coding: utf-8 -*-

import pytest


@pytest.mark.parametrize("key, expected", [
    ("@deviceID", "000C8A8A33FD"),
    ("name", "Bose Portable"),
    ("type", "SoundTouch Portable"),
    ("margeAccountUUID", "2842201"),
])
def test_info(vcr, bt, key, expected):
    with vcr.use_cassette("info"):
        assert bt.info[key] == expected
