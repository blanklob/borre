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
    'version': '0.1.5',
    'description': 'Borre is a dead simple Frakle Dice game maker',
    'long_description': '# Borre\n\n> Borre is a dead simple Farkle 🎲 dice game implementation and game maker made using Python for a School project.\n\n[![PyPi version][pypi-badge]][pypi-url]\n[![Tests][tests-badge]][tests-url]\n\nGame rules are simple, you usually have five dices with six sides, you roll the set of dices, and check if you score bonus or regular standard points.\n\n## Requirements\n\nThis package supports the following minimum versions:\n\n* Python >= 3.7\n\nIf you have Python installed, just skip to Usage, otherwise [install Python][python-url].\n\n> Earlier versions may still work, but we encourage people building new applications\nto upgrade to the current stable.\n\n## Usage\n\nFirst, you will need to install the **borre** package localy\n\n```shell\npip install borre\n```\n\nTo quickly start, with a simple Dice\n\n```python\nimport borre\n\ndice = borre.Dice()\n\n# Rolls the dice once\nprint(dice.roll())\n```\n\nOr create a multiple players\n\n```python\nimport borre\n\nbob = borre.Player("Bob")\nalice = borre.Player("Alice")\n\n# Bob plays with 6 Dices\nprint(bob.play(borre.Dice(6)))\n\n# Alice plays with only 2 Dices\nprint(alice.play(borre.Dice(2)))\n```\n\n> If you have any difficulties, you might as well check the examples in `examples` folder.\n\n## Getting help\n\nIf you have a question about the library, or are having difficulty using it,\nchat with the community in [GitHub Discussions](/discussions)..\n\n## Contributing\n\nEveryone is welcome to make this package better feel free to submit your pull request/feature request.\n\n<!-- Markdown links & img dfn\'s -->\n[tests-url]: https://img.shields.io/github/workflow/status/idbakkasse/borre/tests\n[tests-badge]: https://img.shields.io/github/workflow/status/idbakkasse/borre/Tests?label=Tests&logo=github&style=flat-square\n\n[coverage-url]: https://codecov.io/gh/idbakkasse/borre\n[coverage-badge]: https://img.shields.io/codecov/c/github/idbakkasse/borre?style=flat-square\n\n[pypi-badge]: https://img.shields.io/pypi/v/borre?color=blue&label=pypi%20package&style=flat-square\n[pypi-url]: https://pypi.org/project/borre\n\n[python-url]: https://www.python.org\n',
    'author': 'Youness Idbakkasse',
    'author_email': 'youness@idbakkasse.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
