# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bore_game']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['example = examples.main:main',
    'game = bore_game.main:game']}

setup_kwargs = {
    'name': 'bore-game',
    'version': '0.1.2-alpha',
    'description': 'Bore is a dead simple Dice game',
    'long_description': '## Bore\n\nBore is a dead simple Dice 🎲 game made using Python. (School project 📖)\n\n[![Tests](https://github.com/younessidbakkasse/bore/actions/workflows/ci.yml/badge.svg)](https://github.com/younessidbakkasse/bore/actions/workflows/ci.yml)\n[![Code Quality](https://github.com/younessidbakkasse/bore/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/younessidbakkasse/bore/actions/workflows/quality.yml)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)\n\n## Requirements\n\nThis package supports the following minimum versions:\n\n* Python >= 3.6.2\n\nIf you have Python installed, just skip to Usage, otherwise [install Python 3.6](https://www.python.org/downloads/release/python-360/)\n\n> Dont forget to set the python PATH in your machine.\n> [→ Learn more about Paths](https://www.javatpoint.com/how-to-set-python-path).\n\nEarlier versions may still work, but we encourage people building new applications\nto upgrade to the current stable.\n\n## Usage\n\nAfter the installation, you will need to install the **bore_game** package localy, to do so use the commande below:\n\n```shell\npython -m pip install -e .\n```\n\nThe main game example entrypoint is in the **main.py** file, run the command below to start the game.\n\n```shell\npython examples/main.py\n```\n\n## Getting help\n\nIf you have a question about the library, or are having difficulty using it,\nchat with the community in [GitHub Discussions](https://github.com/younessidbakkasse/bore/discussions)..\n\n\n## Contributing\n\nEveryone is welcome to make this game batter feel free to submit your PR 😀.\n\n',
    'author': 'Youness Id bakkasse',
    'author_email': 'std.youness@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2',
}


setup(**setup_kwargs)
