"""Attack Decorator
Author: Mykaela Moore
Date: 4/28/2025
The class that used to decorate original attack class
"""

from attack_interface import AttackStrategy


class AttackDecorator(AttackStrategy):
    def __init__(self, wrapped: AttackStrategy):
        self._wrapped = wrapped

    def execute(self, board) -> str:
        return self._wrapped.execute(board)
