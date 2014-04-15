# -*- coding: utf-8 -*-

"""setup.py: setuptools control."""

import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('hiptoslack/hiptoslack.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "hiptoslack",
    packages = ["hiptoslack"],
    entry_points = {
        "console_scripts": ['hiptoslack = hiptoslack.hiptoslack:main']
        },
    version = version,
    description = "Python command line application bare bones template.",
    long_description = long_descr,
    author = "Marcin Mincer",
    author_email = "marcin@bladepolska.com",
    url = "http://www.bladepolska.com",
    requires = ['clint']
    )
