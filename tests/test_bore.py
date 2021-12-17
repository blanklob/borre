import bore_game

bore = bore_game.Bore()


def test_bore():
    """
    Tests bore
    """
    assert bore.is_running is True
