'''
By: McKenzie Swindler
Tests for attack class
'''

import unittest

# Minimal mock classes for testing
class MockCell:
    def __init__(self, has_ship=False, already_attacked=False, ship=None):
        self._has_ship = has_ship
        self._hit_called = False
        self._cell = "H" if already_attacked else "~"
        self._ship = ship

    def get_cell(self):
        return self._cell

    def has_ship(self):
        return self._has_ship

    def hit(self):
        if self._has_ship:
            self._cell = "H"
            if self._ship:
                self._ship.is_hit()
            return True
        else:
            self._cell = "M"
            return False

class MockShip:
    def __init__(self, sunk=False):
        self._sunk = sunk
        self.hit_called = False

    def is_hit(self):
        self.hit_called = True

    def is_sunk(self):
        return self._sunk

class MockBoard:
    def __init__(self, cell):
        self._board = [[cell]]  # 1x1 board for simplicity

from attack import Attack  # assuming your class is in attack.py

class TestAttack(unittest.TestCase):

    def test_attack_miss(self):
        cell = MockCell(has_ship=False)
        board = MockBoard(cell)
        attack = Attack(0, 0)
        result = attack.execute(board)
        self.assertEqual(result, "Miss!")
        self.assertEqual(cell.get_cell(), "M")

    def test_attack_hit_not_sunk(self):
        ship = MockShip(sunk=False)
        cell = MockCell(has_ship=True, ship=ship)
        board = MockBoard(cell)
        attack = Attack(0, 0)
        result = attack.execute(board)
        self.assertEqual(result, "Hit!")
        self.assertTrue(ship.hit_called)
        self.assertEqual(cell.get_cell(), "H")

    def test_attack_hit_sunk(self):
        ship = MockShip(sunk=True)
        cell = MockCell(has_ship=True, ship=ship)
        board = MockBoard(cell)
        attack = Attack(0, 0)
        result = attack.execute(board)
        self.assertEqual(result, "You sank a ship!")
        self.assertTrue(ship.hit_called)
        self.assertEqual(cell.get_cell(), "H")

    def test_attack_already_attacked(self):
        cell = MockCell(has_ship=False, already_attacked=True)
        board = MockBoard(cell)
        attack = Attack(0, 0)
        result = attack.execute(board)
        self.assertEqual(result, "Already Attacked")

if __name__ == '__main__':
    unittest.main()
