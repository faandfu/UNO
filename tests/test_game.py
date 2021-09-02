from src.Game import Game


def test_init_game():
    game = Game()

def test_run_game():
    game = Game(False, 2)
    game.run()
