'''
By: McKenzie Swindler
A class using the strategy design pattern that is used for the hard level of the game
'''

from typing import Any, Tuple, Optional
from ai_strategy import AIStrategy
from dumb_strategy import DumbStrategy


class TargetedStrategy(AIStrategy):
    def choose_move(self, ai: Any) -> Optional[Tuple[int, int]]:
        while ai.target_stack:
            move: Tuple[int, int] = ai.target_stack.pop()
            if move not in ai.tried:
                return move
        return DumbStrategy().choose_move(ai)

    def handle_result(self, ai: Any, move: Tuple[int, int], result: str) -> None:
        if result in ["Hit!", "AI sank a ship!"]:
            x, y = move
            potential_targets = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for tx, ty in potential_targets:
                if 0 <= tx < 10 and 0 <= ty < 10:
                    if (tx, ty) not in ai.tried and (tx, ty) not in ai.target_stack:
                        ai.target_stack.append((tx, ty))
