class Menu():
    @staticmethod
    def menu() -> int:
        '''Simple menu function that let's the user choose to play the
        game, see the log file, or quit'''
        while True:
            try:
                option = int(input("Battleship\n1) Play game\n2) See file"
                                   "log\n3) Demo mode\n4) Quit\n"))
                if option in [1, 2, 3, 4]:
                    return option
                else:
                    print("Invalid option. Please enter valid input.")
            except ValueError:
                print("Invalid input. Please enter a number valid input.")
