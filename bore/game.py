from . import constants 
from .player import Player
from .dice import Party


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

