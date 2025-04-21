from board import Board
from attack import Attack
import random

class Opponent:
    def __init__(self) -> None:
        self.top_board = Board()      # AI's view of player’s board (marks H/M)
        self.bottom_board = Board()   # AI’s own board with ships
        self.available_moves = [(x, y) for x in range(10) for y in range(10)]
        self.last_hits = []
        self.target_queue = []
        self.target_stack = []
        self.tried = set()

    def place_ships(self) -> None:
        self.bottom_board.place_ships()

    # def choose_move(self) -> tuple:
    #     """
    #     Returns a (x, y) tuple representing AI's next move.
    #     """
    #     if self.available_moves:
    #         return self.available_moves.pop()
    #     return None

    def choose_move(self):
        # Target mode: try queued moves near last hit
        while self.target_queue:
            move = self.target_queue.pop(0)
            if move not in self.tried:
                return move

        # Hunt mode: random untried cell
        all_coords = [(x, y) for x in range(10) for y in range(10)]
        random.shuffle(all_coords)  # This ensures random order every time

        for move in all_coords:
            if move not in self.tried:
                return move

        return None  # No moves left
    
    def add_adjacent_targets(self, x, y):
        potential_targets = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for tx, ty in potential_targets:
            if 0 <= tx < 10 and 0 <= ty < 10 and (tx, ty) in self.available_moves:
                self.target_stack.append((tx, ty))
                self.available_moves.remove((tx, ty))
    

    # def attack_player(self, player_board: Board) -> bool:
    #     move = self.choose_move()
    #     if move is None:
    #         print("AI has no moves left.")
    #         return False

    #     x, y = move
    #     print(f"AI attacks at {chr(x + ord('A'))}{y + 1}")

    #     if player_board.attack(x, y):
    #         print("AI hits!")
    #         self.top_board._board[y][x].set_cell('H')
    #         player_board._board[y][x].set_cell('H')
    #         self.last_hits.append((x, y))
    #         self.add_adjacent_targets(x, y)
    #         return True
    #     else:
    #         print("AI misses.")
    #         self.top_board._board[y][x].set_cell('M')
    #         player_board._board[y][x].set_cell('M')
    #         return False
    def attack_player(self, player_board):
        move = self.choose_move()
        if move is None:
            print("AI has no moves left.")
            return False

        x, y = move
        self.tried.add((x, y))

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

