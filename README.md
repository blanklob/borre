# Borre

> Borre is a dead simple Farkle 🎲 dice game implementation and game maker made using Python as a School project.

[![PyPi version](https://badgen.net/pypi/v/borre/)](https://pypi.com/project/borre)
[![Tests][tests-badge]][tests-url]

Game rules are simple, you usually have five dices with six sides, you roll the set of dices, and check if you score bonus or regular standard points.

## Requirements

This package supports the following minimum versions:

* Python >= 3.6

If you have Python installed, just skip to Usage, otherwise [install Python 3.6][python-url].

> Earlier versions may still work, but we encourage people building new applications
to upgrade to the current stable.

## Usage

First, you will need to install the **borre** package localy

```shell
pip install borre
```

To quickly start, with a simple Dice

```python
import borre

dice = borre.Dice()

# Rolls the dice once
print(dice.roll())
```

> If you have any difficulties, you might as well check the examples in `examples` folder.

## Getting help

If you have a question about the library, or are having difficulty using it,
chat with the community in [GitHub Discussions](/discussions)..

## Contributing

Everyone is welcome to make this package better feel free to submit your pull request/feature request.

<!-- Markdown links & img dfn's -->
[tests-url]: https://github.com/idbakkasse/borre/actions/workflows/ci.yml
[tests-badge]: https://github.com/idbakkasse/borre/actions/workflows/ci.yml/badge.svg

[python-url]: https://www.python.org
