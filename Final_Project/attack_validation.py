"""Attack Validation
Author: Mykaela Moore
Date: 4/28/2025
The class that handles used to check if cell has been attacked or not."""

from attack_decorator import AttackDecorator
from board import Board  # import your board type



class ValidationAttack(AttackDecorator):
    """Double checks the cell has been attacked already"""

    def execute(self, board: Board) -> str:
        """Checking to see if desired attack position has 
        already been attacked and returning result"""
        wrapped = self._wrapped
        x = getattr(wrapped, 'x', None)
        y = getattr(wrapped, 'y', None)
        if x is None or y is None:
            return super().execute(board)
        cell = board._board[y][x]
        if cell.get_cell() in ('H', 'M'):
            return "Invalid: Repeat Attack"
        return super().execute(board)
