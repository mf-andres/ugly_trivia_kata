class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.coins: int = 0
        self.place: int = 0
        self.is_in_penalty_box: bool = False

    def has_won(self) -> bool:
        return self.coins == 6
