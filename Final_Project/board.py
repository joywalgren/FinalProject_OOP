"""Board
Primary Author: Joy Walgren
Date: 4/16/2025
The class that handles the boards.
Uses ship and cell
"""


import random
from cell import Cell
from ship import Ship


class Board:
    """The class that handles displaying and updating the game board"""

    def __init__(self, size: int = 10) -> None:
        """Set up board class"""
        self._board_size = size
        self._board = [[Cell(x, y) for x in range(self._board_size)]
                       for y in range(self._board_size)]
        ship_sizes = [5, 4, 3]  # 5, 4, 3, 3, 2
        self._ships = [Ship(size) for size in ship_sizes]
        self.clean_board()

    def place_ships(self) -> None:
        """Randomly places ships"""
        for ship in self._ships:
            while True:
                loc_fit = random.randint(0, self._board_size - ship.get_size())
                loc = random.randint(0, self._board_size - 1)
                orient = random.randint(0, 1)
                if self.ship_space_free(ship.get_size(), orient, loc_fit, loc):
                    if orient == 0:  # Horizontal
                        for i in range(ship.get_size()):
                            self._board[loc][loc_fit + i].place_ship(ship)
                    else:  # Vertical
                        for i in range(ship.get_size()):
                            self._board[loc_fit + i][loc].place_ship(ship)
                    break

    def ship_space_free(self, length: int, orient: int, loc_fit: int, loc: int) -> bool:
        """Checks if the space for the ship is free"""
        if orient == 0:  # Horizontal
            return all(self._board[loc][loc_fit + i].get_cell() == '~' for i in range(length))
        else:  # Vertical
            return all(self._board[loc_fit + i][loc].get_cell() == '~' for i in range(length))

    def attack(self, x: int, y: int) -> bool:
        """Handles an attack on the board.
        Returns True if hit, False if miss.
        Raises ValueError if already attacked."""
        cell = self._board[y][x]
        if cell.get_cell() in ['H', 'M']:
            raise ValueError("This square has already been attacked! Try again.")
        return cell.hit()

    def print_board(self) -> None:
        """Prints the board"""
        print("    A B C D E F G H I J")
        print("   ---------------------")
        for i, row in enumerate(self._board, start=1):
            print(f"{i:2}| {' '.join(cell.get_cell() for cell in row)} |")
        print("   ---------------------")

    def check_endgame(self) -> bool:
        """If checks if all ships are sunk returns true if game is done"""
        for ship in self._ships:
            if not ship.is_sunk():
                return False
        return True

    def clean_board(self) -> None:
        """Cleans the boards of attacks and ships for a new state"""
        self._board = [
            [Cell(x, y) for x in range(self._board_size)]
            for y in range(self._board_size)
        ]
