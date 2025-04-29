'''
By: McKenzie Swindler
Tests for attack class
'''

from attack import BasicAttack
import unittest
from typing import Optional


class MockCell:
    def __init__(
            self,
            has_ship: bool = False,
            already_attacked: bool = False,
            ship: Optional["MockShip"] = None) -> None:
        self._has_ship: bool = has_ship
        self._hit_called: bool = False
        self._cell: str = "H" if already_attacked else "~"
        self._ship: Optional["MockShip"] = ship

    def get_cell(self) -> str:
        return self._cell

    def has_ship(self) -> bool:
        return self._has_ship

    def hit(self) -> bool:
        if self._has_ship:
            self._cell = "H"
            if self._ship:
                self._ship.is_hit()
            return True
        else:
            self._cell = "M"
            return False


class MockShip:
    def __init__(self, sunk: bool = False) -> None:
        self._sunk: bool = sunk
        self.hit_called: bool = False

    def is_hit(self) -> None:
        self.hit_called = True

    def is_sunk(self):
        return self._sunk


class MockBoard:
    def __init__(self, cell) -> None:
        self._board: list[list[MockCell]] = [[cell]]


class TestAttack(unittest.TestCase):

    def test_attack_miss(self) -> None:
        cell = MockCell(has_ship=False)
        board = MockBoard(cell)
        attack = BasicAttack(0, 0)
        result: str = attack.execute(board)
        self.assertEqual(result, "Miss!")
        self.assertEqual(cell.get_cell(), "M")

    def test_attack_hit_not_sunk(self) -> None:
        ship = MockShip(sunk=False)
        cell = MockCell(has_ship=True, ship=ship)
        board = MockBoard(cell)
        attack = BasicAttack(0, 0)
        result: str = attack.execute(board)
        self.assertEqual(result, "Hit!")
        self.assertTrue(ship.hit_called)
        self.assertEqual(cell.get_cell(), "H")

    def test_attack_hit_sunk(self) -> None:
        ship = MockShip(sunk=True)
        cell = MockCell(has_ship=True, ship=ship)
        board = MockBoard(cell)
        attack = BasicAttack(0, 0)
        result: str = attack.execute(board)
        self.assertEqual(result, "Ship Sank!!")
        self.assertTrue(ship.hit_called)
        self.assertEqual(cell.get_cell(), "H")

    def test_attack_already_attacked(self) -> None:
        cell = MockCell(has_ship=False, already_attacked=True)
        board = MockBoard(cell)
        attack = BasicAttack(0, 0)
        result: str = attack.execute(board)
        self.assertEqual(result, "Already Attacked")


if __name__ == '__main__':
    unittest.main()
