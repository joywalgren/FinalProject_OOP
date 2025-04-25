'''from player import Player
from board import Board
from ai import Opponent
from dumb_ai import DumbOpponent
from menu import Menu


from dumb_strategy import DumbStrategy
from smart_strategy import TargetedStrategy
from opponent import AIPlayer'''

from attack import *

'''
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
'''

def read_input() -> tuple:
    """
    reads the input from the user
    """
    x, y = input("Enter a letter then a number seperated by a space then press Enter\n").split()
    x = ord(x.upper()) - ord('A')
    y = int(y) - 1
    # print(f"User input converted to coordinates: ({x}, {y})")
    return x, y

def game(win, lose):
    difficulty = Player.get_difficulty()
    keep_playing = True
    top_board = Board()
    bottom_board = Board()

    if difficulty == 'h':
        ai = AIPlayer(TargetedStrategy())
    else:
        ai = AIPlayer(DumbStrategy())


    #placeships
    ai.bottom_board.print_board()
    bottom_board.place_ships()

    player_turn = True 
    
    while keep_playing:
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
                    player_turn = False  # Switch to AI

                if ai.bottom_board.check_endgame():
                    print("You win!")
                    win += 1
                    return win, lose
                    break

            else:
                print("\n--- AI's Turn ---")
                while True:
                    hit = ai.attack_player(bottom_board)

                    if bottom_board.check_endgame():
                        print("AI wins!")
                        lose += 1
                        return win, lose # or break if you're inside a bigger loop

                    if not hit:
                        player_turn = True  # End AI's turn
                        break  # Exit the AI's mini-loop


if __name__ == "__main__":
    win, lose = 0, 0
    while True:
        option = Menu.menu()
        if option == 1:
            win, lose = game(win, lose)
            print(f"Score: You: {win}, AI: {lose}")
            again = input("Play again? (y/n): ")
            if again.lower() != 'y':
                break
        else:
            print("Goodbye!")
            break
