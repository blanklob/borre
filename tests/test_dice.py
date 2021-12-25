import borre, pytest
from borre.dice import Dice
import random



def test_dice_counter():
    """
    it should check if the global Dice counter
    is working.
    """
    test_number_of_dices = 10

    for _ in range(test_number_of_dices):
        borre.Dice()

    assert Dice.counter == test_number_of_dices


def test_dice_sides():
    """
    It should create a dice with 100 sides.
    """
    test_number_sides = 100

    dice = borre.Dice(
        sides=test_number_sides
    )

    assert dice.sides == test_number_sides


def test_dice_sides_exception():
    """
    It should return an error since we're trying
    to create a dice without sides.
    """
    test_number_sides = 0

    with pytest.raises(ValueError):
        borre.Dice(
            sides=test_number_sides
        )


def test_dice_roll():
    """
    It should roll a dice and returns a specific
    dice value.
    """
    test_seed = 100

    rnd = random.Random(test_seed)
    dice = borre.Dice()

    assert dice.roll(test_seed) == rnd.randint(1, dice.sides)


def test_dice_rolls_occurrences():
    """
    It should roll a dice n=100 number of times and
    return an occurence list with sum of occurences
    equals the number of rolls.
    """
    test_number_of_rolls = 100

    dice = borre.Dice()

    assert sum(dice.rolls(test_number_of_rolls)) == test_number_of_rolls


def test_dice_rolls_sides():
    """
    It should roll a dice five times, which is the default,
    but in this case we have a dice with 100 sides, which
    implies that occurrence list should also contain 100 value.
    """
    test_number_of_sides = 100

    dice = borre.Dice(
        sides=test_number_of_sides
    )

    assert len(dice.rolls()) == test_number_of_sides
