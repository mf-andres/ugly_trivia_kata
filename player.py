class Player:
    def __init__(self, name: str):
        self.name = name
        self.coins = 0
        self.place = 0
        self.is_in_penalty_box = False
        self.is_getting_out_of_penalty_box = False

    def has_won(self):
        return self.coins == 6
