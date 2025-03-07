class Board:
    def __init__(self):
        self.board = [str(x) for x in range(1, 10)]

    def reset_board(self):
        self.board = [str(x) for x in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-----")

    def valid_move(self, choice):
        if 1 <= choice <= 9:
            return self.board[choice - 1].isdigit()
        return False

    def update_board(self, choice, symbol):
        if self.valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False
