"""Validate HTML5 files."""

import pkg_resources

__all__ = (
    '__version__',
)

dist = pkg_resources.get_distribution("Online-W3C-Validator")
__version__ = dist.version

# flake8: noqa
from .validator import *

