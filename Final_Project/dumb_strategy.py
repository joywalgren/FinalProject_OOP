'''
By: McKenzie Swindler
A class using the strategy design pattern that is used for the easy level of the game.
This strategy simply chooses random moves and does not adapt or learn from previous results.
'''

import random
from typing import Any, Tuple
from ai_strategy import AIStrategy
from opponent import AIPlayer


class DumbStrategy(AIStrategy):

    def choose_move(self, ai: AIPlayer) -> Tuple[int, int]:
        '''Chooses a random move from the available moves that the AI has not yet tried'''
        random.seed(42)
        random.shuffle(ai.available_moves)
        for move in ai.available_moves:
            if move not in ai.tried:
                return move
        return random.choice([(x, y) for x in range(10)
                             for y in range(10) if (x, y) not in ai.tried])

    def handle_result(self, ai: Any, move: Tuple[int, int], result: str) -> None:
        '''A placeholder method'''
        pass  # Dumb AI doesn't learn or adapt
