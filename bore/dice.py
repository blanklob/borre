import random
import constants

class Dice:
    def __init__(
        self,
        sides: int = constants.NB_DICE_SIDE
    ) -> None:
        self.sides = sides

    def __repr__(self) -> str:
        return f'Dice with {self.sides} sides'


    def roll (self) -> int:
        """
        Perform a roll, and return the value of the roll
        """
        return random.randint(1, self.sides)