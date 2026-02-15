from random import randint
from typing import TYPE_CHECKING, Optional

from board import Board

if TYPE_CHECKING:
    from game import Game
    from space import Card, Space, OwnableSpace

class Player:

    def __init__(self, name: str) -> None: # pyright: ignore[reportGeneralTypeIssues]
        self.name = name
        self.game: Game = None  # type: ignore
        self.cash = 1500

        self.position = 0
        self._doubles_rolled = 0
        self.properties: list[OwnableSpace] = []
        self.cards: list[Card] = []
        self._in_jail: int = 0
        self.bankrupt: bool = False

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
    def space(self) -> "Space":
        return self.game.board.get_space(self.position)


    def _advance_and_land(self, spaces: int) -> "Space":
        if self.game is None:
            raise ValueError("Player must be associated with a game to move.")
        
        new_position = self.position + spaces

        if new_position >= 40:
            self.cash += 200
            print(f"{self.name} passed Go! Collected $200.")

        self.position = new_position % 40
        space = self.game.board.get_space(self.position)
        space.on_land(self)
        return space

    def move(self) -> tuple[int, bool, Optional["Space"]]:
        if self.in_jail:
            roll_total, is_double = self.roll_dice()
            self.last_roll_total = roll_total
            self.in_jail += 1
            
            if is_double:
                self.in_jail = 0
                return roll_total, is_double, self._advance_and_land(roll_total)

            if self.in_jail > 3:
                self.in_jail = 0
                self.cash -= 50
                return roll_total, is_double, self._advance_and_land(roll_total)

            return roll_total, is_double, None

        roll_total, is_double = self.roll_dice()
        self.last_roll_total = roll_total

        if self.doubles_rolled == 3:
            self.in_jail = 1
            return roll_total, is_double, None

        return roll_total, is_double, self._advance_and_land(roll_total)
    
    def roll_dice(self) -> tuple[int, bool]:
        rolls = [randint(1, 6) for _ in range(2)]
        is_double = len(set(rolls)) == 1
        if is_double:
            self.doubles_rolled += 1
        else:
            self.doubles_rolled = 0
        return sum(rolls), is_double

    def __str__(self):
        return f"{self.name}: ${self.cash}"