class Cell:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._cell = "~"  # starts off as water/empty
        self._ship = None  # Reference to a Ship object if present

    def get_cell(self):
        """Returns H = hit, M = miss, S = ship, ~ = water"""
        return self._cell

    def set_cell(self, marker: str) -> None:
        """Sets a piece of the board to a value"""
        if marker in ['H', 'M', 'S', '~']:
            self._cell = marker
        else:
            print("Invalid Marker")

    def has_ship(self) -> bool:
        """Checks if the cell contains a ship"""
        return self._ship is not None

    def place_ship(self, ship):
        """Places a ship in the cell"""
        self._ship = ship  # uses loose coupling
        self._cell = 'S'

    def hit(self) -> bool:
        """Marks the cell as hit and updates the ship if present."""
        # print(f"Attacking cell ({self._x}, {self._y}): Current state = {self._cell}")
        if self._cell == 'S':
            self._cell = 'H'
            self._ship.is_hit()
            return True  # yes it hit
        elif self._cell == '~':
            self._cell = 'M'
        return False
