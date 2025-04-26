# File: attack_interface.py
from abc import ABC, abstractmethod

class AttackStrategy(ABC):
    @abstractmethod
    def execute(self, board) -> str:
        """Perform an attack on the given board and return result string."""
        pass