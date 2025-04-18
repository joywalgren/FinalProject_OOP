"""playgame.py"""

from attack import Attack, Player, Board, IsWon


class PlayGame():
    def playgame():
        gamerunning: bool = True
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        players = [player1, player2]
        turn = 0

        while gamerunning:
            
            current = players[turn % 2]
            opponent = players[(turn + 1) % 2]

            print(f"\n{current.name}'s Turn")
            #Board.print_board(player1.board)
            player2.board.print_board(show_ships = False) #hide ships
            player1.board.print_board(show_ships=True) #reveal ships


            try:
                coords = input("Enter a letter then a number seperated by a space! then press Enter:\n").split()
                if len(coords) != 2:
                    raise ValueError
                x, y = coords
                x = ord(x.upper()) - ord('A')
                y = int(y) -1
                #print (x,y, " YES")
                if not (0 <= x < 10 and 0 <= y < 10):
                    raise ValueError
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
                continue
            
            attack = Attack(y, x)
            result = attack.execute(opponent.board)
            print(f"{current.name} attacks {coords} → {result}")

            # Check win condition
            if IsWon(opponent.board).check():
                print(f"\n{current.name} wins!")
                gamerunning = False
        
        
            turn += 1
        


if __name__ == "__main__":
    PlayGame.playgame() 