# File: validation_attack.py
from attack_decorator import AttackDecorator

class ValidationAttack(AttackDecorator):
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