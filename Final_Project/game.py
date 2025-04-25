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
        """Constructor - uses singleton pattern"""
        if Main._instance:
            raise NameError(
                "Cannot create multiple instances of a singleton class Main"
            )
        Main._instance = self
        self._top_board = Board()
        self._bottom_board = Board()
        Player.get_name()  # asks players name
        option = Menu.menu()
        # should give the option to either play or look at how many wins/losses
        self._difficulty = Player.get_difficulty()  # easy or hard
        if option == 1:
            self.loop(self._difficulty)  # calls the game loop

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

    def loop(self, difficulty: str) -> None:
        """The game loop"""
        self._bottom_board.place_ships()
        if difficulty == 'h':
            ai = AIPlayer(TargetedStrategy())
        else:
            ai = AIPlayer(DumbStrategy())

        player_turn = True
        while not self._bottom_board.check_endgame() and not ai.bottom_board.check_endgame():
            print("Your Top Board:")
            self._top_board.print_board()
            print("Your Bottom Board (Ships):")
            self._bottom_board.print_board()
            # print("AI Bottom Board (Ships):")
            # ai.bottom_board.print_board()

            if player_turn:
                print("\n--- Your Turn ---")
                x, y = self.read_input()
                hit = ai.bottom_board.attack(x, y)

                if hit:
                    print("Hit!")
                    self._top_board._board[y][x].set_cell('H')
                else:
                    print("Miss!")
                    self._top_board._board[y][x].set_cell('M')
                    player_turn = False  # Give AI the turn

            else:
                print("\n--- AI's Turn ---")
                hit = ai.attack_player(self._bottom_board)
                if not hit:
                    player_turn = True  # Give player the turn

        if ai.bottom_board.check_endgame():
            print("You win!")
            # win+=1
        else:
            print("You Lost :(")
            # lose+=1
        play_again: str = 'a'
        while play_again not in ['y', 'n', 'Y', 'N']:
            play_again = input("Would you like to play again? y/n\n")
        if play_again in ['y', 'Y']:
            self._bottom_board.clean_board()
            ai.bottom_board.clean_board()
            self._difficulty = Player.get_difficulty()
            self.loop(self._difficulty)

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
        Main.get_instance()


if __name__ == '__main__':
    Main.main()  # pragma: no cover
