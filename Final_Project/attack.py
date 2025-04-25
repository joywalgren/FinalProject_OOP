"""
attack.py"""

# import random
# from cell import Cell
from board import Board

# from cell import Cell


class Ship:
    _color_cycle = [
        '\033[91mS\033[0m',
        '\033[92mS\033[0m',
        '\033[93mS\033[0m',
        '\033[94mS\033[0m',
        '\033[95mS\033[0m']
    _color_index = 0

    def __init__(self, size):
        self.size = size
        self.hits = 0
        self.symbol = Ship._color_cycle[Ship._color_index % len(Ship._color_cycle)]
        Ship._color_index += 1

    def is_hit(self):
        """Registers a hit on the ship"""
        self.hits += 1
        return self.is_sunk()

    def get_size(self) -> int:
        """Returns the size of the ship"""
        return self.size

    def is_sunk(self):
        """Checks if the ship is sunk"""
        return self.hits >= self.size

    def get_symbol(self) -> str:
        return self.symbol



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
                self.result = "Already Attacked"  # In case ship was already hit
                                                    #(redundant guard)
        else:
            cell.hit()  # will mark it as a miss
            self.result = "Miss!"

        return self.result


class Cell:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._cell = "~"  # starts off as water/empty
        self._ship = None  # Reference to a Ship object if present

    def get_cell(self):
        """Returns display character: H = hit, M = miss, S = ship (colored), ~ = water"""
        if self._cell in ['H', 'M', '~']:
            return self._cell
        elif self._ship:
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

    def place_ship(self, ship):
        """Places a ship in the cell"""
        self._ship = ship  # uses loose coupling
        self._cell = ''

    def hit(self) -> bool:
        """Marks the cell as hit and updates the ship if present."""
        # print(f"Attacking cell ({self._x}, {self._y}): Current state = {self._cell}")
        if self._ship and self._cell != 'H':
            self._cell = 'H'
            self._ship.is_hit()
            return True  # yes it hit
        elif self._cell == '~':
            self._cell = 'M'
        return False



class Player:
    def __init__(self, name: str):
        self.name = name
        self.board = Board()
        self.board.place_ships()

    def get_name(self) -> str:
        name = input("Hello! Welcome to our Battleship Game! What is your name? ")
        print("Hello ", name, "! Are you ready to play?")
        return name

class Board:
    """The class that handles displaying and updating the game board"""

    def __init__(self, size=10) -> None:
        """Set up board class"""
        self._board_size = size
        self._board = [[Cell(x, y) for x in range(self._board_size)]
                       for y in range(self._board_size)]
        ship_sizes = [5] #4, 3, 3, 2
        self._ships = [Ship(size) for size in ship_sizes]

    def place_ships(self) -> None:
        """Randomly places ships"""
        for ship in self._ships:
            while True:
                loc_fit = random.randint(0, self._board_size - ship.get_size())
                loc = random.randint(0, self._board_size - 1)
                orient = random.randint(0, 1)
                # print(f"Placing ship of size {ship.get_size()} at ({loc_fit},
                #       {loc}) with orientation {'Horizontal' if orient == 0 else 'Vertical'}")
                if self.ship_space_free(ship.get_size(), orient, loc_fit, loc):
                    if orient == 0:  # Horizontal
                        for i in range(ship.get_size()):
                            # places the ship object in the cell at location loc
                            self._board[loc][loc_fit + i].place_ship(ship)
                    else:  # Vertical
                        for i in range(ship.get_size()):
                            self._board[loc_fit + i][loc].place_ship(ship)
                    break

    def ship_space_free(self, length, orient, loc_fit, loc) -> bool:
        """Checks if the space for the ship is free"""
        if orient == 0:  # Horizontal
            return all(self._board[loc][loc_fit + i].get_cell() == '~' for i in range(length))
        else:  # Vertical
            return all(self._board[loc_fit + i][loc].get_cell() == '~' for i in range(length))

    def attack(self, x: int, y: int) -> bool:
        """Handles an attack on the board returns"""
        return self._board[y][x].hit()

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


        
class DumbOpponent:
    def __init__(self) -> None:
        self.top_board = Board()      # AI's view of player’s board (marks H/M)
        self.bottom_board = Board()   # AI’s own board with ships
        self.bottom_board.place_ships()
        self.available_moves = [(x, y) for x in range(10) for y in range(10)]
        self.target_stack = []
        self.tried = set()



    def choose_move(self):

        # Hunt mode: random untried cell

        random.shuffle(self.available_moves)  # This ensures random order every time

        for move in self.available_moves:
            if move not in self.tried:
                return move

        return None  # No moves left

    def attack_player(self, player_board):
        move = self.choose_move()
        if move is None:
            print("AI has no moves left.")
            return False

        x, y = move
        self.tried.add((x, y))
        self.available_moves.remove((x, y))

        print(f"AI attacks at {chr(x + ord('A'))}{y + 1}")

        attack = Attack(x, y)
        result = attack.execute(player_board)

        print("AI result:", result)

        if result in ["Hit!", "You sank a ship!"]:
            self.top_board._board[y][x].set_cell('H')
            return True
        elif result == "Miss!":
            self.top_board._board[y][x].set_cell('M')
            return False
        else:
            # Already Attacked – should not happen if choose_move avoids it
            return False
        
class Opponent(Dumb_Opponent):

    def choose_move(self):

        while self.target_stack:
            move = self.target_stack.pop()
            if move not in self.tried:
                return move

        # Hunt mode: random untried cell calls base class
        move = super().choose_move()
        return move  # will either be None or a tuple (prob need to fix that)

    def add_adjacent_targets(self, x, y):
        potential_targets = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for tx, ty in potential_targets:
            if 0 <= tx < 10 and 0 <= ty < 10:
                if (tx, ty) not in self.tried and (tx, ty) not in self.target_stack:
                    self.target_stack.append((tx, ty))

    def attack_player(self, player_board):
        # Call the dumb_ai attack_player method
        hit = super().attack_player(player_board)

        # If the attack was a hit, add adjacent targets
        if hit:
            # Get the last move made by the AI
            last_move = list(self.tried)[-1]  # The most recent move added to `self.tried`
            x, y = last_move
            self.add_adjacent_targets(x, y)

        return hit  # will still be the true or false from the base class


class Menu():
    def menu() -> int:
        option = int(input("Battleship\n" \
        "1) Play game\n" \
        "2) See file log \n"))
        return option
    

class Player():
    def __init__(self) -> None:
        name = " "
        self._name = name

    def get_name() -> str:
        name = input("Hello! Welcome to our Battleship Game! What is your name? ")
        print("Hello ", name, "! Are you ready to play?")

    def get_difficulty() -> str:
        diff = input("What difficulty would you like to play on? 'h' for Hard 'e' for Easy\n ")
        return diff
    
from abc import ABC, abstractmethod

class AIStrategy(ABC):
    @abstractmethod
    def choose_move(self, ai) -> tuple:
        pass

    @abstractmethod
    def handle_result(self, ai, move, result) -> None:
        pass

# dumb_strategy.py
import random
from ai_strategy import AIStrategy

class DumbStrategy(AIStrategy):
    def choose_move(self, ai):
        random.shuffle(ai.available_moves)
        for move in ai.available_moves:
            if move not in ai.tried:
                return move
        return None

    def handle_result(self, ai, move, result):
        pass  # Dumb AI doesn't learn or adapt

from ai_strategy import AIStrategy
from dumb_strategy import DumbStrategy

class TargetedStrategy(AIStrategy):
    def choose_move(self, ai):
        while ai.target_stack:
            move = ai.target_stack.pop()
            if move not in ai.tried:
                return move
        return DumbStrategy().choose_move(ai)

    def handle_result(self, ai, move, result):
        if result in ["Hit!", "You sank a ship!"]:
            x, y = move
            potential_targets = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for tx, ty in potential_targets:
                if 0 <= tx < 10 and 0 <= ty < 10:
                    if (tx, ty) not in ai.tried and (tx, ty) not in ai.target_stack:
                        ai.target_stack.append((tx, ty))
