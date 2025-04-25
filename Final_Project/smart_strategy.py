from ai_strategy import AIStrategy
from dumb_strategy import DumbStrategy

class TargetedStrategy(AIStrategy):
    def choose_move(self, ai):
        while ai.target_stack:
            move = ai.target_stack.pop()
            if move not in ai.tried:
                return move
        return DumbStrategy().choose_move(ai)

    def handle_result(self, ai, move, result):
        if result in ["Hit!", "AI sank a ship!"]:
            x, y = move
            potential_targets = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for tx, ty in potential_targets:
                if 0 <= tx < 10 and 0 <= ty < 10:
                    if (tx, ty) not in ai.tried and (tx, ty) not in ai.target_stack:
                        ai.target_stack.append((tx, ty))
