import constants
from player import Player
from dice import Dice
from utils import (
    get_player_input
)


class Set:
    def __init__(
        self,
        number_of_dices: int = constants.DEFAULT_DICES_NB
    ) -> None:
        self.number_of_dices = number_of_dices
        self.dices = []
        self.occurences = [0] * constants.NB_DICE_SIDE
        self.score = 0

        for _ in range(self.number_of_dices):
            self.dices.append(Dice())


    def __repr__(self) -> str:
        set_repr = ''
        for dice_value in self.occurences:
            set_repr += f'*{dice_value}: {self.occurences[dice_value -1]} /n'
        return set_repr


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



class Party:
    def __init__(
        self,
        player: Player
    ) -> None:
        self.player = player
        self.score = 0
        self.number_of_dices_left = constants.DEFAULT_DICES_NB
        self.is_running = True


    def __repr__(self) -> str:
        return f"""
        The player {self.player.username} is playing and has stacked a score of 
        {self.score} points, there are {self.number_of_dices_left} dices left.
        """


    def run(self) -> None:
        """
        Rolls a set of dice
        """
        while self.is_running:
            self.set = Set(self.number_of_dices_left)
            self.set.roll()

            print(self.set.occurences)

            self.set.score += self.calculate_standard_score()
            self.set.score += self.calculate_bonus_score()

            self.score += self.set.score
            self.number_of_dices_left = sum(self.set.occurences)

            self.validate()

        self.player.score += self.score


    def calculate_standard_score(self) -> int:
        """
        Calculate and returns the standard party score
        """
        score = 0
        for dice_value, score_multiplier in constants.LIST_SCORING_MERGED:
            score += self.set.occurences[dice_value - 1] * score_multiplier

            # Remove dices who were eligible to standard score
            self.set.occurences[dice_value - 1] = 0

        return score


    def calculate_bonus_score(self) -> int:
        """
        Calculate and returns the global score if there is any combos
        """
        score = 0
        for index, occurrence in enumerate(self.set.occurences):
            num_of_bonus = occurrence // constants.TRIGGER_OCCURRENCE_FOR_BONUS

            if num_of_bonus:
                if index == 0:
                    score += num_of_bonus * constants.BONUS_VALUE_FOR_ACE_BONUS
                else:
                    score += num_of_bonus * constants.BONUS_VALUE_FOR_NORMAL_BONUS * (index + 1)

            # Reset items who have bonus score
            self.set.occurences[index] %= constants.TRIGGER_OCCURRENCE_FOR_BONUS
 
        return score


    def validate(self) -> None:
        """
        Validate if the player wishes to continue the party and roll another set,
        or if has no more scoring Dices left 
        """
        if (self.set.score == 0):
            self.score = 0
            self.is_running = False
            return None

        if (self.number_of_dices_left == 0):
            player_input = get_player_input("Do you want to reset the game ? (Yes or Non)")

            if (player_input == "non"):
                self.is_running = False
            else:
               self.number_of_dices_left = constants.DEFAULT_DICES_NB 

        else:
            player_input = get_player_input("Do you want to continue ? (Yes or Non)")

            if (player_input == "non"):
                self.is_running = False

    


class Game:
    def __init__(
        self,
        num_of_players: list = constants.DEFAULT_PLAYERS_NUMBER,
    ) -> None:
        self.winner = None
        self.num_of_players = num_of_players
        self.is_running = True
        self.players = []

        # todo: function that creates players
        for _ in range(self.num_of_players):
            self.players.append(Player(username=str(_)))


    def score(self) -> int:
        """
        Check each players global game score
        """
        for player in self.players:
            print(player)


    def lunch(self) -> None:
        """
        Lunch the main game loop
        """
        while self.is_running:
            for player in self.players:
                print(f'Player {player.username} will play...')
                party = Party(player)
                party.run()

                print(party)
                if player.score >= constants.DEFAULT_TARGET_SCORE:
                    self.is_running = False
                    print(f'The player {player.username} won Bore 🎉.')
                    break

