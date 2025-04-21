"""
attack.py"""

import random
from cell import Cell
from board import Board

# class Ship:
#     def __init__(self, size: int, coordinates: list[tuple[int,int]]):
#         self.size = size
#         self.coordinates = coordinates
#         self.hits = 0
#         self.hit_positions: list[tuple[int,int]] = []

#     def is_hit(self, x: int, y: int) -> bool:
#         if (x, y) in self.coordinates and (x, y) not in self.hit_positions:
#             self.hits += 1
#             self.hit_positions.append((x, y))
#             return True
#         return False

#     def is_sunk(self) -> bool:
#         return self.hits >= self.size

# attack.py

class Attack:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.result = None

    def execute(self, board) -> str:
        cell = board._board[self.y][self.x]

        current = cell.get_cell()
        if current in ("H", "M"):
            self.result = "Already Attacked"
            return self.result

        if cell.has_ship():
            hit_result = cell.hit()  # this handles updating the cell and ship
            if hit_result:
                ship = cell._ship  # ship reference is stored in cell
                self.result = "You sank a ship!" if ship.is_sunk() else "Hit!"
            else:
                self.result = "Already Attacked"  # In case ship was already hit (redundant guard)
        else:
            cell.hit()  # will mark it as a miss
            self.result = "Miss!"

        return self.result


# class Attack:
#     def __init__(self, x: int, y: int) -> None:
#         self.x = x
#         self.y = y
#         self.result = None

#     def execute(self, board) -> str:
#         # 1) Is there a ship at (x,y)?
#         if (self.x, self.y) in board._ship_positions:
#             ship = board._ship_positions[(self.x, self.y)]
#             board.set_cell(self.x, self.y, "H")

#             # 2) Tell the ship it was hit *at* (x,y)
#             was_hit = ship.is_hit(self.x, self.y)
            
#             # 3) Based on whether it sank or just hit:
#             if was_hit:
#                 self.result = "You sank a ship!" if ship.is_sunk() else "Hit!"
#             else:
#                 # (optional) if you want to catch repeat-hits here:
#                 self.result = "Already Attacked"
        
#         # 4) Already attacked this spot?
#         elif board.get_cell(self.x, self.y) in ("X", "O"):
#             self.result = "Already Attacked"
        
#         # 5) Miss
#         else:
#             board.set_cell(self.x, self.y, "M")
#             self.result = "Miss!"
        
#         return self.result
  

    
class Player:
    def __init__(self, name: str):
        self.name = name
        self.board = Board()
        self.board.place_ships()

    def get_name(self)-> str:
        name = input("Hello! Welcome to our Battleship Game! What is your name? ")
        print("Hello ",name,"! Are you ready to play?")
        return name

# class Board(object):
#     def __init__(self, size=10) -> None:
#         """set up board class"""
#         self._board_size = size
#         ship_sizes = [5, 4, 3, 3, 2]
#         #self._ships = []  # list to hold actual Ship instances
#         self._ships = []
#         self._ship_positions: dict[tuple[int,int], Ship] = {}
#         #board = [['~' for _ in range(10)] for _ in range(10)]
#         #self._board = board
#         self._board = [[Cell(x, y) for x in range(self._board_size)] for y in range(self._board_size)]

#         self._ship_sizes = ship_sizes

#     def place_ships(self) -> None:
#         for ship_size in self._ship_sizes:
#             while True:
#                 loc_fit = random.randint(0, 9 - ship_size + 1)
#                 loc = random.randint(0, 9)
#                 orient = random.randint(0, 1)
#                 if self.ship_space_free(ship_size, orient, loc_fit, loc):
#                     break

#             coords = []
#             if orient == 0:  # Horizontal
#                 coords = [(loc, loc_fit + i) for i in range(ship_size)]
#             else:  # Vertical
#                 coords = [(loc_fit + i, loc) for i in range(ship_size)]

#             ship = Ship(ship_size, coords)
#             self._ships.append(ship)

#             for x, y in coords:
#                 self._board[x][y].place_ship(ship)  # still looks empty, or use str(ship_size) for testing
#                 self._ship_positions[(x, y)] = ship

#     def ship_space_free(self, length, orient, loc_fit, loc) -> bool:
#         """Checks if the space for the ship is free"""
#         if orient == 0:  # Horizontal
#             return all(self._board[loc][loc_fit + i].get_cell() == '~' for i in range(length))
#         else:  # Vertical
#             return all(self._board[loc_fit + i][loc].get_cell() == '~' for i in range(length))
        
#     @property
#     def board(self) -> list:
#         """
#         returns the board
#         """
#         return self._board

#     def has_ship(self, x: int, y: int) -> bool:
#         return self._board[x][y].isdigit()
    
#     def get_cell(self, x: int, y: int) -> str:
#     # returns "~", "S", "H", or "M"
#         return self._board[x][y].get_cell()

#     def set_cell(self, x: int, y: int, marker: str) -> None:
#         # delegates to Cell.set_cell(...)
#         self._board[x][y].set_cell(marker)

#     def print_board(self, show_ships: bool = False) -> None:
#         print("    A B C D E F G H I J")
#         print("   ---------------------")
#         for i, row in enumerate(self._board):
#             display_row: list[str] = []
#             for j, cell in enumerate(row):
#                 if (i, j) in self._ship_positions:
#                     # if there's a ship here...
#                     if show_ships:
#                         display_row.append("S")
#                     else:
#                         display_row.append("~")
#                 else:
#                     display_row.append(cell.get_cell())
#             print(f"{i+1:2} | {' '.join(display_row)} |")
#         print("   ---------------------")

#     def all_ships_sunk(self) -> bool:
#         """
#         Returns True when every Ship in self._ships reports is_sunk().
#         """
#         return all(ship.is_sunk() for ship in self._ships)

# class IsWon:
#     """
#     Encapsulates the win condition: all ships on a board have been sunk.
#     """

#     def __init__(self, board) -> None:
#         self._board = board

#     def check(self) -> bool:
#         """
#         Returns True if every Ship on the board reports is_sunk().
#         """
#         return self._board.all_ships_sunk()
    
# class Cell:
#     def __init__(self, x: int, y: int):
#         self._x = x
#         self._y = y
#         self._cell = "~"  # starts off as water/empty
#         self._ship = None  # Reference to a Ship object if present

#     def get_cell(self):
#         """Returns H = hit, M = miss, S = ship, ~ = water"""
#         return self._cell

#     def set_cell(self, marker: str) -> None:
#         """Sets a piece of the board to a value"""
#         if marker in ['H', 'M', 'S', '~']:
#             self._cell = marker
#         else:
#             print("Invalid Marker")

#     def has_ship(self) -> bool:
#         """Checks if the cell contains a ship"""
#         return self._ship is not None

#     def place_ship(self, ship):
#         """Places a ship in the cell"""
#         self._ship = ship  # uses loose coupling
#         self._cell = 'S'

#     def hit(self) -> bool:
#         """Marks the cell as hit and updates the ship if present."""
#         # print(f"Attacking cell ({self._x}, {self._y}): Current state = {self._cell}")
#         if self._cell == 'S':
#             self._cell = 'H'
#             self._ship.is_hit()
#             return True  # yes it hit
#         elif self._cell == '~':
#             self._cell = 'M'
#         return False

