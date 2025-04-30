"""Attack Decorator
Author: Mykaela Moore
Date: 4/28/2025
The class that used to decorate original attack class
"""

from attack_interface import AttackStrategy
from board import Board  # import your board type



class AttackDecorator(AttackStrategy):
    """subclassing attackStrategy
    """
    def __init__(self, wrapped: AttackStrategy) -> None:
        """Referencing to original function
        """
        self._wrapped = wrapped

    def execute(self, board: Board) -> str:
        """Runs attacks
        """
        return self._wrapped.execute(board)
