#!/bin/sh -e

set -x

if [ -d 'bore-game-*' ] ; then
  rm -r bore-game-*
fi

poetry build -n
tar -xvf dist/*.tar.gz '*/setup.py'
cp $(find . -name setup.py) setup.py
mv bore-game-*/setup.py ..
