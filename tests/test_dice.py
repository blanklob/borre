from bore_game.dice import Dice
import random


def test_dice_sides():
    """
    Tests the number of sides
    """
    num_of_sides = 9
    dice = Dice(num_of_sides)

    assert dice.sides == num_of_sides


def test_dice_roll():
    """
    Tests the generated dice combination
    """
    test_dice_seed = random.randint(0, 100)
    test_dice_sides = random.randint(1, 100)

    random_dice_set = random.Random(test_dice_seed)
    dice = Dice(test_dice_sides, test_dice_seed)

    assert random_dice_set.randint(1, test_dice_sides) == dice.roll()
