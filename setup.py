# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 14:51:12 2018

@author: Jedidiah Yohan
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fornax",
    version="0.0.1",
    author="Jedidiah Yohan Enioluwa",
    author_email="kouduraninci@gmail.com",
    description="A Port to python of Fornax.Net Search Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/koudura/FornaxPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
)
