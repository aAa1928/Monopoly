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


class Property(OwnableSpace):
    def __init__(self, name: str, position: int, price: int, rent_values: list[int], color: str):
        super().__init__(name, position, price)
        # rent_values would be [Base, 1H, 2H, 3H, 4H, Hotel]
        self.rent_values = rent_values 
        self.houses = 0
        self.color = color
        self.hotel = False

    @property
    def rent(self) -> int:
        if self.hotel:
            return self.rent_values[5]
        if self.houses > 0:
            return self.rent_values[self.houses]
        
        base_rent = self.rent_values[0]
        if self.owner:
            
            owned_in_group = [p for p in self.owner.properties 
                            if isinstance(p, Property) and p.color == self.color]
            
            if len(owned_in_group) == self.owner.game.board.get_color_group_size(self.color):
                return base_rent * 2
                
        return base_rent
    
    def on_land(self, player: "Player") -> None:
        super().on_land(player)
        if self.owner is not None and self.owner != player and not self.is_mortgaged:
            player.game.pay(player, self.rent, self.owner)


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
        super().on_land(player)
        if self.owner is not None and self.owner != player and not self.is_mortgaged:
            player.game.pay(player, self.util_multiplier * player.last_roll_total, self.owner)


class Railroad(OwnableSpace):
    def __init__(self, name: str, position: int):
        super().__init__(name, position, 200)

    @property
    def rent(self) -> int:
        if self.owner is None:
            return 0
        count = len([s for s in self.owner.properties if isinstance(s, Railroad)])
        return 25 * (2 ** (count - 1)) if count > 0 else 0

    def on_land(self, player: "Player") -> None:
        super().on_land(player)
        if self.owner is not None and self.owner != player and not self.is_mortgaged:
            player.game.pay(player, self.rent, self.owner)


class Tax(Space):
    def __init__(self, name: str, position: int, tax: int):
        super().__init__(name, position)
        self.tax = tax

    def on_land(self, player: "Player") -> None:
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