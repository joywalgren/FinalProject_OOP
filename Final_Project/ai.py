from board import Board
from attack import Attack
import random


class Opponent:
    def __init__(self) -> None:
        self.top_board = Board()      # AI's view of player’s board (marks H/M)
        self.bottom_board = Board()   # AI’s own board with ships
        self.bottom_board.place_ships()
        self.available_moves = [(x, y) for x in range(10) for y in range(10)]
        self.target_stack = []
        self.tried = set()

    def choose_move(self):

        while self.target_stack:
            move = self.target_stack.pop()
            if move not in self.tried:
                return move

        # Hunt mode: random untried cell
    
        random.shuffle(self.available_moves)  # This ensures random order every time

        for move in self.available_moves:
            if move not in self.tried:
                return move

        return None  # No moves left
    
    def add_adjacent_targets(self, x, y):
        potential_targets = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for tx, ty in potential_targets:
            if 0 <= tx < 10 and 0 <= ty < 10:
                if (tx, ty) not in self.tried and (tx, ty) not in self.target_stack:
                    self.target_stack.append((tx, ty))
    

    
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
            self.add_adjacent_targets(x, y)
            return True
        elif result == "Miss!":
            self.top_board._board[y][x].set_cell('M')
            return False
        else:
            # Already Attacked – should not happen if choose_move avoids it
            return False

