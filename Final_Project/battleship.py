import random


class Board(object):
    def __init__(self) -> None:
        """set up board class"""
        board = [['~' for _ in range(10)] for _ in range(10)]
        ship_sizes = [5, 4, 3, 3, 2]
        self._board = board
        self._ship_sizes = ship_sizes

    def place_ships(self) -> None:
        for ships in self._ship_sizes:
            while True:
                loc_fit = random.randint(0, 9-ships+1)
                loc = random.randint(0, 9)
                orient = random.randint(0, 1)
                if self.ship_space_free(ships, orient, loc_fit, loc) is True:
                    break
            if orient == 0:  # ship is Horizontal
                for i in range(ships):
                    self._board[loc][loc_fit+i] = str(i)
            if orient == 1:  # ship is Vertical
                for i in range(ships):
                    self._board[loc_fit+i][loc] = str(i)

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

    def print_board(self) -> None:
        print("    A B C D E F G H I J")
        print("   ---------------------")
        for i, row in enumerate(self._board, start=1):
            print(f"{i:2}| {' '.join(row)} |")
        print("   ---------------------")


def attack(tboard: Board, enemy_board: Board, x, y):
    actionComplete: bool = False
    while actionComplete is False:
        if tboard.get_cell(x, y) == '~':
            if enemy_board.has_ship(x, y):
                tboard.set_cell(x, y, 'H')
                enemy_board.set_cell(x, y, 'H')
            else:
                tboard.set_cell(x, y, 'M')
            actionComplete = True
        else:
            print("invalid action")


def read_input() -> tuple:
    """
    reads the input from the user
    """
    x, y = input("Enter a letter then a number seperated by a space then press Enter\n").split()
    x = ord(x.upper()) - ord('A')
    y = int(y) - 1
    return x, y


top_board = Board()
bottom_board = Board()
ai_top_board = Board()
ai_bottom_board = Board()
bottom_board.place_ships()
top_board.print_board()
bottom_board.print_board()
user_input = read_input()
attack(top_board, bottom_board, user_input[1], user_input[0])

# while True:
#     attack(top_board, bottom_board, user_input[0], user_input[1])
top_board.print_board()
bottom_board.print_board()
