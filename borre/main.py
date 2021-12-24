from typing import List
import logging

import borre.parametres as params
from borre.party import Party
from borre.player import Player


class Borre:
    def __init__(
        self,
        num_of_players: int = params.DEFAULT_PLAYERS_NUMBER,
    ) -> None:
        self.winner = None
        self.num_of_players = num_of_players
        self.is_running = True
        self.players = []

        # todo: function that creates players
        for _ in range(self.num_of_players):
            self.players.append(Player(username=str(_)))

    def score(self) -> List[Player]:
        """
        Check each players global game score
        """
        for player in self.players:
            print(player)

        return self.players

    def lunch(self) -> None:
        """
        Lunch the main game loop
        """
        while self.is_running:
            for player in self.players:
                logging.warning(f"Player {player.username} will play...")
                party = Party(player)
                party.run()

                if player.score >= params.DEFAULT_TARGET_SCORE:
                    self.is_running = False
                    print(f"The player {player.username} won Bore 🎉.")
                    break
