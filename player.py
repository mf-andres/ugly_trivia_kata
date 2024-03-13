class Player:
    def __init__(self, name: str):
        self.name = name
        self.coins = 0
        self.place = 0

    def has_won(self):
        return self.coins == 6
