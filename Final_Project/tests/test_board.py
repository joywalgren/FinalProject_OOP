import unittest
import io
import sys
from unittest.mock import patch

from board import Board
from cell import Cell
from ship import Ship

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=10)

    def test_initial_state(self):
        """Board initializes with correct size and all water cells."""
        self.assertEqual(self.board._board_size, 10)
        for y in range(self.board._board_size):
            for x in range(self.board._board_size):
                cell = self.board._board[y][x]
                self.assertIsInstance(cell, Cell)
                self.assertEqual(cell.get_cell(), "~")

    def test_ship_space_free_on_empty(self):
        """ship_space_free returns True anywhere on an empty board."""
        self.assertTrue(self.board.ship_space_free(length=5, orient=0, loc_fit=0, loc=0))
        self.assertTrue(self.board.ship_space_free(length=5, orient=1, loc_fit=0, loc=0))

    @patch('board.random.randint')
    def test_place_ships(self, mock_randint):
        """place_ships positions ships according to randint outputs."""
        # For a single ship of size 5: loc_fit=0, loc=0, orient=0
        mock_randint.side_effect = [0, 0, 0]
        self.board.place_ships()
        ship = self.board._ships[0]
        for i in range(ship.get_size()):
            cell = self.board._board[0][i]
            self.assertTrue(cell.has_ship())
            self.assertEqual(cell.get_cell(), ship.get_symbol())

    @patch('board.random.randint')
    def test_attack_and_repeats(self, mock_randint):
        """attack returns correct hit/miss and raises on repeat."""
        mock_randint.side_effect = [0, 0, 0]
        self.board.place_ships()
        # hit
        self.assertTrue(self.board.attack(0, 0))
        self.assertEqual(self.board._board[0][0].get_cell(), "H")
        # miss
        self.assertFalse(self.board.attack(5, 5))
        self.assertEqual(self.board._board[5][5].get_cell(), "M")
        # repeat on hit square
        with self.assertRaises(ValueError):
            self.board.attack(0, 0)

    def test_check_endgame_and_clean_board(self):
        """check_endgame reflects sunk ships; clean_board resets cells."""
        # initially not all sunk
        self.assertFalse(self.board.check_endgame())
        # sink all ships manually
        ship = self.board._ships[0]
        for _ in range(ship.get_size()):
            ship.is_hit()
        self.assertTrue(self.board.check_endgame())
        # clean resets grid
        self.board.clean_board()
        self.assertEqual(self.board._board[0][0].get_cell(), "~")
        self.assertFalse(self.board._board[0][0].has_ship())

    def test_print_board_output(self):
        """print_board outputs header, rows, and footer."""
        captured = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured
        try:
            self.board.print_board()
        finally:
            sys.stdout = original_stdout
        lines = captured.getvalue().splitlines()
        # header + divider + 10 rows + divider = 13
        self.assertEqual(len(lines), 13)
        self.assertTrue(lines[0].startswith("    A B C D E F G H I J"))
        self.assertTrue(lines[1].startswith("   -----"))

if __name__ == '__main__':
    unittest.main() #no pragma
