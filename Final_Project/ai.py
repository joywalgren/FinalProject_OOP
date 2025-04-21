from battleship import Board

class Opponent:
    def __init__(self) -> None:
        self.top_board = Board()      # AI's view of player’s board (marks H/M)
        self.bottom_board = Board()   # AI’s own board with ships
        self.available_moves = [(x, y) for x in range(10) for y in range(10)]
        self.last_hits = []
        self.target_stack = []

    def place_ships(self) -> None:
        self.bottom_board.place_ships()

    def choose_move(self) -> tuple:
        """
        Returns a (x, y) tuple representing AI's next move.
        """
        if self.available_moves:
            return self.available_moves.pop()
        return None
    
    def add_adjacent_targets(self, x, y):
        potential_targets = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for tx, ty in potential_targets:
            if 0 <= tx < 10 and 0 <= ty < 10 and (tx, ty) in self.available_moves:
                self.target_stack.append((tx, ty))
                self.available_moves.remove((tx, ty))
    
    def attack_player(self, player_board: Board) -> None:
        """
        AI selects a move and attacks the player's board. player_board would be the bottom board
        """
        x, y = self.choose_move()
        if player_board.has_ship(x, y):
            self.top_board.set_cell(x, y, 'H')
            player_board.set_cell(x, y, 'H')
            self.last_hits.append((x, y))
            self.add_adjacent_targets(x, y) 
            #need to figure out how to tell when the ship has sunk and to move on 
        else:
            self.top_board.set_cell(x, y, 'M')
            player_board.set_cell(x, y, 'M')