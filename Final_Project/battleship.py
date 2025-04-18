from player import Player
from board import Board


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


Player.get_name()


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
ai_top_board = Board()
ai_bottom_board = Board()

bottom_board.place_ships()
ai_bottom_board.place_ships()
print(f"player board endgame: {bottom_board.check_endgame()}\nEnemy board endgame {ai_bottom_board.check_endgame()}")

# as long as all the ships in one players arent sunk, keep playing
while not bottom_board.check_endgame() and not ai_bottom_board.check_endgame():
    print("Your Top Board:")
    top_board.print_board()
    print("Your Bottom Board (Ships):")
    bottom_board.print_board()
    print("AI's Bottom Board (Hidden):")
    ai_bottom_board.print_board()  # This would normally be hidden in a real game
    # currently only the player attacks
    user_input = read_input()
    attack(top_board, ai_bottom_board, user_input[0], user_input[1])
