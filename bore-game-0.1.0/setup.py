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
    'version': '0.1.0',
    'description': 'README.md',
    'long_description': None,
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
