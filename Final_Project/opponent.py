'''
The main class for the AI opponent
'''

from board import Board
# New attack system:
from attack      import BasicAttack
from attack_validation import ValidationAttack
from attack_logging    import LoggingAttack
from attack_stats     import StatsAttack

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

        coord = f"{chr(x + ord('A'))}{y + 1}"
        print(f"AI attacks at {coord}")

        # --- build the decorator chain for this shot ---
        attack = ValidationAttack(
                    StatsAttack(
                      LoggingAttack(
                        BasicAttack(x, y)
                      )
                    )
                 )

        result = attack.execute(player_board)
        print("AI result:", result)

        # --- update AI’s view of your board ---
        mark = 'H' if "Hit" in result or "sank" in result else 'M'
        self.top_board._board[y][x].set_cell(mark)

        # Let the strategy react
        self.strategy.handle_result(self, move, result)
        return result in ["Hit!", "AI sank a ship!"]
