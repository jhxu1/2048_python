import unittest
from screen import Screen

class TestScreen(unittest.TestCase):
    def test_move_up(self):
        tmp_screen = Screen(height=3, width=3)
        # case1
        mock_data = [['X', 'X', 'X'], ['X', 'X', 'X'], [2, 2, 2]]
        tmp_screen._data = mock_data
        tmp_screen._move_up()
        self.assertEqual(tmp_screen.data, [[2, 2, 2], ['X', 'X', 'X'], ['X', 'X', 'X']])

        # case2
        mock_data = [['X', 'X', 'X'], ['X', 2, 'X'], [2, 2, 2]]
        tmp_screen._data = mock_data
        tmp_screen._move_up()
        self.assertEqual(tmp_screen.data, [[2, 4, 2], ['X', 'X', 'X'], ['X', 'X', 'X']])

        # case3
        mock_data = [['X', 4, 'X'], ['X', 2, 'X'], [2, 2, 2]]
        tmp_screen._data = mock_data
        tmp_screen._move_up()
        self.assertEqual(tmp_screen.data, [[2, 4, 2], ['X', 4, 'X'], ['X', 'X', 'X']])

    def test_move_left(self):
        tmp_screen = Screen(height=3, width=3)
        # case1
        mock_data = [['X', 'X', 'X'], ['X', 'X', 'X'], [2, 2, 2]]
        tmp_screen._data = mock_data
        tmp_screen._move_left()
        self.assertEqual(tmp_screen.data, [['X', 'X', 'X'], ['X', 'X', 'X'], [4, 2, 'X']])
        
if __name__ == '__main__':
    unittest.main()