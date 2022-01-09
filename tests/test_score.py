import borre

TEST_OCCURENCES_1 = [1, 0, 3, 1, 0, 1]
TEST_OCCURENCES_2 = [3, 0, 1, 1, 1, 0]
TEST_OCCURENCES_3 = [0, 2, 1, 1, 0, 2]

def test_standard_score() -> None:
    """
    it should check if the standard score rules are
    working with diffrent occurences samples
    """
    test_occurences_1_score = borre.Score(TEST_OCCURENCES_1.copy())
    test_occurences_2_score = borre.Score(TEST_OCCURENCES_2.copy())
    test_occurences_3_score = borre.Score(TEST_OCCURENCES_3.copy())

    assert test_occurences_1_score.standard_score == 100
    assert test_occurences_2_score.standard_score == 350
    assert test_occurences_3_score.standard_score == 0


def test_bonus_score() -> None:
    """
    it should check if the bonus score rules are
    working with diffrent occurences samples
    """
    test_occurences_1_score = borre.Score(TEST_OCCURENCES_1.copy())
    test_occurences_2_score = borre.Score(TEST_OCCURENCES_2.copy())
    test_occurences_3_score = borre.Score(TEST_OCCURENCES_3.copy())

    assert test_occurences_1_score.bonus_score == 300
    assert test_occurences_2_score.bonus_score == 1000
    assert test_occurences_3_score.bonus_score == 0


def test_global_score() -> None:
    """
    it should check if the global score rules are
    working with diffrent occurences samples
    """
    test_occurences_1_score = borre.Score(TEST_OCCURENCES_1.copy())
    test_occurences_2_score = borre.Score(TEST_OCCURENCES_2.copy())
    test_occurences_3_score = borre.Score(TEST_OCCURENCES_3.copy())

    assert test_occurences_1_score.global_score == 400
    assert test_occurences_2_score.global_score == 1050
    assert test_occurences_3_score.global_score == 0
