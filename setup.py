from setuptools import setup

import re
import sys


# extract html5validator version from __init__.py
with open("w3c_validator/__init__.py", "r") as f:
    INIT = f.read()
    VERSION = next(re.finditer("__version__ = \"(.*?)\"", INIT)).group(1)

setup(
    name="W3C Validator",
    version=VERSION,
    packages=["w3c_validator", ],
    license="MIT",
    long_description=open("README.md").read(),
    install_requires=["requests", ],
    entry_poins={
        "console_scripts": [
            "w3c_validator = w3c_validator.validator:main",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
