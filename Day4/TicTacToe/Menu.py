class Menu:
    def get_choice(self):
        while True:
            choice = input("Enter your choice 1 or 2: ")
            if choice.isdigit() and choice in ('1', '2'):
                return choice
            else:
                print("Invalid Choice, Please input a valid Choice")

    def display_main_menu(self):
        print("Play X - O Now!")
        print("1. Start Game")
        print("2. Quit Game")
        return self.get_choice()

    def display_endgame_menu(self):
        print("1. Restart Game")
        print("2. Quit Game")
        return self.get_choice()