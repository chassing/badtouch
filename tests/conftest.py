# -*- coding: utf-8 -*-

# add code to sys.path
import os
import sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR + '/../')

import pytest
import vcr as vcrpy

from badtouch import BadTouch

# setup logging
import logging
logging.basicConfig()
logging.getLogger("vcr").setLevel(logging.INFO)
logging.getLogger("badtouch").setLevel(logging.DEBUG)


@pytest.fixture
def vcr():
    return vcrpy.VCR(
        cassette_library_dir=CURRENT_DIR + '/fixtures',
        path_transformer=vcrpy.VCR.ensure_suffix('.yaml'),
        record_mode='once'
    )


@pytest.fixture
def bt():
    return BadTouch("bose-portable.local")
