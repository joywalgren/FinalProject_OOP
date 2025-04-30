"""Attack Interface
Author: Mykaela Moore
Date: 4/28/2025
The class that executes attack and prints out everything happening."""

from abc import ABC, abstractmethod
from board import Board  # import your board type



class AttackStrategy(ABC):
    """Inheriting abtract base class. Defining an interface, not something 
    you can instantiate directly
    """
    @abstractmethod
    def execute(self, board: Board) -> str:
        """Perform an attack on the given board and return result string."""
        pass
