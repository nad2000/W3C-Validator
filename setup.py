import re

from setuptools import setup

with open("w3c_validator/__init__.py", "r") as f:
    VERSION = next(re.finditer("__version__ = \"(.*?)\"", f.read())).group(1).strip()

setup(
    name="Online-W3C-Validator",
    author="Radomirs Cirskis",
    author_email="nad2000@gmail.com",
    version=VERSION,
    url="https://github.com/nad2000/W3C-Validator",
    project_urls={
        "Source Code": "https://github.com/nad2000/W3C-Validator",
    },
    packages=[
        "w3c_validator",
    ],
    license="MIT",
    long_description=open("README.md").read(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "w3c_validator=w3c_validator.validator:main",
        ]
    },
    keywords=[
        'html validator',
        'html',
        'validator',
        'checker',
        'html5',
        'w3',
    ],
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
    ])
