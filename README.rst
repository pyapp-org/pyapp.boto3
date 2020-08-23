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



The default settings will obtain configuration from your environment.

Or they can be customised via the `AWS_CREDENTIALS` block in your runtime
settings file::

    AWS_CREDENTIALS = {
        "default": {
            "default_region": "ap-southeast2"
        }
    }


Usage
=====

The following example creates an S3 `Resource` instance::

    from pyapp_ext.boto3 import resource

    # Get resource
    s3 = resource("S3")


API
===

`pyapp_ext.boto3.get_session(config_name: str = None)`

    Get named Boto3 `Session` instance


`pyapp_ext.boto3.client(service_name: str, config_name: str = None, **client_args)`

    Get named Boto3 `Client` instance


`pyapp_ext.boto3.resource(service_name: str, config_name: str = None, **resource_args)`

    Get named Boto3 `Resource` instance
