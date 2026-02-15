from abc import ABC, abstractmethod
from itertools import count
from typing import TYPE_CHECKING, Optional

import game

if TYPE_CHECKING:
    from player import Player

__all__ = [
    "Space",
    "OwnableSpace",
    "Property",
    "Utility",
    "Railroad",
    "Tax",
    "Card",
    "Chance",
    "ChanceSpace",
    "CommunityChest",
    "CommunityChestSpace",
    "GoToJail",
    "Jail",
    "FreeParking",
    "Go",
]

class Space(ABC):
    def __init__(self, name: str, position: int):
        self.name = name
        self.position = position

    @abstractmethod
    def on_land(self, player: "Player") -> None:
        """Called when a player lands on this space."""
        print(f"{player.name} landed on {self.name}")

    def __str__(self):
        return self.name


class OwnableSpace(Space):
    def __init__(self, name: str, position: int, price: int):
        super().__init__(name, position)
        self.price = price
        self.owner: Optional["Player"] = None
        self.is_mortgaged: bool = False

    def on_land(self, player: "Player") -> None:
        super().on_land(player)
        if self.owner is not None and self.owner != player and not self.is_mortgaged:
            raise NotImplementedError("Rent payment logic not implemented yet.")


class Property(OwnableSpace):
    def __init__(self, name: str, position: int, price: int, rent: int, color: str):
        super().__init__(name, position, price)
        self.base_rent = rent
        self.houses: int = 0
        self.color: str = color
        self.hotel: bool = False
    
    def on_land(self, player: "Player") -> None:
        pass


class Utility(OwnableSpace):
    def __init__(self, name: str, position: int):
        super().__init__(name, position, 150)
    
    @property
    def util_multiplier(self) -> int:
        if self.owner is None:
            return 0
        count = len([s for s in self.owner.properties 
                 if isinstance(s, Utility) and not s.is_mortgaged])
        
        return 10 if count == 2 else 4

    def on_land(self, player: "Player") -> None:
        if self.owner is not None and self.owner != player and not self.is_mortgaged:
            print(player, player.game)
            player.game.pay(player, self.util_multiplier * player.last_roll_total, self.owner)


class Railroad(OwnableSpace):
    def __init__(self, name: str, position: int):
        super().__init__(name, position, 200)

    def on_land(self, player: "Player") -> None:
        if self.owner is not None and self.owner != player and not self.is_mortgaged:
            raise NotImplementedError("Railroad rent logic not implemented yet.")


class Tax(Space):
    def __init__(self, name: str, position: int, tax: int):
        super().__init__(name, position)
        self.tax = tax

    def on_land(self, player: "Player") -> None:
        if not player.game:
            raise ValueError("Game instance is required to process tax payment.")
        
        super().on_land(player)
        print(f"{player.name} owes ${self.tax} in taxes.")
        player.game.pay(player, self.tax)


class Card():
    def __init__(self):
        raise NotImplementedError("Card logic not implemented yet.")

class ChanceSpace(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)

    def on_land(self, player: "Player") -> None:
        super().on_land(player)


class Chance(Card):
    def __init__(self) -> None:
        raise NotImplementedError("Chance card logic not implemented yet.")


class CommunityChestSpace(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)

    def on_land(self, player: "Player") -> None:
        super().on_land(player)


class CommunityChest(Card):
    def __init__(self) -> None:
        raise NotImplementedError("Community Chest card logic not implemented yet.")


class GoToJail(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)

    def on_land(self, player: "Player") -> None:
        super().on_land(player)
        player.in_jail = 1


class Jail(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)

    def on_land(self, player: "Player") -> None:
        super().on_land(player)


class FreeParking(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)

    def on_land(self, player: "Player") -> None:
        super().on_land(player)


class Go(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)

    def on_land(self, player: "Player") -> None:
        super().on_land(player)