class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0

    def is_hit(self):
        self.hits += 1
        return self.is_sunk()

    def is_sunk(self):
        return self.hits >= self.size