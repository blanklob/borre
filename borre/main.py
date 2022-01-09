from typing import List
from borre.player import Player


class Borre:
    def __init__(
        self,
        players: List[Player]
    ) -> None:
        self.is_running = True
        self.players = players

        # Checking how many players are there
        if all(isinstance(player, Player) for player in self.players):
            self.num_of_players = len(self.players)
        else:
            raise ValueError("Please use Player instances for player parameter.")


