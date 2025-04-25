"""Game
Author: Joy Walgren
Date: 4/24/2025
The manager class for battleship
using the singleton pattern.
"""

from __future__ import annotations
from board import Board
from player import Player
from menu import Menu
from dumb_strategy import DumbStrategy
from smart_strategy import TargetedStrategy
from opponent import AIPlayer


class Main(object):
    """Singleton class Main"""

    _instance = None

    def __init__(self) -> None:
        if Main._instance:
            raise NameError("Cannot create multiple instances of a singleton class Main")
        Main._instance = self
        self._top_board = Board()
        self._bottom_board = Board()
        self._wins = 0
        self._losses = 0
        Player.get_name()


    def read_input(self) -> tuple:
        """
        reads the input from the user
        """
        while True:
            try:
                user_input = input(
                    "Enter a letter (A-J) and a number (1-10) separated by a space:\n"
                    ).strip()
                x, y = user_input.split()
                x = ord(x.upper()) - ord('A')
                y = int(y) - 1

                if 0 <= x < 10 and 0 <= y < 10:
                    return x, y  # Valid input
                else:
                    print("Invalid coordinates.")
            except ValueError:
                print("Invalid input format.")

    def loop(self):
        keep_playing = True
        top_board = Board()
        bottom_board = Board()

        if self._difficulty == 'h':
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
                    while True:
                        x, y = self.read_input()
                        try:
                            hit = ai.bottom_board.attack(x, y)
                            break  # Exit loop on successful attack
                        except ValueError as e:
                            print(e)  # e.g., "This square has already been attacked!"

                    if hit:
                        print("Hit!")
                        top_board._board[y][x].set_cell('H')
                    else:
                        print("Miss!")
                        top_board._board[y][x].set_cell('M')
                        player_turn = False  # Switch to AI

                    if ai.bottom_board.check_endgame():
                        print("You win!")
                        self._wins += 1
                        return

                else:
                    print("\n--- AI's Turn ---")
                    while True:
                        hit = ai.attack_player(bottom_board)

                        if bottom_board.check_endgame():
                            print("AI wins!")
                            self._losses += 1
                            break  # or break if you're inside a bigger loop

                        if not hit:
                            player_turn = True  # End AI's turn
                            break  # Exit the AI's mini-loop

    @classmethod
    def get_instance(cls) -> Main:
        """Creates or returns an existing instance.

        Returns:
            Main: Singleton class instance.
        """
        if not cls._instance:
            cls._instance = Main()
        return cls._instance

    @classmethod
    def reset_instance(cls) -> None:
        """Resets the instance
        """
        cls._instance = None

    @staticmethod
    def main() -> None:
        """Main static method."""
        manager = Main.get_instance()
        while True:
            option = Menu.menu()
            if option == 1:
                manager._difficulty = Player.get_difficulty()
                manager.loop()
                print(f"Score: You: {manager._wins}, AI: {manager._losses}")
                again = input("Play again? (y/n): ")
                if again.lower() != 'y':
                    break
            else:
                print(f"Total Score: You : {manager._wins}, AI: {manager._losses}")
                break


if __name__ == "__main__":
    Main.main()
