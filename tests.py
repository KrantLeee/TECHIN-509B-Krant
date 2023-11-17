import io
import sys
import unittest
import logic
import cli


class TestLogic(unittest.TestCase):
    def test_make_empty_board(self):
        b1 = logic.business_logic()
        result = b1.make_empty_board()
        expected = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(result, expected)
    
    #All possibilities in get_winner function
    def test_get_winner_row(self):
        b1 = logic.business_logic()
        b1.board = [
            ['X', 'X', 'X'],
            [None, 'O', None],
            [None, None, 'O'],
        ]
        self.assertEqual(b1.get_winner('X'), 'X')

    def test_get_winner_column(self):
        b2 = logic.business_logic()
        b2.board = [
            ['X', None, 'O'],
            ['X', 'O', None],
            ['X', None, 'O'],
        ]
        self.assertEqual(b2.get_winner('X'), 'X')

    def test_get_winner_diagonal(self):
        b3 = logic.business_logic()
        b3.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            ['O', None, 'X'],
        ]
        self.assertEqual(b3.get_winner('X'), 'X')

    def test_get_winner_draw(self):
        b4 = logic.business_logic()
        b4.board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertIsNone(b4.get_winner('X'))
        self.assertIsNone(b4.get_winner('O'))
    
    def test_get_winner_no_winner_yet(self):
        b5 = logic.business_logic()
        b5.board = [
            ['X', 'O', 'X'],
            ['X', None, 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertIsNone(b5.get_winner('X'))
        self.assertIsNone(b5.get_winner('O'))
    #End of check_winner unit tests

    def test_check_draw(self):
        b6 = logic.business_logic()
        b6.board = [
            ['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(b6.check_draw(), True)

    def test_next_player(self):
        b7 = logic.business_logic()
        b7.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(b7.next_player(), 'O')


class TestCli(unittest.TestCase):
    def test_show_board(self):
        u1 = cli.user_interaction(logic.business_logic())
        u1.board = [
            ['X', 'O', 'X'],
            [None, 'X', 'O'],
            ['O', None, None]
        ]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        u1.show_board()
        sys.stdout = sys.__stdout__
        expected_output = "X | O | X\n——— ——— ———\n  | X | O\n——— ——— ———\nO |   |  \n"
        self.assertEqual(expected_output, captured_output.getvalue())
       


if __name__ == '__main__':
    unittest.main()
