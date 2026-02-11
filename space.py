from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from player import Player

__all__ = [
    "Space",
    "OwnableSpace",
    "Property",
    "Utility",
    "Railroad",
    "Tax",
    "Chance",
    "CommunityChest",
    "GoToJail",
    "Jail",
    "FreeParking",
    "Go",
]

class Space:
    def __init__(self, name: str, position: int):
        self.name = name
        self.position = position

    def on_land(self, player: "Player") -> None:
        print(f"{player.name} landed on {self.name}")

class OwnableSpace(Space):
    def __init__(self, name: str, position: int, price: int):
        super().__init__(name, position)
        self.price = price
        self.owner: Optional["Player"] = None
        self.is_mortgaged: bool = False

    def get_rent(self, dice_roll: int = 0) -> int:
        return 0

    def on_land(self, player: "Player") -> None:
        super().on_land(player)
        if self.owner is not None and self.owner != player and not self.is_mortgaged:
            rent = self.get_rent()
            raise NotImplementedError("Rent payment logic not implemented yet.")

class Property(OwnableSpace):
    def __init__(self, name: str, position: int, price: int, rent: int):
        super().__init__(name, position, price)
        self.base_rent = rent
        self.houses: int = 0
        self.hotel: bool = False

    def get_rent(self, dice_roll: int = 0) -> int:
        if self.hotel:
            return self.base_rent * 5
        return self.base_rent * (self.houses + 1)

class Utility(OwnableSpace):
    def __init__(self, name: str, position: int):
        super().__init__(name, position, 150)

    def get_rent(self, dice_roll: int = 0) -> int:
        return dice_roll * 4

class Railroad(OwnableSpace):
    def __init__(self, name: str, position: int):
        super().__init__(name, position, 200)

    def get_rent(self, dice_roll: int = 0) -> int:
        return 25

class Tax(Space):
    def __init__(self, name: str, position: int, tax: int):
        super().__init__(name, position)
        self.tax = tax

    def on_land(self, player: "Player") -> None:
        super().on_land(player)
        raise NotImplementedError("Tax payment logic not implemented yet.")

class Chance(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)

class CommunityChest(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)

class GoToJail(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)

class Jail(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)

class FreeParking(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)

class Go(Space):
    def __init__(self, name: str, position: int):
        super().__init__(name, position)