from space import *

class Board:
    def __init__(self) -> None:
        self.spaces: tuple[Space, ...] = (
            Go("Go", 0),
            Property("Mediterranean Avenue", 1, 60, 2, "brown"),
            CommunityChestSpace("Community Chest", 2),
            Property("Baltic Avenue", 3, 60, 4, "brown"),
            Tax("Income Tax", 4, 200),
            Railroad("Reading Railroad", 5),
            Property("Oriental Avenue", 6, 100, 6, "light_blue"),
            ChanceSpace("Chance", 7),
            Property("Vermont Avenue", 8, 100, 6, "light_blue"),
            Property("Connecticut Avenue", 9, 120, 8, "light_blue"),
            Jail("Just Visiting", 10),
            Property("St. Charles Place", 11, 140, 10, "pink"),
            Utility("Electric Company", 12),
            Property("States Avenue", 13, 140, 10, "pink"),
            Property("Virginia Avenue", 14, 160, 12, "pink"),
            Railroad("Pennsylvania Railroad", 15),
            Property("St. James Place", 16, 180, 14, "orange"),
            CommunityChestSpace("Community Chest", 17),
            Property("Tennessee Avenue", 18, 180, 14, "orange"),
            Property("New York Avenue", 19, 200, 16, "orange"),
            FreeParking("Free Parking", 20),
            Property("Kentucky Avenue", 21, 220, 18, "red"),
            ChanceSpace("Chance", 22),
            Property("Indiana Avenue", 23, 220, 18, "red"),
            Property("Illinois Avenue", 24, 240, 20, "red"),
            Railroad("B & O Railroad", 25),
            Property("Atlantic Avenue", 26, 260, 22, "yellow"),
            Property("Ventnor Avenue", 27, 260, 22, "yellow"),
            Utility("Water Works", 28),
            Property("Marvin Gardens", 29, 280, 24, "yellow"),
            GoToJail("Go to Jail", 30),
            Property("Pacific Avenue", 31, 300, 26, "green"),
            Property("North Carolina Avenue", 32, 300, 26, "green"),
            CommunityChestSpace("Community Chest", 33),
            Property("Pennsylvania Avenue", 34, 320, 28, "green"),
            Railroad("Short Line", 35),
            ChanceSpace("Chance", 36),
            Property("Park Place", 37, 350, 35, "blue"),
            Tax("Luxury Tax", 38, 100),
            Property("Boardwalk", 39, 400, 50, "blue")
        )

    def get_space(self, position: int) -> Space:
        return self.spaces[position]