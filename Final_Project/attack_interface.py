"""Attack Interface
Author: Mykaela Moore
Date: 4/28/2025
The class that executes attack and prints out everything happening."""

from abc import ABC, abstractmethod


class AttackStrategy(ABC):
    @abstractmethod
    def execute(self, board) -> str:
        """Perform an attack on the given board and return result string."""
        pass
