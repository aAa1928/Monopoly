from space import *

class Board:
    def __init__(self):
        self.spaces = self._build_board()

    def _build_board(self):
        return [
            Go("Go", 0),
            Property("Mediterranean Avenue", 1, 60, 2),
            CommunityChest("Community Chest", 2),
            Property("Baltic Avenue", 3, 60, 4),
            Tax("Income Tax", 4, 200),
            Railroad("Reading Railroad", 5),
            Property("Oriental Avenue", 6, 100, 6),
            Chance("Chance", 7),
            Property("Vermont Avenue", 8, 100, 6),
            Property("Connecticut Avenue", 9, 120, 8),
            Jail("Just Visiting", 10),
            Property("St. Charles Place", 11, 140, 10),
            Utility("Electric Company", 12),
            Property("States Avenue", 13, 140, 10),
            Property("Virginia Avenue", 14, 160, 12),
            Railroad("Pennsylvania Railroad", 15),
            Property("St. James Place", 16, 180, 14),
            CommunityChest("Community Chest", 17),
            Property("Tennessee Avenue", 18, 180, 14),
            Property("New York Avenue", 19, 200, 16),
            FreeParking("Free Parking", 20),
            Property("Kentucky Avenue", 21, 220, 18),
            Chance("Chance", 22),
            Property("Indiana Avenue", 23, 220, 18),
            Property("Illinois Avenue", 24, 240, 20),
            Railroad("B & O Railroad", 25),
            Property("Atlantic Avenue", 26, 260, 22),
            Property("Ventnor Avenue", 27, 260, 22),
            Utility("Water Works", 28),
            Property("Marvin Gardens", 29, 280, 24),
            GoToJail("Go to Jail", 30),
            Property("Pacific Avenue", 31, 300, 26),
            Property("North Carolina Avenue", 32, 300, 26),
            CommunityChest("Community Chest", 33),
            Property("Pennsylvania Avenue", 34, 320, 28),
            Railroad("Short Line", 35),
            Chance("Chance", 36),
            Property("Park Place", 37, 350, 35),
            Tax("Luxury Tax", 38, 100),
            Property("Boardwalk", 39, 400, 50)
        ]

    def get_space(self, position):
        return self.spaces[position]