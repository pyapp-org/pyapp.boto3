#############
pyApp - Boto3
#############

*Let us handle the boring stuff!*

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
      :alt: Once you go Black...

This extension provides a factory method for using Boto 3 to allow configuration to be
configured via pyApp settings.

The extension also provides checks to confirm the settings are correct and
that the application is able to connect to the redis instance.


Installation
============

Install using *pip*::

    pip install pyapp-boto3

Install using *pipenv*::

    pipenv install pyapp-boto3


Add `pae.boto3` into the `EXT` list in your applications
`default_settings.py`.

The default settings will obtain configuration from your environment.

Or they can be customised via the `AWS_CREDENTIALS` block in your runtime
settings file::

    AWS_CREDENTIALS = {
        "default": {
            "default_region": "ap-southeast2"
        }
    }


.. note::

    The URL is a defined by Redis client see the
    `documentation <https://github.com/andymccurdy/redis-py/blob/master/redis/client.py#L599>`_.
    In addition to the url any argument that can be provided to `Redis.from_url` can be provided.


Usage
=====

The following example creates both `Connection` and `Session` instances::

    from pae.redis import get_client

    # Get connection
    redis = get_client()

    redis.set("foo")


API
===

`pae.redis.get_client(default: str = None) -> Redis`

    Get named `Redis` client instance
