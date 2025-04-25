class Player():
    def __init__(self) -> None:
        name = " "
        self._name = name

    @staticmethod
    def get_name() -> str:
        name = input("Hello! Welcome to our Battleship Game! What is your name? ")
        print("Hello ", name, "! Are you ready to play?")

    @staticmethod
    def get_difficulty() -> str:
        diff = input("What difficulty would you like to play on? 'h' for Hard 'e' for Easy\n ")
        return diff