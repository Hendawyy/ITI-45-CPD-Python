class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter Your Name: ")
            if name.isalpha():
                self.name = name
                break
            else:
                print("Invalid Name, Please input a valid name")

    def choose_symbol(self):
        while True:
            symbol = input("Choose Your Symbol(Single Letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                return symbol.upper()
            else:
                print("Invalid symbol, Please input a valid symbol")

    def choose_unique_symbol(self, symbols):
        while True:
            player_symbol = self.choose_symbol()
            if player_symbol not in symbols:
                symbols.add(player_symbol)
                self.symbol = player_symbol
                break
            else:
                print(f"Symbol {player_symbol} is already taken. Please choose a different one.")
