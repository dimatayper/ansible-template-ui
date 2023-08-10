#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017-2018 Matt Martz
# Copyright 2023 Dmitry Titov
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import re
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def read_file(file_path, encoding='utf-8'):
    """Utility function to read a file."""
    with open(file_path, 'r', encoding=encoding) as f:
        return f.read()


def find_version(*file_paths):
    """Extract the version from the given file."""
    version_file = read_file(os.path.join(here, *file_paths), 'latin1')

    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Get the long description from the README
long_description = ''
requirements = []

try:
    long_description = read_file('README.rst')
except FileNotFoundError:
    pass

try:
    requirements = read_file('requirements.txt').splitlines()
except FileNotFoundError:
    pass


setup(
    name='ansible_template_ui',
    version=find_version('ansible_template_ui/__init__.py'),
    description='Web UI for testing ansible templates',
    long_description=long_description,
    keywords='ansible jinja jinja2 template ansible-template-ui',
    author='Matt Martz, Dmitry Titov',
    author_email='matt@sivel.net, pointtitov@yandex.com',
    url='https://github.com/sivel/ansible-template-ui',
    license='Apache License, Version 2.0',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=requirements,
    package_data={
        '': ['client/*']
    },
)
