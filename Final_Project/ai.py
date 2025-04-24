from attack import Attack
from dumb_ai import Dumb_Opponent


class Opponent(Dumb_Opponent):

    def place_ships(self) -> None:
        self.bottom_board.place_ships()


    def choose_move(self):

        while self.target_stack:
            move = self.target_stack.pop()
            if move not in self.tried:
                return move

        # Hunt mode: random untried cell calls base class
        move = super().choose_move()
        return move  # will either be None or a tuple (prob need to fix that)

    def add_adjacent_targets(self, x, y):
        potential_targets = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for tx, ty in potential_targets:
            if 0 <= tx < 10 and 0 <= ty < 10:
                if (tx, ty) not in self.tried and (tx, ty) not in self.target_stack:
                    self.target_stack.append((tx, ty))

    def attack_player(self, player_board):
        # Call the dumb_ai attack_player method
        hit = super().attack_player(player_board)

        # If the attack was a hit, add adjacent targets
        if hit:
            # Get the last move made by the AI
            last_move = list(self.tried)[-1]  # The most recent move added to `self.tried`
            x, y = last_move
            self.add_adjacent_targets(x, y)

        return hit  # will still be the true or false from the base class

