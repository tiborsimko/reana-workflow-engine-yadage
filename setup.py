# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2025 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REANA-Workflow-Engine-Yadage."""

from __future__ import absolute_import, print_function

import os
import re

from setuptools import find_packages, setup

readme = open("README.md").read()
history = open("CHANGELOG.md").read()

tests_require = [
    "pytest-reana>=0.9.2,<0.10.0",
]

extras_require = {
    "debug": [
        "wdb",
        "ipdb",
        "Flask-DebugToolbar",
    ],
    "docs": [
        "myst-parser",
        "Sphinx>=1.5.1",
        "sphinx-rtd-theme>=0.1.9",
    ],
    "tests": tests_require,
    # Using older jq on amd64 due to https://github.com/reanahub/reana-demo-bsm-search/issues/21
    "jq": [
        "jq==0.1.7; platform_machine == 'x86_64'",
        "jq==1.2.2; platform_machine == 'aarch4'",
        "jq==1.2.2; platform_machine == 'arm64'",
    ],
    "pygraphviz": [
        "pygraphviz>=1.5",
    ],
}

extras_require["all"] = []
for key, reqs in extras_require.items():
    if ":" == key[0]:
        continue
    extras_require["all"].extend(reqs)


setup_requires = [
    "pytest-runner>=2.7",
]

install_requires = [
    "graphviz>=0.12",  # FIXME needed only if yadage visuale=True.
    "pydot>=1.0.29",  # FIXME needed only if yadage visuale=True.
    "pydotplus>=2.0.2",  # FIXME needed only if yadage visuale=True.
    # Pinning adage/packtivity/yadage/yadage-schemas to make sure we use compatible versions.
    # See https://github.com/reanahub/reana-workflow-engine-yadage/pull/236#discussion_r992475484
    "adage==0.10.1",
    "packtivity==0.14.24",
    "yadage==0.20.1",
    "yadage-schemas==0.10.6",
    "reana-commons[yadage]>=0.9.11,<0.10.0",
    "requests>=2.25.1",
    "rfc3987==1.3.8",  # FIXME remove once yadage-schemas solves yadage deps.
]

packages = find_packages()


# Get the version string. Cannot be done with import!
with open(os.path.join("reana_workflow_engine_yadage", "version.py"), "rt") as f:
    version = re.search(r'__version__\s*=\s*"(?P<version>.*)"\n', f.read()).group(
        "version"
    )

setup(
    name="reana-workflow-engine-yadage",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    author="REANA",
    author_email="info@reana.io",
    url="https://github.com/reanahub/reana-workflow-engine-yadage",
    packages=[
        "reana_workflow_engine_yadage",
    ],
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "run-yadage-workflow="
            "reana_workflow_engine_yadage.cli:run_yadage_workflow",
        ]
    },
    extras_require=extras_require,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
