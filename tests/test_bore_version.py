import bore_game

# Initiate the game
game = bore_game.Bore()


def test_bore_version():
    """
    Tests the version number
    """
    assert game.is_running == True
