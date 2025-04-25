'''
The main class for the AI opponent
'''

from board import Board
from attack import Attack

class AIPlayer:
    def __init__(self, strategy):
        self.top_board = Board()
        self.bottom_board = Board()
        self.bottom_board.place_ships()
        self.available_moves = [(x, y) for x in range(10) for y in range(10)]
        self.target_stack = []
        self.tried = set()
        self.strategy = strategy

    def choose_move(self):
        return self.strategy.choose_move(self)

    def attack_player(self, player_board):
        move = self.choose_move()
        if move is None:
            print("AI has no moves left.")
            return False

        x, y = move
        self.tried.add(move)
        if move in self.available_moves:
            self.available_moves.remove(move)

        print(f"AI attacks at {chr(x + ord('A'))}{y + 1}")
        attack = Attack(x, y)
        result = attack.execute(player_board)
        print("AI result:", result)

        # Update the top board
        if result in ["Hit!", "AI sank a ship!"]:
            self.top_board._board[y][x].set_cell('H')
        elif result == "Miss!":
            self.top_board._board[y][x].set_cell('M')

        # Let the strategy react
        self.strategy.handle_result(self, move, result)
        return result in ["Hit!", "AI sank a ship!"]
