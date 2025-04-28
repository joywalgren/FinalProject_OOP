"""Attack Validation
Author: Mykaela Moore
Date: 4/28/2025
The class that handles used to check if cell has been attacked or not."""

from attack_decorator import AttackDecorator

class ValidationAttack(AttackDecorator):
    """Double checks the cell has been attacked already"""
    def execute(self, board) -> str:
        wrapped = self._wrapped
        x = getattr(wrapped, 'x', None)
        y = getattr(wrapped, 'y', None)
        if x is None or y is None:
            return super().execute(board)
        cell = board._board[y][x]
        if cell.get_cell() in ('H', 'M'):
            return "Invalid: Repeat Attack"
        return super().execute(board)