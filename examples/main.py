import borre

# Creating the players
youness = borre.Player("Youness")
david = borre.Player("David")

# intiating the game
game = borre.Borre(
    players = [youness, david]
)

# Runing the game
def main() -> None:
    game.players[0].play(borre.Dice())
    print(game.players)


if __name__ == "__main__":
    main()
