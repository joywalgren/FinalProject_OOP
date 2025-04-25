class Menu():
    @staticmethod
    def menu() -> int:
        while True:
            try:
                option = int(input("Battleship\n1) Play game\n2) See file log\n"))
                if option in [1, 2]:
                    return option
                else:
                    print("Invalid option. Please enter valid input.")
            except ValueError:
                print("Invalid input. Please enter a number valid input.")
    
