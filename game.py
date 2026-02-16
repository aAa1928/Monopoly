from functools import singledispatch
from typing import Any, Iterable, Literal, TYPE_CHECKING, Optional

from board import Board
from player import Player

if TYPE_CHECKING:
    from space import OwnableSpace, Property

class Game():
    def __init__(self, players: Iterable[Player]) -> None:
        self.players = tuple(player for player in players)
        for player in self.players:
            player.game = self
        self.houses: int = 32
        self.hotels = 12
        self.board = Board()

    @property
    def active_players(self) -> Iterable[Player]:
        return (player for player in self.players if not player.bankrupt)

    def pay(self, debtor: Player, amount: int, creditor: Optional[Player] = None):
        print(f'{debtor.name} pays ${amount} to {creditor.name if creditor else "bank"}')
        debtor.cash -= amount
        if debtor.cash < 0:
            self.resolve_debt(debtor, creditor)
        elif creditor:
            creditor.cash += amount

    def resolve_debt(self, debtor: Player, creditor: Optional[Player] = None):
        raise NotImplementedError("Debt resolution not implemented yet.")
    
    def auction(self, property: "OwnableSpace"):
        raise NotImplementedError("Auction logic not implemented yet.")
    
    def trade(self, player1: Player, player2: Player, offer: dict[str, Any], request: dict[str, Any]):
        raise NotImplementedError("Trade logic not implemented yet.")
    
    def buy_property(self, player: Player, property: "OwnableSpace"):
        if property.owner is not None:
            raise ValueError(f"{property} is already owned by {property.owner.name}.")
        if player.cash < property.price:
            raise ValueError(f"{player.name} does not have enough cash to buy {property}.")
        
        player.cash -= property.price
        property.owner = player
        player.properties.append(property)
        print(f"{player.name} bought {property} for ${property.price}.")

    def build(self, player: Player, property: "Property", building_type: Literal['house', 'hotel']) -> None:
        if property.owner != player:
            raise ValueError(f"{player.name} does not own {property}.")
        
        match property.color:
            case "brown" | "light_blue":
                cost = 50
            case "pink" | "orange":
                cost = 100
            case "red" | "yellow":
                cost = 150
            case "green" | "blue":
                cost = 200
            case _:
                raise ValueError(f"Invalid property color: {property.color}")
        
        if player.cash < cost:
            raise ValueError(f"{player.name} does not have enough cash to build on {property}.")
        
        match building_type:
            case 'house':
                if property.houses >= 4:
                    raise ValueError(f"{property} already has 4 houses. Must build a hotel next.")
                if self.houses <= 0:
                    raise ValueError("No houses left in the bank.")
                property.houses += 1
                self.houses -= 1
                player.cash -= cost
                print(f"{player.name} built a house on {property} for ${cost}.")
            
            case 'hotel':
                if property.houses != 4:
                    raise ValueError(f"{property} must have 4 houses before building a hotel.")
                if property.hotel:
                    raise ValueError(f"{property} already has a hotel.")
                if self.hotels <= 0:
                    raise ValueError("No hotels left in the bank.")
                property.hotel = True
                property.houses = 0
                self.hotels -= 1
                self.houses += 4  # Return the 4 houses to the bank
                player.cash -= cost
                print(f"{player.name} built a hotel on {property} for ${cost}.")
            case _:
                raise ValueError(f"Invalid building type: {building_type}")
        
    @singledispatch
    def mortgage_property(self, player: Player, property: "OwnableSpace"):
        if property.owner != player:
            raise ValueError(f"{player.name} does not own {property}.")
        
        property.is_mortgaged = True
        player.cash += property.price // 2
        print(f"{player.name} mortgaged {property} for ${property.price // 2}.")

    @mortgage_property.register
    def _(self, player: Player, property: "Property"):
        if property.houses > 0 or property.hotel:
            raise ValueError(f"Cannot mortgage {property} while it has houses or a hotel.")
        if property.owner != player:
            raise ValueError(f"{player.name} does not own {property}.")
        
        property.is_mortgaged = True
        player.cash += property.price // 2
        print(f"{player.name} mortgaged {property} for ${property.price // 2}.")

    @mortgage_property.register
    def _(self, player: Player, property: "OwnableSpace"):
        if property.owner != player:
            raise ValueError(f"{player.name} does not own {property}.")
        
        property.is_mortgaged = True
        player.cash += property.price // 2
        print(f"{player.name} mortgaged {property} for ${property.price // 2}.")