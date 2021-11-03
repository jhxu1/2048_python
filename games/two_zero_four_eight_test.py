import unittest
from common.player import Player
from games.two_zero_four_eight import TwoZeroFourEightPlayer, TwoZeroFourEightScreen, TwoZeroFourEightGame
import os
import json

class TestScreen(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        config_path = os.path.join(os.getcwd(), "config/two_zero_four_eight.json")
        self.config = json.load(open(config_path, "r"))

    def test_init_screen(self):
        screen = TwoZeroFourEightScreen(self.config)
        screen.init()

    def test_init_player(self):
        player = Player(name="xiaoxu", id="0000")

    def test_init_game(self):
        game = TwoZeroFourEightGame(self.config)
        player = Player(name="xiaoxu", id="000")
        game.add_player(player)




    # def test_move_up(self):
    #     tmp_screen = Screen(height=3, width=3)
    #     # case1
    #     mock_data = [['X', 'X', 'X'], ['X', 'X', 'X'], [2, 2, 2]]
    #     tmp_screen._data = mock_data
    #     tmp_screen._move_up()
    #     self.assertEqual(tmp_screen.data, [[2, 2, 2], ['X', 'X', 'X'], ['X', 'X', 'X']])

    #     # case2
    #     mock_data = [['X', 'X', 'X'], ['X', 2, 'X'], [2, 2, 2]]
    #     tmp_screen._data = mock_data
    #     tmp_screen._move_up()
    #     self.assertEqual(tmp_screen.data, [[2, 4, 2], ['X', 'X', 'X'], ['X', 'X', 'X']])

    #     # case3
    #     mock_data = [['X', 4, 'X'], ['X', 2, 'X'], [2, 2, 2]]
    #     tmp_screen._data = mock_data
    #     tmp_screen._move_up()
    #     self.assertEqual(tmp_screen.data, [[2, 4, 2], ['X', 4, 'X'], ['X', 'X', 'X']])

    # def test_move_left(self):
    #     tmp_screen = Screen(height=3, width=3)
    #     # case1
    #     mock_data = [['X', 'X', 'X'], ['X', 'X', 'X'], [2, 2, 2]]
    #     tmp_screen._data = mock_data
    #     tmp_screen._move_left()
    #     self.assertEqual(tmp_screen.data, [['X', 'X', 'X'], ['X', 'X', 'X'], [4, 2, 'X']])
        
if __name__ == '__main__':
    unittest.main()