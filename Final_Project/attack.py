"""Attack 
Author: Mykaela Moore
Date: 4/28/2025
Original attack file. Logic is built here."""

from attack_interface import AttackStrategy

class BasicAttack(AttackStrategy):
    """Attack that player and ai will use"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def execute(self, board) -> str:
        """Attack is hit or miss and returns if there was an outcome ie. ship sank"""
        cell = board._board[self.y][self.x]
        current = cell.get_cell()
        if current in ("H", "M"):
            return "Already Attacked"
        
        if cell.has_ship():
            cell.hit()
            ship = cell._ship
            if ship.is_sunk():
                return "Ship Sank!!"
            else:
                return "Hit!"
        else:
                cell.hit()
                return "Miss!"
