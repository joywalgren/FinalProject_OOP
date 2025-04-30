'''
By: McKenzie Swindler
Tests for attack class
'''

from attack import BasicAttack
import unittest
from typing import Optional


class MockCell:
    '''Mock version of Cell for testing attack behavior'''

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
        '''Return the current symbol in the cell'''
        return self._cell

    def has_ship(self) -> bool:
        '''Return whether the cell contains a ship'''
        return self._has_ship

    def hit(self) -> bool:
        '''Simulate hitting the cell and update its state'''
        if self._has_ship:
            self._cell = "H"
            if self._ship:
                self._ship.is_hit()
            return True
        else:
            self._cell = "M"
            return False


class MockShip:
    '''Mock version of a Ship'''

    def __init__(self, sunk: bool = False) -> None:
        self._sunk: bool = sunk
        self.hit_called: bool = False

    def is_hit(self) -> None:
        '''Record that the ship was hit'''
        self.hit_called = True

    def is_sunk(self):
        '''Return whether the ship has sunk'''
        return self._sunk


class MockBoard:
    '''Mock version of Board that only has one cell'''

    def __init__(self, cell) -> None:
        self._board: list[list[MockCell]] = [[cell]]


class TestAttack(unittest.TestCase):
    '''Unit tests for a BasicAttack class'''

    def test_attack_miss(self) -> None:
        '''Test an attack on a cell with no ship '''
        cell = MockCell(has_ship=False)
        board = MockBoard(cell)
        attack = BasicAttack(0, 0)
        result: str = attack.execute(board)
        self.assertEqual(result, "Miss!")
        self.assertEqual(cell.get_cell(), "M")

    def test_attack_hit_not_sunk(self) -> None:
        '''Test an attack that hits a ship but does not sink it'''
        ship = MockShip(sunk=False)
        cell = MockCell(has_ship=True, ship=ship)
        board = MockBoard(cell)
        attack = BasicAttack(0, 0)
        result: str = attack.execute(board)
        self.assertEqual(result, "Hit!")
        self.assertTrue(ship.hit_called)
        self.assertEqual(cell.get_cell(), "H")

    def test_attack_hit_sunk(self) -> None:
        '''Test an attack that hits and sinks a ship'''
        ship = MockShip(sunk=True)
        cell = MockCell(has_ship=True, ship=ship)
        board = MockBoard(cell)
        attack = BasicAttack(0, 0)
        result: str = attack.execute(board)
        self.assertEqual(result, "Ship Sank!!")
        self.assertTrue(ship.hit_called)
        self.assertEqual(cell.get_cell(), "H")

    def test_attack_already_attacked(self) -> None:
        '''Test an attack on a cell that was alrady attacked'''
        cell = MockCell(has_ship=False, already_attacked=True)
        board = MockBoard(cell)
        attack = BasicAttack(0, 0)
        result: str = attack.execute(board)
        self.assertEqual(result, "Already Attacked")


if __name__ == '__main__':
    unittest.main()
