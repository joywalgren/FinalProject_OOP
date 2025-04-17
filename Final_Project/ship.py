# from cell import Cell


class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0

    def is_hit(self):
        """Registers a hit on the ship"""
        self.hits += 1
        return self.is_sunk()

    def get_size(self) -> int:
        """Returns the size of the ship"""
        return self.size

    def is_sunk(self):
        """Checks if the ship is sunk"""
        return self.hits >= self.size