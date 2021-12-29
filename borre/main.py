from typing import List, Union
import borre.parametres as params
from borre.player import Player


class Borre:
    def __init__(
        self,
        players: Union[List[Player], Player]
    ) -> None:
        self.is_running = True
        self.players = players

        if type(self.players) is list and all(isinstance(player, Player) for player in self.players):
            self.num_of_players = len(self.players)
        elif isinstance(self.players, Player):
            self.num_of_players = 1
        else:
            raise ValueError("Please use Player instances for player parameter.")

    def run(self):
        pass

    def score(self):
        pass



