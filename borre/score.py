import borre.parametres as params
from typing import List

class Score:
    def __init__(self, occurences: List[int]) -> None:
        """
        Initiliase the scores and saves the original occurrences list
        for comparaison
        """
        self.original_occurences = occurences.copy()
        self.occurences = occurences
        self._bonus_score = 0
        self._standard_score = 0
        self._global_score = 0


    def __repr__(self) -> str:
        """
        Shows the score of the occurence list when called upon print
        """
        return f"The occurrence {self.original_occurences} gives a global score of {self.global_score} points"


    @property
    def bonus_score(self) -> int:
        """
        Compute and return the score for bonus rules
        Basicly if we get the same dice 3 times, we multiply
        it's value by 3, except for the Ice dice we get 1000pts
        Then filter the occurrences list from bonus scoring dices
        """
        for side_index, side_occurrence in enumerate(self.occurences):
            nb_of_bonus = side_occurrence // params.THRESHOLD_BONUS
            if nb_of_bonus > 0:
                if side_index == 0:
                    self._bonus_score += nb_of_bonus * params.ACE_BONUS_MULTIPLIER \
                        * (side_index + 1)
                else:
                    self._bonus_score += nb_of_bonus * params.STD_BONUS_MULTIPLIER \
                        * (side_index + 1)

                self.occurences[side_index] %= params.THRESHOLD_BONUS

        return self._bonus_score


    @property
    def standard_score(self) -> int:
        """
        Compute and return the score for standard rules
        Dice value 1 is scoring 100pts
        Dice value 5 is scoring 50
        Then filter the occurrences list from standard scoring dices
        """
        for value, multiplier in zip(params.SCORING_DICE_VALUE, params.SCORING_MULTIPLIER):
            self._standard_score += self.occurences[value - 1] * multiplier

            self.occurences[value - 1] = 0

        return self._standard_score


    @property
    def global_score(self) -> int:
        """
        Compute and return the score for global rules
        Dice value 1 is scoring 100pts
        Dice value 5 is scoring 50
        """
        self._global_score = self.bonus_score + self.standard_score
        return self._global_score
