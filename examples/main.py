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
    occurence = game.players[0].play(borre.Dice())
    occurence_score = borre.Score(occurence)
    print(occurence, occurence_score.global_score)


if __name__ == "__main__":
    main()
