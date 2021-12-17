import random, logging
from typing import List

import bore_game.parametres as params


class Dice:
    def __init__(self, sides: int = params.NB_DICE_SIDE, seed: None = None) -> None:
        try:
            if sides < 1:
                raise ValueError
        except ValueError:
            logging.exception("Sorry, the Dice must have at least one side.")
            return None

        self.sides = sides
        self.seed = seed

    def __repr__(self) -> str:
        return f"Dice with {self.sides} sides"

    def roll(self) -> int:
        """
        Perform a roll, and return the value of the roll
        """
        if self.seed is not None:
            random_dice = random.Random(self.seed)
            return random_dice.randint(1, self.sides)

        return random.randint(1, self.sides)


class Set:
    def __init__(
        self,
        number_of_dices: int = params.DEFAULT_DICES_NB,
        number_of_dices_sides: int = params.NB_DICE_SIDE,
        score: int = 0,
    ) -> None:
        """
        Initializing a set of dices with a predifined amount of sides/faces
        """
        self.number_of_dices = number_of_dices
        self.occurences = [0 for _ in range(number_of_dices_sides)]
        self.dices = [Dice(number_of_dices_sides) for _ in range(number_of_dices_sides)]
        self.score = score

    def __repr__(self) -> str:
        """
        This built-in methods is callback when we call a print on the element,
        here we construct the printed string with a for loop
        """
        set_repr = ""
        for dice_value in self.occurences:
            set_repr += f"*{dice_value}: {self.occurences[dice_value -1]} /n"

        return set_repr

    def roll(self) -> List[int]:
        """
        Perform a roll of a number of dices
        """
        for dice in self.dices:
            if type(dice) is Dice:
                # the dice.roll() method returns a random integer
                # between 1 and 6
                result = dice.roll()
                # saving the results in the occurrences array
                self.occurences[result - 1] += 1

        return self.occurences
