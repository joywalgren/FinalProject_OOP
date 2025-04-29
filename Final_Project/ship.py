"""Attack
Author: Mykaela Moore
Date: 4/28/2025
Ship logic and attributes. """


class Ship:
    """The designs of the ship"""
    _color_cycle = [
        '\033[91mS\033[0m',
        '\033[92mS\033[0m',
        '\033[93mS\033[0m',
        '\033[94mS\033[0m',
        '\033[95mS\033[0m']
    _color_index = 0

    def __init__(self, size):
        self.size = size
        self.hits = 0
        self.symbol = Ship._color_cycle[Ship._color_index % len(Ship._color_cycle)]
        Ship._color_index += 1

    def is_hit(self) -> bool:
        """Registers a hit on the ship"""
        self.hits += 1
        return self.is_sunk()

    def get_size(self) -> int:
        """Returns the size of the ship"""
        return self.size

    def is_sunk(self):
        """Checks if the ship is sunk"""
        return self.hits >= self.size

    def get_symbol(self) -> str:
        """Each time a ship is placed it will be a different color."""
        return self.symbol
