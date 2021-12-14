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

    def __repr__(self) -> str:
        # todo: Use a loop
        return f"""
            *1: {self.occurences[0]}
            *2: {self.occurences[1]}
            *3: {self.occurences[2]}
            *4: {self.occurences[3]}
            *5: {self.occurences[4]}
            *6: {self.occurences[5]}
        """

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
    def __init__(
        self,
        player: Player
    ) -> None:
        self.set = Set()
        self.player = player
        self.score = 0
        self.number_of_dices_left = constants.DEFAULT_DICES_NB
        self.is_running = True


    def __repr__(self) -> str:
        return f"""
        The player {self.player.username} is playing and has stacked a score of {self.score} points
        and there is {self.number_of_dices_left} dices left.
        """


    def run(self) -> None:
        """
        Rolls a set of dice
        """
        while self.is_running:
            self.set.roll()

            self.calculate_standard_score()
            self.calculate_bonus_score()
            self.player.score = self.score

            self.validate_playing()
            print(self)


    def calculate_standard_score(self) -> int:
        """
        Calculate and returns the standard party score
        """
        for dice_value, score_multiplier in constants.LIST_SCORING_MERGED:
            self.score += self.set.occurences[dice_value - 1] * score_multiplier

            # Reset items who are eligible for bonus score
            self.set.occurences[dice_value - 1] = 0

        return self.score


    def calculate_bonus_score(self) -> int:
        """
        Calculate and returns the global score if there is any combos
        """
        for index, occurrence in enumerate(self.set.occurences):
            num_of_bonus = occurrence // constants.TRIGGER_OCCURRENCE_FOR_BONUS

            if num_of_bonus:
                if not index:
                    self.score += num_of_bonus * constants.BONUS_VALUE_FOR_ACE_BONUS * (index + 1)
                else:
                    self.score += num_of_bonus * constants.BONUS_VALUE_FOR_NORMAL_BONUS * (index + 1)

            # Reset items who have bonus score
            self.set.occurences[index] %= constants.TRIGGER_OCCURRENCE_FOR_BONUS

        return self.score

    def validate_playing(self):
        """
        Validate if the player wants to continue the game if he lost
        """
        self.number_of_dices_left = sum(self.set.occurences)
        if(not self.number_of_dices_left):
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

        for _ in range(self.num_of_players):
            self.players.append(Player(username=str(_)))

        self.party = Party(self.players[0])


    def score(self) -> int:
        for player in self.players:
            print(player)


    def lunch(self) -> None:
        print('Game lunching..')
        self.party.run()

