import io
import sys
import unittest
from unittest.mock import patch

from board import Board
from cell import Cell


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
        """place_ships positions all five ships according to randint outputs."""
        # Arrange deterministic placement: for each ship i, place it
        # horizontally at row=i, columns 0..size-1
        side_effects = []
        for i, ship in enumerate(self.board._ships):
            side_effects.extend([0, i, 0])  # loc_fit=0, loc=i, orient=0
        mock_randint.side_effect = side_effects

        # Act
        self.board.place_ships()

        # Assert each ship's segments
        for i, ship in enumerate(self.board._ships):
            for x in range(ship.get_size()):
                cell = self.board._board[i][x]
                self.assertTrue(cell.has_ship(), f"Expected ship at ({i},{x})")
                self.assertEqual(cell.get_cell(), ship.get_symbol())

        # And total ship-cells equals sum of ship sizes
        total_cells = sum(ship.get_size() for ship in self.board._ships)
        count = sum(
            1 for row in self.board._board for cell in row if cell.has_ship()
        )
        self.assertEqual(count, total_cells)

    @patch('board.random.randint')
    def test_attack_and_repeats(self, mock_randint):
        """attack returns correct hit/miss and raises on repeat."""
        # Same deterministic placement for all five ships
        side_effects = []
        for i, ship in enumerate(self.board._ships):
            side_effects.extend([0, i, 0])
        mock_randint.side_effect = side_effects

        self.board.place_ships()

        # Hit the first ship at (0,0)
        self.assertTrue(self.board.attack(0, 0))
        self.assertEqual(self.board._board[0][0].get_cell(), "H")

        # Miss somewhere else
        self.assertFalse(self.board.attack(5, 5))
        self.assertEqual(self.board._board[5][5].get_cell(), "M")

        # Re-attacking the same cell raises
        with self.assertRaises(ValueError):
            self.board.attack(0, 0)

    def test_check_endgame_and_clean_board(self):
        """check_endgame reflects all ships sunk; clean_board resets cells."""
        # Initially no ship is sunk
        self.assertFalse(self.board.check_endgame())

        # Sink every ship fully
        for ship in self.board._ships:
            for _ in range(ship.get_size()):
                ship.is_hit()
        self.assertTrue(self.board.check_endgame())

        # clean_board should reset every cell to water and remove ships
        self.board.clean_board()
        for y in range(self.board._board_size):
            for x in range(self.board._board_size):
                cell = self.board._board[y][x]
                self.assertEqual(cell.get_cell(), "~")
                self.assertFalse(cell.has_ship())

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
