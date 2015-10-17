# -*- coding: utf-8 -*-

import pytest
from badtouch.key import KEYS


@pytest.mark.parametrize("key, expected", zip(KEYS, len(KEYS) * [{'status': '/key'}]))
def test_dynamic_shortcut_methods(vcr, bt, key, expected):
    with vcr.use_cassette("select_key"):
        # get shortcut method and call it
        assert getattr(bt.key, key.lower())() == expected


def test_not_predefined_method_not_a_dynamic_method(bt):
    with pytest.raises(AttributeError):
        bt.key.does_not_exists("DOES_NOT_EXISTS")
