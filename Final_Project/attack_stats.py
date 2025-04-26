# File: stats_attack.py
from attack_decorator import AttackDecorator

class StatsAttack(AttackDecorator):
    hits = 0
    misses = 0
    repeats = 0

    def execute(self, board) -> str:
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
    def report():
        print(f"Stats → Hits: {StatsAttack.hits}, Misses: {StatsAttack.misses}, Repeats: {StatsAttack.repeats}")
