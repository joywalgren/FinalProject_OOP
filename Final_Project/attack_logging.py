# File: logging_attack.py
from attack_decorator import AttackDecorator

class LoggingAttack(AttackDecorator):
    def execute(self, board) -> str:
        result = super().execute(board)
        x = getattr(self._wrapped, 'x', None)
        y = getattr(self._wrapped, 'y', None)
        coord = f"{chr(x + ord('A'))}{y + 1}" if x is not None and y is not None else "?"
        print(f"[LOG] Attack at {coord} -> {result}")
        return result