"""Game
Primary Author: Joy Walgren
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
# decorator imports
from attack import BasicAttack
from attack_validation import ValidationAttack
from attack_logging import LoggingAttack
from attack_stats import StatsAttack


class Main(object):
    """Singleton class Main"""

    _instance = None

    def __init__(self) -> None:
        if Main._instance:
            raise NameError("Cannot create multiple instances of a singleton class Main")
        Main._instance = self
        self._top_board = Board()
        self._bottom_board = Board()
        self._player = Player()
        self._difficulty: str = ''

    def read_input(self) -> tuple[int, int]:
        """
        reads the input from the user
        """
        while True:
            try:
                user_input = input(
                    "Enter a letter (A-J) and a number (1-10) separated by a space:\n"
                ).strip()
                x_str, y_str = user_input.split()
                x = ord(x_str.upper()) - ord('A')
                y = int(y_str) - 1

                if 0 <= x < 10 and 0 <= y < 10:
                    return x, y  # Valid input
                else:
                    print("Invalid coordinates.")
            except ValueError:
                print("Invalid input format.")

    def player_turn(self, ai: AIPlayer) -> bool:
        """Handles all the interactions with the player on their turn"""
        print("\n\033[94m--- Your Turn ---\033[0m")
        while True:
            print("Your Top Board:")
            self._top_board.print_board()
            print("Your Bottom Board (Ships):")
            self._bottom_board.print_board()
            x, y = self.read_input()

            # Build decorator chain
            attack_obj = ValidationAttack(
                StatsAttack(
                    LoggingAttack(
                        BasicAttack(x, y)
                    )
                )
            )
            result = attack_obj.execute(ai.bottom_board)

            # Update top board view
            if result in ["Hit!", "You sank a ship!"]:
                self._top_board._board[y][x].set_cell('H')
                if ai.bottom_board.check_endgame():
                    return True  # Game over
                continue  # Allow another attack on hit

            if result == "Miss!":
                self._top_board._board[y][x].set_cell('M')
                return False  # switch to AI turn

            if result in ["Already Attacked", "Invalid: Repeat Attack"]:
                print("You already tried that spot. Try again.")
                continue

            return False  # Default return if no other condition is met

    def ai_turn(self, ai: AIPlayer) -> bool:
        """Handles the ai's turn"""
        print("\n\033[91m--- AI's Turn ---\033[0m")
        while True:
            hit = ai.attack_player(self._bottom_board)

            if not hit:
                return True  # Turns player turn to true

    def loop(self, reveal_ai_board: bool = False) -> None:
        """The main game loop"""
        # New boards
        self._top_board = Board()
        self._bottom_board = Board()
        self._bottom_board.place_ships()

        # The main game loop
        if self._difficulty == 'h':
            ai = AIPlayer(TargetedStrategy())
        else:
            ai = AIPlayer(DumbStrategy())

        if reveal_ai_board:
            print("\n--- DEMO: AI's Bottom Board (Ship Positions) ---")
            ai.bottom_board.print_board()

        player_turn = True

        while not self._bottom_board.check_endgame() and not ai.bottom_board.check_endgame():
            if player_turn:
                player_turn = self.player_turn(ai)
            else:
                player_turn = self.ai_turn(ai)

        if ai.bottom_board.check_endgame():
            print("You win!")
            self._player.update_player_stats(1, 0)  # Add 1 win
        else:
            self._bottom_board.print_board()
            print("You lose :(")
            self._player.update_player_stats(0, 1)  # Add 1 loss

        # Display stats and log summary
        StatsAttack.report()

    @classmethod
    def get_instance(cls) -> Main:
        """Creates or returns an existing instance.

        Returns:
            Main: Singleton class instance.
        """
        if cls._instance is None:
            cls._instance = cls()
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

        open("data.txt", "w").close()

        while True:
            option = Menu.menu()
            if option == 1:
                manager._difficulty = Player.get_difficulty()

                manager.loop(reveal_ai_board=False)
                again = input("Play again? (y/n): ")
                if again.lower() != 'y':
                    break
            elif option == 2:
                manager._player.display_player_stats()  # Display the player's stats
                input("\nPress Enter to return to menu…")
            elif option == 3:
                manager._difficulty = Player.get_difficulty()

                manager.loop(reveal_ai_board=True)
            elif option == 4:
                break
            else:
                break
        # save data to file before exiting
        manager._player.save_dict_to_file("data.txt", manager._player._data_dict)


if __name__ == "__main__":
    Main.main()  # no pragma
