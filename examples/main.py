import borre


def main() -> None:
    dice = borre.Dice(
        sides=6
    )

    print(dice.rolls())


if __name__ == "__main__":
    main()
