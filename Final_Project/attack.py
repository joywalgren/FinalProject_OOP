# File: basic_attack.py
from attack_interface import AttackStrategy

class BasicAttack(AttackStrategy):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def execute(self, board) -> str:
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

"""
attack.py

# import random
# from cell import Cell
from board import Board

# from cell import Cell

class Attack:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.result = None

    def execute(self, board) -> str:
        cell = board._board[self.y][self.x]

        current = cell.get_cell()
        if current in ("H", "M"):
            self.result = "Already Attacked"
            return self.result

        if cell.has_ship():
            hit_result = cell.hit()  # this handles updating the cell and ship
            if hit_result:
                ship = cell._ship  # ship reference is stored in cell
                self.result = "You sank a ship!" if ship.is_sunk() else "Hit!"
            else:
                self.result = "Already Attacked"  # In case ship was already hit
                                                    #(redundant guard)
        else:
            cell.hit()  # will mark it as a miss
            self.result = "Miss!"

        return self.result
    """