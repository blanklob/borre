import borre


def test_player_counter() -> None:
    """
    it should check if the global Players counter
    is working
    """
    test_number_of_players = 10
    test_username = "Bob"

    for _ in range(test_number_of_players):
        borre.Player(username=test_username)

    assert borre.Player.counter == test_number_of_players


def test_player_plays_tracker() -> None:
    """
    it should check if the how many times a player
    has played in a match
    """
    test_player_1 = borre.Player("Bob")
    test_player_2 = borre.Player("Alice")

    test_player_1_plays = 3
    test_player_2_plays = 10

    for _ in range(test_player_1_plays):
        test_player_1.play(borre.Dice())

    for _ in range(test_player_2_plays):
        test_player_2.play(borre.Dice())

    assert test_player_1.nb_of_plays == test_player_1_plays
    assert test_player_2.nb_of_plays == test_player_2_plays

