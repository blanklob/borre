"""
Borre is a dead simple Farkle dice game implementation and game maker,
game rules are simple, you usually have five dices with six
sides, you roll the set of dices, and check if you score bonus
or regular standard points.

Made by a Youness Idbakkasse, David, Alexandre for a School project
at Hetic.
"""

__version__ = "0.1.5"


from .main import Borre as Borre
from .dice import Dice as Dice
from .player import Player as Player
from .score import Score as Score


