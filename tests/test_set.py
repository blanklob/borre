from bore_game.dice import Set


def test_set_of_dices():
    """
    Tests the number of sides
    """
    num_of_dices = 10
    set_of_dices = Set(num_of_dices)

    assert set_of_dices.number_of_dices == num_of_dices
