import random, logging
from typing import List, Union
import borre.parametres as params


class Dice:
    """
    A Dice has a certain number of sides and
    methods that roll the dice a number of times.
    """
    counter = 0

    def __init__(
        self,
        sides: int = params.DEFAULT_DICE_SIDES_NUMBER,
    ) -> None:

        if not sides:
            raise ValueError("Sorry, the Dice must have at least one side.")

        self.sides = sides
        Dice.counter += 1


    def __repr__(self) -> str:
        """
        Print informations about an exact dice.
        """
        return f"Dice number #{self.counter} with {self.sides} sides"


    def roll(
        self,
        seed: Union[None, int] = None
    ) -> int:
        """
        Perform a roll, and return the value of the roll.
        """
        if seed is not None:
            random.seed(seed)

        return random.randint(1, self.sides)


    def rolls(
        self,
        number_of_rolls: int = params.DEFAULT_DICES_NUMBER
    ) -> List[int]:
        """
        Perform a number_of_rolls, and returns a list of value occurences,
        if somehow we perform a great amount of rolls, we might use the data
        stored to draw the famous Gauss curve.
        """
        value_occurences = [0 for _ in range(self.sides)]

        for _ in range(number_of_rolls):
            value_occurences[self.roll() - 1] += 1

        return value_occurences

