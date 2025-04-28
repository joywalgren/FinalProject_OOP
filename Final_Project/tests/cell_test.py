'''
By: McKenzie Swindler
Tests for cell class
'''

import unittest

# Minimal mock Ship class for testing
class MockShip:
    def __init__(self):
        self.hit_called = False

    def is_hit(self):
        self.hit_called = True

    def get_symbol(self):
        return 'S'

from cell import Cell  # adjust if your file is named differently

class TestCell(unittest.TestCase):

    def test_cell_initialization(self):
        cell = Cell(2, 3)
        self.assertEqual(cell._x, 2)
        self.assertEqual(cell._y, 3)
        self.assertEqual(cell.get_cell(), "~")
        self.assertFalse(cell.has_ship())

    def test_set_cell_valid_markers(self):
        cell = Cell(0, 0)
        for marker in ['H', 'M', 'S', '~']:
            cell.set_cell(marker)
            self.assertEqual(cell.get_cell(), marker)

    def test_set_cell_invalid_marker(self):
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        cell = Cell(0, 0)
        cell.set_cell('X')
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertIn("Invalid Marker", captured_output.getvalue())

    def test_place_ship(self):
        cell = Cell(1, 1)
        ship = MockShip()
        cell.place_ship(ship)
        self.assertTrue(cell.has_ship())
        self.assertEqual(cell._ship, ship)
        self.assertEqual(cell.get_cell(), 'S')  # Should show ship symbol

    def test_hit_on_ship(self):
        cell = Cell(5, 5)
        ship = MockShip()
        cell.place_ship(ship)
        result = cell.hit()
        self.assertTrue(result)
        self.assertEqual(cell.get_cell(), 'H')
        self.assertTrue(ship.hit_called)

    def test_hit_on_water(self):
        cell = Cell(2, 2)
        self.assertFalse(cell.has_ship())
        result = cell.hit()
        self.assertFalse(result)
        self.assertEqual(cell.get_cell(), 'M')

    def test_hit_on_already_hit_ship(self):
        cell = Cell(1, 1)
        ship = MockShip()
        cell.place_ship(ship)
        cell.hit()  # first hit
        ship.hit_called = False  # reset to check second hit
        result = cell.hit()
        self.assertFalse(result)
        self.assertFalse(ship.hit_called)
        self.assertEqual(cell.get_cell(), 'H')

if __name__ == '__main__':
    unittest.main()
