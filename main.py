from time import sleep

from game import Game, Player

if __name__ == "__main__":

    game = Game(players=[Player('A'), Player('B')])
    
    while game.players:
        for player_index, player in enumerate(game.players):
            while player:
                
                if player_index == 0:
                    response = input(f"{player.name}, roll dice? (y/n): ").lower()
                    if response != 'y':
                        print("Error: You must roll the dice.\n")
                        continue
                else:
                    sleep(1)
                
                roll_total, is_double, space = player.move()

                if space is None:
                    if is_double and player.in_jail:
                        print(f"{player.name} rolled 3 doubles in a row and goes to jail!\n")
                    else:
                        print(f"{player.name} rolled a {roll_total} but remains in jail\n")
                    break

                print(f"{player.name} rolled a {roll_total} {'(double) ' if is_double else ''}and landed on {space} ({player.position})")
                print(player, end="\n\n")

                # Handle property purchase
                if hasattr(space, 'owner') and space.owner is None and hasattr(space, 'price'): # pyright: ignore[reportAttributeAccessIssue]
                    if player_index == 0:
                        choice = input(f"Buy {space} for ${space.price}? (y/n): ").lower() # pyright: ignore[reportAttributeAccessIssue]
                        if choice == 'y':
                            game.buy_property(player, space)  # pyright: ignore[reportArgumentType]
                    print()

                if not is_double:
                    break