from random import randint

class Player:

    def __init__(self, name: str):
        self.name = name
        self._cash = 1500
        
        self._position = 0
        self._doubles_rolled = 0
        self.properties = NotImplemented
        self._in_jail: int = 0
        self.is_active = False

    @property
    def cash(self):
        return self._cash
        
    @cash.setter
    def cash(self, amount):
        self._cash = amount

    @property
    def doubles_rolled(self):
        return self._doubles_rolled
    
    @doubles_rolled.setter
    def doubles_rolled(self, value):
        self._doubles_rolled = value

    @property
    def in_jail(self):
        return self._in_jail
    
    @in_jail.setter
    def in_jail(self, value):
        self._in_jail = value
        if value == 1:
            self.doubles_rolled = 0
            self.position = 10

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, new_val):
        # Trigger Pass Go only if explicitly passing the 40 threshold
        if new_val >= 40:
            self.cash += 200
            print(f"{self.name} passed Go! Collected $200.")
        
        self._position = new_val % 40

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