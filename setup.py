
import os
import sys

try:
    from setuptools import setup, find_packages
    from setuptools.extension import Extension
except ImportError:
    from distutils.core import setup, find_packages
    from distutils.extension import Extension

from py2neo import __license__

extra_opts = {}

python_2 = sys.version_info < (3,)

try:
    with open("README.md", "r") as fd:
        extra_opts['long_description'] = fd.read()
except IOError:
    pass        # Install without README.md

packages = find_packages(exclude=("book", "examples", "examples.*", "test", "test.*"))
package_metadata = {
    "name": "neo4j_doc_manager",
    "version": "1.0.0.dev",
    "description": "Neo4j Doc manager for Mongo Connnector",
    "long_description": "Neo4j Doc Manager is a tool that will import data in Mongodb for a" 
                        "Neo4j graph structure, via Mongo-Connector.",
    "author": "Neo4j Team",
    "author_email": "contact@neo4j.com",
    "url": "http://neo4j.org/",
    "entry_points": {
        "console_scripts": [
        ],
    },
    "packages": packages,
    "license": "",
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Database",
        "Topic :: Software Development",
    ],
    "zip_safe": False,
}


try:
    setup(ext_modules=extensions, **package_metadata)
except:
    setup(**package_metadata)
