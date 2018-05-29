"""Validate HTML5 files."""

__all__ = (
    '__version__',
    'version_info'
)

from pbr.version import VersionInfo

_v = VersionInfo('mock').semantic_version()
__version__ = _v.release_string()
version_info = _v.version_tuple()

# flake8: noqa
from .validator import *

