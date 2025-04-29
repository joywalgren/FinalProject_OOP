"""Cell
Author: Joy Walgren
Date: 4/16/2025
The class that handles the cells on the board.
Uses loose coupling to talk with ship
"""
from typing import Optional
from ship import Ship


class Cell:
    """Keeps track of each cell on the board"""

    def __init__(self, x: int, y: int):
        """Initializes the cell"""
        self._x = x
        self._y = y
        self._cell = "~"  # Starts off as water/empty
        self._ship: Optional[Ship] = None

    def get_cell(self) -> str:
        """Returns display character: H = hit, M = miss, S = ship (colored), ~ = water"""
        if self._cell in ['H', 'M', '~']:
            return self._cell
        elif self._ship is not None:
            return self._ship.get_symbol()
        else:
            return self._cell

    def set_cell(self, marker: str) -> None:
        """Sets a piece of the board to a value"""
        if marker in ['H', 'M', 'S', '~']:
            self._cell = marker
        else:
            print("Invalid Marker")

    def has_ship(self) -> bool:
        """Checks if the cell contains a ship"""
        return self._ship is not None

    def place_ship(self, ship: Ship) -> None:
        """Places a ship in the cell"""
        self._ship = ship
        self._cell = 'S'

    def hit(self) -> bool:
        """Marks the cell as hit and updates the ship if present."""
        if self._ship is not None and self._cell != 'H':
            self._cell = 'H'
            self._ship.is_hit()
            return True  # yes, it hit
        elif self._cell == '~':
            self._cell = 'M'
        return False
