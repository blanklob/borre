import borre
import random



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

    dice = borre.Dice(
        sides=test_number_sides
    )

    assert dice is None

