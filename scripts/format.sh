#!/bin/sh -e
set -x

poetry run black bore_game tests
