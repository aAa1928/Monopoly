from typing import Any, Iterable, TYPE_CHECKING, Optional

from board import Board
from player import Player

if TYPE_CHECKING:
    from space import OwnableSpace

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

    def mortgage_property(self, player: Player, property: "OwnableSpace"):
        raise NotImplementedError("Mortgage logic not implemented yet.")