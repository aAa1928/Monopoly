from board import Board
from player import Player

class Game():
    def __init__(self, players: list[Player]) -> None:
        self.players = [player for player in players]
        self.board = Board()
        self.houses: int = 32
        self.hotels = 12