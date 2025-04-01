import random

#make a board class to store boards in
top_board = [['~' for _ in range(10)] for _ in range(10)]
bottom_board = [['~' for _ in range(10)] for _ in range(10)]
ai_board = [['~' for _ in range(10)] for _ in range(10)]
ship_sizes = [2,3,3,4,5]


class Board(object):
    def __init__(self) -> None:
        """set up board class"""
        board: tuple[str][str] = [['~' for _ in range(10)] for _ in range(10)]
        self.place_ships(board)
        self.print_board(board)

    def place_ships(self, board) -> None:
        for ships in ship_sizes:
            loc_fit = random.randint(0, 9) - ships
            loc = random.randint(0, 9)
            orient = random.randint(0, 1)  # 0 is horz 1 is vert
            if orient == 0:
                for i in range(ships):
                    board[loc][loc_fit+i] = str(i)
            if orient == 1:
                for i in range(ships):
                    board[loc_fit+i][loc] = str(i)

    def print_board(self, board) -> None:
        print("    A B C D E F G H I J")
        print("   ---------------------")
        for i, row in enumerate(board, start=0):
            print(f"{i:2}| {' '.join(row)} |")
        print("   ---------------------")


test_board = Board
test_board.print_board()
