HBMQTT
======

``HBMQTT`` is an open source `MQTT`_ client and broker implementation.

Built on top of :mod:`asyncio`, Python's standard asynchronous I/O framework, HBMQTT provides a straightforward API
based on coroutines, making it easy to write highly concurrent applications.

Features
--------

HBMQTT implements the full set of `MQTT 3.1.1`_ protocol specifications and provides the following features:

- Support QOS_0, QOS_1 and QOS_2 messages flow
- Client auto-reconnection on network lost
- Authentication through password file (more methods can be added through a plugin system)
- Basic ``$SYS`` topics
- TCP and websocket support
- SSL support over TCP and websocket
- Plugin system

Build status
------------

.. image:: https://travis-ci.org/beerfactory/hbmqtt.svg?branch=develop
    :target: https://travis-ci.org/beerfactory/hbmqtt

    [![Build Status](https://travis-ci.org/beerfactory/hbmqtt.svg?branch=master)](https://travis-ci.org/beerfactory/hbmqtt)


.. image:: https://coveralls.io/repos/beerfactory/hbmqtt/badge.svg?branch=develop&service=github
    :target: https://coveralls.io/github/beerfactory/hbmqtt?branch=develop

.. image:: https://readthedocs.org/projects/hbmqtt/badge/?version=latest
    :target: http://hbmqtt.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

Getting started
---------------

hbmqtt is available on `Pypi <https://pypi.python.org/pypi/hbmqtt>`_ and can installed simply using ``pip`` :

    $ pip install hbmqtt

Documentation is available on `Read the Docs`_.

Bug reports, patches and suggestions welcome! Just `open an issue`_ or join the `forum`_.


.. _Read the Docs: http://hbmqtt.readthedocs.org/
.. _open an issue: https://github.com/beerfactory/hbmqtt/issues/new
.. _forum: http://forum.beerfactory.org/c/hbmqtt
