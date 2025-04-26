# File: attack_decorator.py
from attack_interface import AttackStrategy

class AttackDecorator(AttackStrategy):
    def __init__(self, wrapped: AttackStrategy):
        self._wrapped = wrapped

    def execute(self, board) -> str:
        return self._wrapped.execute(board)