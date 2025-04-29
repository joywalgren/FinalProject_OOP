'''
By: McKenzie Swindler
Tests for ship class
'''

import unittest
from ship import Ship  # adjust if your file is named differently


class TestShip(unittest.TestCase):

    def test_initialization(self) -> None:
        ship = Ship(3)
        self.assertEqual(ship.get_size(), 3)
        self.assertEqual(ship.hits, 0)
        self.assertIn('S', ship.get_symbol())
        self.assertTrue(ship.get_symbol().startswith('\033'))  # colored output

    def test_is_hit_and_is_sunk(self) -> None:
        ship = Ship(2)
        # First hit
        sunk = ship.is_hit()
        self.assertEqual(ship.hits, 1)
        self.assertFalse(sunk)
        self.assertFalse(ship.is_sunk())

        # Second hit - should sink
        sunk = ship.is_hit()
        self.assertEqual(ship.hits, 2)
        self.assertTrue(sunk)
        self.assertTrue(ship.is_sunk())

    def test_large_ship(self) -> None:
        ship = Ship(5)
        for _ in range(4):
            ship.is_hit()
            self.assertFalse(ship.is_sunk())

        ship.is_hit()  # 5th hit
        self.assertTrue(ship.is_sunk())


if __name__ == '__main__':
    unittest.main()
