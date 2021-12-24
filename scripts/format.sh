#!/bin/sh -e

set -x

poetry run black borre tests examples
