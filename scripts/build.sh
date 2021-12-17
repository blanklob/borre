#!/bin/sh -e

set -x

poetry build -n
tar -xvf dist/*.tar.gz '*/setup.py'
cp $(find . -name setup.py) setup.py
