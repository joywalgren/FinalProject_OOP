'''
By: McKenzie Swindler
Base class for strategy design pattern for the opponent
'''

from abc import ABC, abstractmethod
from typing import Tuple, Any


class AIStrategy(ABC):
    @abstractmethod
    def choose_move(self, ai: Any) -> Tuple[int, int]:
        """Select a move for the AI player."""
        pass

    @abstractmethod
    def handle_result(self, ai: Any, move: Tuple[int, int], result: str) -> None:
        """Process the result of a move (e.g., hit, miss, sunk)."""
        pass
