#! /usr/bin/env bash
set -uvx
set -e
pip install wheel setuptools
rm -rf dist
python setup.py bdist_wheel
