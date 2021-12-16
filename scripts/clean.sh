#!/bin/sh -e

if [ -d 'dist' ] ; then
    rm -r dist
fi

if [ -d '.tox' ] ; then
    rm -r .tox
fi
