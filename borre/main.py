from typing import List, Union
from borre.player import Player
import borre.parametres as params


class Borre:
    def __init__(
        self,
        players: Union[List[Player], Player]
    ) -> None:
        self.is_running = True
        self.players = players

        # Checking how many players are there
        if type(self.players) is list and all(isinstance(player, Player) for player in self.players):
            self.num_of_players = len(self.players)
        elif isinstance(self.players, Player):
            self.num_of_players = 1
        else:
            raise ValueError("Please use Player instances for player parameter.")


