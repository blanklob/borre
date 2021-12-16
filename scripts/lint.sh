#!/usr/bin/env bash

set -e
set -x

poetry run mypy bore_game
poetry run black bore_game tests --check
