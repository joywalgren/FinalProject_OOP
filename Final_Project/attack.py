"""
attack.py"""

import random

class Ship:
    def __init__(self, size: int, coordinates: list[tuple[int,int]]):
        self.size = size
        self.coordinates = coordinates
        self.hits = 0
        self.hit_positions: list[tuple[int,int]] = []

    def is_hit(self, x: int, y: int) -> bool:
        if (x, y) in self.coordinates and (x, y) not in self.hit_positions:
            self.hits += 1
            self.hit_positions.append((x, y))
            return True
        return False

    def is_sunk(self) -> bool:
        return self.hits >= self.size

# attack.py

class Attack:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.result = None

    def execute(self, board) -> str:
        # 1) Is there a ship at (x,y)?
        if (self.x, self.y) in board._ship_positions:
            ship = board._ship_positions[(self.x, self.y)]
            board.set_cell(self.x, self.y, "X")

            # 2) Tell the ship it was hit *at* (x,y)
            was_hit = ship.is_hit(self.x, self.y)
            
            # 3) Based on whether it sank or just hit:
            if was_hit:
                self.result = "You sank a ship!" if ship.is_sunk() else "Hit!"
            else:
                # (optional) if you want to catch repeat-hits here:
                self.result = "Already Attacked"
        
        # 4) Already attacked this spot?
        elif board.get_cell(self.x, self.y) in ("X", "O"):
            self.result = "Already Attacked"
        
        # 5) Miss
        else:
            board.set_cell(self.x, self.y, "O")
            self.result = "Miss!"
        
        return self.result
  

    
class Player:
    def __init__(self, name: str):
        self.name = name
        self.board = Board()
        self.board.place_ships()

    def get_name(self)-> str:
        name = input("Hello! Welcome to our Battleship Game! What is your name? ")
        print("Hello ",name,"! Are you ready to play?")
        return name

class Board(object):
    def __init__(self) -> None:
        """set up board class"""
        self._ships = []  # list to hold actual Ship instances
        self._ship_positions: dict[tuple[int,int], Ship] = {}
        board = [['~' for _ in range(10)] for _ in range(10)]
        ship_sizes = [2]
        self._board = board
        self._ship_sizes = ship_sizes

    def place_ships(self) -> None:
        coordinates = []
        for ship_size in self._ship_sizes:
            while True:
                loc_fit = random.randint(0, 9 - ship_size + 1)
                loc = random.randint(0, 9)
                orient = random.randint(0, 1)
                if self.ship_space_free(ship_size, orient, loc_fit, loc):
                    break

            coords = []
            if orient == 0:  # Horizontal
                coords = [(loc, loc_fit + i) for i in range(ship_size)]
            else:  # Vertical
                coords = [(loc_fit + i, loc) for i in range(ship_size)]

            ship = Ship(ship_size, coords)
            self._ships.append(ship)

            for x, y in coords:
                self._board[x][y] = "~"  # still looks empty, or use str(ship_size) for testing
                self._ship_positions[(x, y)] = ship

    def ship_space_free(self, length, orient, loc_fit, loc) -> bool:
        is_free: bool = True
        if orient == 0:
            for i in range(length):
                is_free = (self._board[loc][loc_fit+i]) == '~'
                if is_free is False:
                    break
            return is_free
        if orient == 1:
            for i in range(length):
                is_free = (self._board[loc_fit+i][loc]) == '~'
                if is_free is False:
                    break
            return is_free
        
    @property
    def board(self) -> list:
        """
        returns the board
        """
        return self._board
    
    def get_cell(self, x: int, y: int) -> str:
        """
        returns what's in the cell
        """
        return self._board[x][y]
 
    def set_cell(self, x: int, y: int, marker: str) -> None:
        """
        sets a piece of the board to a value
        """
        self._board[x][y] = marker

    def has_ship(self, x: int, y: int) -> bool:
        return self._board[x][y].isdigit()

    def print_board(self, show_ships: bool = False) -> None:
        print("    A B C D E F G H I J")
        print("   ---------------------")
        for i, row in enumerate(self._board):
            display_row = []
            for j, cell in enumerate(row):
                if show_ships and (i, j) in self._ship_positions:
                    display_row.append("S")
                else:
                    display_row.append(cell)
            # Row numbers are 1–10
            print(f"{i+1:2}| {' '.join(display_row)} |")
        print("   ---------------------")

    def all_ships_sunk(self) -> bool:
        """
        Returns True when every Ship in self._ships reports is_sunk().
        """
        return all(ship.is_sunk() for ship in self._ships)

class IsWon:
    """
    Encapsulates the win condition: all ships on a board have been sunk.
    """

    def __init__(self, board) -> None:
        self._board = board

    def check(self) -> bool:
        """
        Returns True if every Ship on the board reports is_sunk().
        """
        return self._board.all_ships_sunk()
