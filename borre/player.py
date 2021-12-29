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
        """
        self.id = Player.counter
        self.username = username
        self.score = 0
        self.nb_of_roll = 0
        self.nb_of_turn = 0
        self.is_moderator = is_moderator

        Player.counter += 1


    def play(
        self,
        dice: Dice,
        number_of_rolls: int = params.DEFAULT_DICES_NUMBER
    ) -> List[int]:
        """
        """
        dice = Dice(number_of_rolls)
        self.nb_of_roll += number_of_rolls
        return dice.rolls()


    def __repr__(self) -> str:
        """
        """
        return f"You are {self.username} and your score is {self.score} points"


