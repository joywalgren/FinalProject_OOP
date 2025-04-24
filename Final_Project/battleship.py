from player import Player
from board import Board
from ai import Opponent
from dumb_ai import Opponent
from menu import Menu


def attack(player_top_board: Board, enemy_board: Board, x: int, y: int):
    """
    Handles an attack on the enemy board and updates the player's top board.
    """
    if enemy_board.attack(x, y):  # Check if the attack hits a ship
        print("Hit!")
        player_top_board._board[y][x].set_cell('H')  # update top board
    else:
        print("Miss!")
        player_top_board._board[y][x].set_cell('M')  # update top board


option = Menu.menu()
Player.get_name()
difficulty = Player.get_difficulty()



def read_input() -> tuple:
    """
    reads the input from the user
    """
    x, y = input("Enter a letter then a number seperated by a space then press Enter\n").split()
    x = ord(x.upper()) - ord('A')
    y = int(y) - 1
    # print(f"User input converted to coordinates: ({x}, {y})")
    return x, y


top_board = Board()
bottom_board = Board()
# for smart ai
ai = Opponent()
ai.place_ships()

# for dumb
dumb_ai = Opponent()
dumb_ai.place_ships()


bottom_board.place_ships()

if option == 1: #option play game 
    if difficulty == "h":
        player_turn = True

        while not bottom_board.check_endgame() and not ai.bottom_board.check_endgame():
            print("Your Top Board:")
            top_board.print_board()
            print("Your Bottom Board (Ships):")
            bottom_board.print_board()

            if player_turn:
                print("\n--- Your Turn ---")
                x, y = read_input()
                hit = ai.bottom_board.attack(x, y)

                if hit:
                    print("Hit!")
                    top_board._board[y][x].set_cell('H')
                else:
                    print("Miss!")
                    top_board._board[y][x].set_cell('M')
                    player_turn = False  # Give AI the turn

                if ai.bottom_board.check_endgame():
                    print("You win!")
                    break
            else:

            print("\n--- AI's Turn ---")
            hit = ai.attack_player(bottom_board)  
            if not hit:
                player_turn = True  # Give player the turn

                if bottom_board.check_endgame():
                    print("AI wins!")

    else:
        player_turn = True

        while not bottom_board.check_endgame() and not dumb_ai.bottom_board.check_endgame():
            print("Your Top Board:")
            top_board.print_board()
            print("Your Bottom Board (Ships):")
            bottom_board.print_board()

            if player_turn:
                print("\n--- Your Turn ---")
                x, y = read_input()
                hit = dumb_ai.bottom_board.attack(x, y)

                if hit:
                    print("Hit!")
                    top_board._board[y][x].set_cell('H')
                else:
                    print("Miss!")
                    top_board._board[y][x].set_cell('M')
                    player_turn = False  # Give AI the turn

                if dumb_ai.bottom_board.check_endgame():
                    print("You win!")
                    break
            else:

            print("\n--- AI's Turn ---")
            hit = dumb_ai.attack_player(bottom_board)  
            if not hit:
                player_turn = True  # Give player the turn

            if bottom_board.check_endgame():
                print("AI wins!")



    

