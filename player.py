from random import randint

class Player:
    def __init__(self, name: str):
        self.name = name
        self.cash = 1500
        self.position = 0
        self.doubles_rolled = 0
        self.properties = NotImplemented
        self.in_jail = False

    def add_cash(self, amount):
        self.cash += amount

    def __str__(self):
        return f"{self.name}: ${self.cash}"
    
    def roll_dice(self) -> tuple[int, bool]:
        rolls = [randint(1, 6) for _ in range(2)]
        is_double = len(set(rolls)) == 1
        if is_double:
            self.doubles_rolled += 1
        else:
            self.doubles_rolled = 0
        return sum(rolls), is_double