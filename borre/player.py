from borre.dice import Dice
import borre.parametres as params
from typing import List


class Player:
    """
    A Player has some proporties such as name, score
    and number of times he rolled a dice.
    """
    counter = 0

    def __init__(
        self,
        username: str,
        is_moderator: bool = False
    ) -> None:
        """
        Initialize the player and give it a username
        """
        self.id = Player.counter
        self.username = username
        self.score = 0
        self.nb_of_plays = 0
        self.is_moderator = is_moderator

        Player.counter += 1


    def play(
        self,
        dice: Dice,
        number_of_rolls: int = params.DEFAULT_DICES_NUMBER,
    ) -> List[int]:
        """
        Rolls a dice a number_of_rolls times and updated the plays tracker
        """
        self.nb_of_plays += 1
        return dice.rolls(number_of_rolls)


    def __repr__(self) -> str:
        """
        Prints the player info when called using print
        """
        return f"You are: {self.username} and your score: {self.score} points/n"


