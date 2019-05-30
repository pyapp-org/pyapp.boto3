"""
PyApp - Boto 3 Extension

This extension provides a factory method for using Boto 3 with AWS.

"""
from pyapp.versioning import get_installed_version

from .factory import *

__name__ = "PyApp Boto 3 Extension"
__version__ = get_installed_version("pyApp-Boto3", __file__)
__default_settings__ = ".default_settings"
__checks__ = ".checks"
