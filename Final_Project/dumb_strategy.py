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