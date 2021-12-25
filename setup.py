# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['borre']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['example = examples.main:main']}

setup_kwargs = {
    'name': 'borre',
    'version': '0.1.3',
    'description': 'Borre is a dead simple Dice game maker',
    'long_description': "# Borre\n\n> Borre is a dead simple Farkle 🎲 dice game implementation and game maker made using Python as a School project.\n\n[![PyPi version](https://badgen.net/pypi/v/borre/)](https://pypi.com/project/borre)\n[![Tests][tests-badge]][tests-url]\n\nGame rules are simple, you usually have five dices with six sides, you roll the set of dices, and check if you score bonus or regular standard points.\n\n## Requirements\n\nThis package supports the following minimum versions:\n\n* Python >= 3.6\n\nIf you have Python installed, just skip to Usage, otherwise [install Python 3.6][python-url].\n\n> Earlier versions may still work, but we encourage people building new applications\nto upgrade to the current stable.\n\n## Usage\n\nFirst, you will need to install the **borre** package localy\n\n```shell\npip install borre\n```\n\nTo quickly start, with a simple Dice\n\n```python\nimport borre\n\ndice = borre.Dice()\n\n# Rolls the dice once\nprint(dice.roll())\n```\n\n> If you have any difficulties, you might as well check the examples in `examples` folder.\n\n## Getting help\n\nIf you have a question about the library, or are having difficulty using it,\nchat with the community in [GitHub Discussions](/discussions)..\n\n## Contributing\n\nEveryone is welcome to make this package better feel free to submit your pull request/feature request.\n\n<!-- Markdown links & img dfn's -->\n[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg\n[black-url]: https://github.com/psf/black\n\n[tests-url]: https://github.com/younessidbakkasse/borre/actions/workflows/ci.yml\n[tests-badge]: https://github.com/younessidbakkasse/borre/actions/workflows/ci.yml/badge.svg\n\n[python-url]: https://www.python.org\n",
    'author': 'Youness Id bakkasse',
    'author_email': 'hi@younessidbakkasse.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
