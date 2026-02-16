from space import *

class Board:
    def __init__(self) -> None:
        self.spaces: tuple[Space, ...] = (
            Go("Go", 0),
            Property("Mediterranean Avenue", 1, 60, [2, 10, 30, 90, 160, 250], "brown"),
            CommunityChestSpace("Community Chest", 2),
            Property("Baltic Avenue", 3, 60, [4, 20, 60, 180, 320, 450], "brown"),
            Tax("Income Tax", 4, 200),
            Railroad("Reading Railroad", 5),
            Property("Oriental Avenue", 6, 100, [6, 30, 90, 270, 400, 550], "light_blue"),
            ChanceSpace("Chance", 7),
            Property("Vermont Avenue", 8, 100, [6, 30, 90, 270, 400, 550], "light_blue"),
            Property("Connecticut Avenue", 9, 120, [8, 40, 100, 300, 450, 600], "light_blue"),
            Jail("Just Visiting", 10),
            Property("St. Charles Place", 11, 140, [10, 50, 150, 450, 625, 750], "pink"),
            Utility("Electric Company", 12),
            Property("States Avenue", 13, 140, [10, 50, 150, 450, 625, 750], "pink"),
            Property("Virginia Avenue", 14, 160, [12, 60, 180, 500, 700, 900], "pink"),
            Railroad("Pennsylvania Railroad", 15),
            Property("St. James Place", 16, 180, [14, 70, 200, 550, 750, 950], "orange"),
            CommunityChestSpace("Community Chest", 17),
            Property("Tennessee Avenue", 18, 180, [16, 80, 220, 600, 800, 1000], "orange"),
            Property("New York Avenue", 19, 200, [18, 90, 250, 700, 900, 1100], "orange"),
            FreeParking("Free Parking", 20),
            Property("Kentucky Avenue", 21, 220, [18, 90, 250, 700, 900, 1100], "red"),
            ChanceSpace("Chance", 22),
            Property("Indiana Avenue", 23, 220, [18, 90, 250, 700, 900, 1100], "red"),
            Property("Illinois Avenue", 24, 240, [20, 100, 300, 750, 950, 1250], "red"),
            Railroad("B & O Railroad", 25),
            Property("Atlantic Avenue", 26, 260, [22, 110, 330, 800, 975, 1150], "yellow"),
            Property("Ventnor Avenue", 27, 260, [22, 110, 330, 800, 975, 1150], "yellow"),
            Utility("Water Works", 28),
            Property("Marvin Gardens", 29, 280, [24, 120, 360, 850, 1025, 1200], "yellow"),
            GoToJail("Go to Jail", 30),
            Property("Pacific Avenue", 31, 300, [26, 130, 390, 900, 1100, 1275], "green"),
            Property("North Carolina Avenue", 32, 300, [26, 130, 390, 900, 1100, 1275], "green"),
            CommunityChestSpace("Community Chest", 33),
            Property("Pennsylvania Avenue", 34, 320, [28, 150, 450, 1000, 1200, 1400], "green"),
            Railroad("Short Line", 35),
            ChanceSpace("Chance", 36),
            Property("Park Place", 37, 350, [35, 175, 500, 1100, 1300, 1500], "blue"),
            Tax("Luxury Tax", 38, 100),
            Property("Boardwalk", 39, 400, [50, 200, 600, 1400, 1750, 2000], "blue")
        )

    def __getitem__(self, index: int) -> Space:
        return self.spaces[index % len(self.spaces)]
    
    def __len__(self) -> int:
        return len(self.spaces)
    
    def get_color_group_size(self, color: str) -> int:
        return len([s for s in self.spaces if isinstance(s, Property) and s.color == color])