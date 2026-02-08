from game import Game, Player

from time import sleep


if __name__ == "__main__":

    game = Game(players=[Player('A'), Player('B')])

    while game.players:
        for player in game.players:
            while player:
                sleep(2)
                roll = player.roll_dice()
                
                if player.in_jail:
                    player.in_jail += 1
                    if roll[1]:  # Rolled doubles
                        player.in_jail = 0
                        player.position = (player.position + roll[0]) % 40
                    elif player.in_jail > 3:  # 3 rolls completed
                        player.in_jail = 0
                        player.position = (player.position + roll[0]) % 40
                    else:
                        print(f"{player.name} rolled a {roll[0]} but remains in jail\n")
                        break
                else:
                    player.position = (player.position + roll[0]) % 40
                    
                    if player.doubles_rolled == 3:
                        player.in_jail = 1
                        print(f"{player.name} rolled 3 doubles in a row and goes to jail!\n")
                        break
                
                print(f"{player.name} rolled a {roll[0]} {'(double)' if roll[1] else ''}")
                print('Current position:', player.position)
                space = game.board.get_space(player.position)
                print(space, space.name, '\n')

                if not roll[1]:
                    break