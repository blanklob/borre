#!/bin/sh -e


if [ -d 'dist' ] ; then
  rm -r dist
fi

if [ -d '.tox' ] ; then
  rm -r .tox
fi

if [ -d '.mypy_cache' ] ; then
  rm -r .mypy_cache
fi

if [ -d '.pytest_cache' ] ; then
  rm -r .pytest_cache
fi
