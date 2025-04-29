'''
Player class to keep track of player stats
'''

from collections import defaultdict


class Player():
    def __init__(self) -> None:
        # name = " "
        self._name = self.get_name().lower()
        outfile = "data.txt"
        self._data_dict = self.create_dict_from_file(outfile, ',')

    @staticmethod
    def get_name() -> str:
        '''Get and save the name from the player'''
        name = input("Hello! Welcome to our Battleship Game! What is your name?")
        print("Hello ", name, "! Are you ready to play?")
        return name

    @staticmethod
    def get_difficulty() -> str:
        '''Get and save the difficulty level from the player'''
        diff = input("What difficulty would you like to play on? 'h' for Hard 'e' for Easy\n ")
        return diff

    def create_dict_from_file(self, file_path, delimiter=','):
        """
        Creates a dictionary with multiple values per key from a file.
        """
        data_dict = defaultdict(list)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(delimiter)
                        key = parts[0]  # Name
                        wins = int(parts[1])
                        losses = int(parts[2])
                        data_dict[key].extend([wins, losses])
        except FileNotFoundError:
            print(f"File not found: {file_path}. Starting with an empty data dictionary.")
        return dict(data_dict)

    def save_dict_to_file(self, file_path, data, delimiter=','):
        """
        Saves the dictionary back into the file for future use.
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            for key, values in data.items():
                file.write(f"{key}{delimiter}{values[0]}{delimiter}{values[1]}\n")

    def update_player_stats(self, wins: int, losses: int) -> None:
        """
        Updates the player's wins and losses in the data dictionary.
        """
        if self._name in self._data_dict:
            self._data_dict[self._name][0] += wins
            self._data_dict[self._name][1] += losses
        else:
            self._data_dict[self._name] = [wins, losses]

    def display_player_stats(self) -> None:
        """
        Displays the player's stats (wins and losses) from the data dictionary.
        """
        if self._name in self._data_dict:
            wins, losses = self._data_dict[self._name]
            print(f"{self._name.capitalize()}, you have won {wins} times and lost {losses} times.")
        else:
            print(f"{self._name.capitalize()}, you have no recorded games yet.")
