#!/usr/bin/env bash

set -e
set -x

poetry run mypy borre/dice.py examples
