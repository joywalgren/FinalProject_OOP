'''
By: McKenzie Swindler
Tests for cell class
'''

from cell import Cell
import unittest
import sys
from io import StringIO


class MockShip:
    '''A mack Ship class for testing Cell'''

    def __init__(self) -> None:
        self.hit_called: bool = False

    def is_hit(self) -> None:
        '''Simulates a ship being hit'''
        self.hit_called = True

    def get_symbol(self) -> str:
        '''returns a symbol representinng the ship'''
        return 'S'


class TestCell(unittest.TestCase):
    '''Unit tests for the Cell class'''

    def test_cell_initialization(self) -> None:
        '''Test that cell initializes correctly'''
        cell: Cell = Cell(2, 3)
        self.assertEqual(cell._x, 2)
        self.assertEqual(cell._y, 3)
        self.assertEqual(cell.get_cell(), "~")
        self.assertFalse(cell.has_ship())

    def test_set_cell_valid_markers(self) -> None:
        '''Test that setting valid markers updates the cell correctly'''
        cell: Cell = Cell(0, 0)
        for marker in ['H', 'M', 'S', '~']:
            cell.set_cell(marker)
            self.assertEqual(cell.get_cell(), marker)

    def test_set_cell_invalid_marker(self) -> None:
        '''Test that setting an invalid marker prints an error message'''
        captured_output: StringIO = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        cell: Cell = Cell(0, 0)
        cell.set_cell('X')
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertIn("Invalid Marker", captured_output.getvalue())

    def test_place_ship(self) -> None:
        '''Test placing a ship'''
        cell: Cell = Cell(1, 1)
        ship: MockShip = MockShip()
        cell.place_ship(ship)
        self.assertTrue(cell.has_ship())
        self.assertEqual(cell._ship, ship)
        self.assertEqual(cell.get_cell(), 'S')  # Should show ship symbol

    def test_hit_on_ship(self) -> None:
        '''Test hitting on hitting a cell with a ship'''
        cell: Cell = Cell(5, 5)
        ship: MockShip = MockShip()
        cell.place_ship(ship)
        result: bool = cell.hit()
        self.assertTrue(result)
        self.assertEqual(cell.get_cell(), 'H')
        self.assertTrue(ship.hit_called)

    def test_hit_on_water(self) -> None:
        '''Test on hitting a cell with no ship'''
        cell: Cell = Cell(2, 2)
        self.assertFalse(cell.has_ship())
        result: bool = cell.hit()
        self.assertFalse(result)
        self.assertEqual(cell.get_cell(), 'M')

    def test_hit_on_already_hit_ship(self) -> None:
        '''Test hitting a ship twice'''
        cell: Cell = Cell(1, 1)
        ship: MockShip = MockShip()
        cell.place_ship(ship)
        cell.hit()  # first hit
        ship.hit_called = False  # reset to check second hit
        result = cell.hit()
        self.assertFalse(result)
        self.assertFalse(ship.hit_called)
        self.assertEqual(cell.get_cell(), 'H')
