"""Attack Stats
Author: Mykaela Moore
Date: 4/28/2025
The class that handles used to handle outcomes of guess ie. hit, miss, repeat."""

from attack_decorator import AttackDecorator
from board import Board  # import your board type


class StatsAttack(AttackDecorator):
    """Keeps track of your hits, misses, and repeats over the whole program"""
    hits = 0
    misses = 0
    repeats = 0

    def execute(self, board: Board) -> str:
        """Counters"""
        result = super().execute(board)
        if "Hit" in result and "sank" not in result:
            StatsAttack.hits += 1
        elif "sank" in result:
            StatsAttack.hits += 1
        elif "Miss" in result:
            StatsAttack.misses += 1
        elif "Already" in result or "Invalid" in result:
            StatsAttack.repeats += 1
        return result

    @staticmethod
    def report() -> None:
        """Print the stats"""
        print(
            f"Stats → Hits: {StatsAttack.hits}, "
            f"Misses: {StatsAttack.misses}, "
            f"Repeats: {StatsAttack.repeats}"
        )
