'''
By: McKenzie Swindler
A class using the strategy design pattern that is used for the easy level of the game
'''

import random
from typing import Any, Optional, Tuple
from ai_strategy import AIStrategy


class DumbStrategy(AIStrategy):
    def choose_move(self, ai: Any) -> Optional[Tuple[int, int]]:
        random.shuffle(ai.available_moves)
        for move in ai.available_moves:
            if move not in ai.tried:
                return move
        return None

    def handle_result(self, ai: Any, move: Tuple[int, int], result: str) -> None:
        pass  # Dumb AI doesn't learn or adapt
