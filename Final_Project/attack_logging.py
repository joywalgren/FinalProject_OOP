"""Attack Logging
Author: Mykaela Moore
Date: 4/28/2025
The class that handles used to handle record of attacks."""

from attack_decorator import AttackDecorator
"""This is what keeps track of where players are attacking. Prints out the action of the turn."""


class LoggingAttack(AttackDecorator):
    def execute(self, board) -> str:
        result = super().execute(board)
        x = getattr(self._wrapped, 'x', None)
        y = getattr(self._wrapped, 'y', None)
        coord = f"{chr(x + ord('A'))}{y + 1}" if x is not None and y is not None else "?"
        print(f"[LOG] Attack at {coord} -> {result}")
        return result
