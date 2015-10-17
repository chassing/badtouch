========
BadTouch
========

A friendly python library for the `Bose SoundTouch (R) API <http://products.bose.com/api-developer/index.html>`_.

.. image:: https://travis-ci.org/chassing/badtouch.svg?branch=develop
    :target: https://travis-ci.org/chassing/badtouch


Installation
------------

To install badtouch python library, simply:

.. code-block:: shell

    pip install badtouch


``badtouch`` requires Python >= 3.4.


Quick Start
-----------

Connect to your Bose SoundTouch (R) device and retrieve basic device information:


.. code-block:: python

    from badtouch import BadTouch

    bt = BadTouch("bose-portable.local")
    print(bt.info)


Links
-----

TODO
