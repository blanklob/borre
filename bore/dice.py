import random
import constants

class Dice:
    def __init__(
        self,
        sides: int = constants.NB_DICE_SIDE
    ) -> None:
        self.sides = sides

    def roll (self) -> int:
        """
        Perform a roll, and return the value of the roll
        """
        return random.randint(1, self.sides)


class Set:
    def __init__(
        self,
        number_of_dices: int = constants.DEFAULT_DICES_NB
    ) -> None:
        self.number_of_dices = number_of_dices
        self.dices = []
        self.occurences = [0] * constants.NB_DICE_SIDE

        for _ in range(self.number_of_dices):
            self.dices.append(Dice())


    def roll(self) -> list:
        """
        Perform a roll of a number of dices
        """
        for dice in self.dices:
            if type(dice) is Dice:
                # the dice.roll() method returns a random integer
                # between 1 and 6
                result = dice.roll()
                self.occurences[result-1] += 1

        return self.occurences


class Player:
    def __init__(
        self,
        username: str
    ) -> None:
        self.username = username
        self.score = 0
        self.is_playing = False


    def __repr__(self) -> str:
        return f'You are {self.username} and your score is {self.score} points'


class Party:
    def __init__(self, player: Player) -> None:
        self.set = Set()
        self.player = player
        self.score = 0


    def __repr__(self) -> str:
        return f'Player {self.player} is playing and has stacked a score of {self.score} points'


    def run(self) -> None:
        """
        Rolls a set of dice
        """
        self.set.roll()


    def get_standard_score(self) -> int:
        """
        Calculate and returns the standard party score
        """
        result = (
            self.set.occurences[constants.LIST_SCORING_DICE_VALUE[0]-1] * constants.LIST_SCORING_MULTIPLIER[0]
            + self.set.occurences[constants.LIST_SCORING_DICE_VALUE[1]-1] * constants.LIST_SCORING_MULTIPLIER[1]
        )

        return result


    def get_bonus_score(self) -> int:
        """
        Calculate and returns bonus score if there is any combos
        """
        score = 0
        for index, occurrence in enumerate(self.set.occurences):
            num_of_bonus = occurrence // constants.TRIGGER_OCCURRENCE_FOR_BONUS

        if num_of_bonus:
            if not index:
                bonus_multiplier = constants.BONUS_VALUE_FOR_ACE_BONUS
            else:
                bonus_multiplier = constants.BONUS_VALUE_FOR_NORMAL_BONUS

            score += num_of_bonus * bonus_multiplier * (index + 1)
            self.set.occurences[index] %= constants.TRIGGER_OCCURRENCE_FOR_BONUS

        return score


    # score getter
    def get_score(self) -> int:
        """
        Returns the global game score
        """
        self.score = self.standard_score() + self.bonus_score()

        return self.score



class Game:
    def __init__(self, num_of_players: list) -> None:
        self.party = Party()
        self.winner = None
        self.num_of_players = num_of_players


    def score(self) -> int:
        pass


    def lunch(self) -> None:
        print(self.party)
        self.party.run()
