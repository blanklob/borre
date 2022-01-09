# Borre

> Borre is a dead simple Farkle 🎲 dice game implementation and game maker made using Python for a School project.

[![PyPi version][pypi-badge]][pypi-url]
[![Tests][tests-badge]][tests-url]

Game rules are simple, you usually have five dices with six sides, you roll the set of dices, and check if you score bonus or regular standard points.

## Requirements

This package supports the following minimum versions:

* Python >= 3.7

If you have Python installed, just skip to Usage, otherwise [install Python][python-url].

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

Or create a multipe players

```python
import borre

bob = borre.Player("Bob")
alice = borre.Player("Alice")

# Bob plays with 6 Dices
print(bob.play(borre.Dice(6)))

# Alice plays with only 2 Dices
print(alice.play(borre.Dice(2)))
```

> If you have any difficulties, you might as well check the examples in `examples` folder.

## Getting help

If you have a question about the library, or are having difficulty using it,
chat with the community in [GitHub Discussions](/discussions)..

## Contributing

Everyone is welcome to make this package better feel free to submit your pull request/feature request.

<!-- Markdown links & img dfn's -->
[tests-url]: https://img.shields.io/github/workflow/status/idbakkasse/borre/tests
[tests-badge]: https://img.shields.io/github/workflow/status/idbakkasse/borre/Tests?label=Tests&logo=github&style=flat-square

[coverage-url]: https://codecov.io/gh/idbakkasse/borre
[coverage-badge]: https://img.shields.io/codecov/c/github/idbakkasse/borre?style=flat-square

[pypi-badge]: https://img.shields.io/pypi/v/borre?color=blue&label=pypi%20package&style=flat-square
[pypi-url]: https://pypi.org/project/borre

[python-url]: https://www.python.org
