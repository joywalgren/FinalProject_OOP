from abc import ABC, abstractmethod

class AIStrategy(ABC):
    @abstractmethod
    def choose_move(self, ai) -> tuple:
        pass

    @abstractmethod
    def handle_result(self, ai, move, result) -> None:
        pass
