"""Bore is a dead simple Dice game"""

__version__ = "0.1.1"


from . import parametres as parametres
from .dice import Dice as Dice
from .main import Bore as Bore
from .player import Player as Player
from .utils import get_player_input as get_player_input
