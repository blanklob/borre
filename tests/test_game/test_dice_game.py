from bore.game import Game

game = Game()


def test_dice_game():
    assert game.is_running == True