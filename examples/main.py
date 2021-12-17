import logging
import bore_game


logger = logging.getLogger(__name__)


def main() -> None:
    game = bore_game.Bore()
    game.lunch()


if __name__ == "__main__":
    main()
