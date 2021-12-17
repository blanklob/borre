import bore_game
import logging

logger = logging.getLogger(__name__)

def main():
    game = bore_game.Bore()
    game.lunch()


if __name__ == "__main__":
    main()

