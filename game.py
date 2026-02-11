from board import Board
from player import Player

from typing import Iterable

class Game():
    def __init__(self, players: Iterable[Player]) -> None:
        self.players = [player for player in players]
        self.board = Board()
        self.houses: int = 32
        self.hotels = 12