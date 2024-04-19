#! /usr/bin/env bash
set -uvx
set -e
cp -rp ~/.pypirc $USERPROFILE/
pip install twine
twine upload dist/*
