#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup

# Package meta-data
NAME = "dummy-framework"
DESCRIPTION = "Dummy Python Web Framework built for learning purposes."
EMAIL = "bmachin7@gmail.com"
AUTHOR = "Byron Machin"
REQUIRES_PYTHON = ">=3.11.0"
VERSION = "0.0.1"

# Which packages are required for this module to be executed?
REQURIED = [
    "WebOb==1.8.8",
    "parse==1.20.2",
    "Jinja2==3.1.4",
    "whitenoise==6.7.0",
    "requests==2.32.3",
    "requests-wsgi-adapter==0.4.1",
]

# The rest you shouldn't have to touch too much

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the Long-description
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dict.

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

# Where the "magic" happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=["test_"]),
    install_requires=REQURIED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Languaje :: Python :: 3.11",
    ],
    setup_requires=["wheel"],
)