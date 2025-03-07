import os
from Player import Player
from Board import Board
from Menu import Menu

def clear_screen():
    os.system("cls")

class Game:
    def __init__(self):
        self.players = [Player(),Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0
        self.symbols=set()


    def setup_players(self):
        for i, player in enumerate(self.players, start=1):
            print(f"Player {i}, Enter Your Details: ")
            player.choose_name()
            player.choose_unique_symbol(self.symbols)
            clear_screen()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play_turn(self):
        player = self.players[self.current_player_index]
        board = self.board.display_board()
        clear_screen()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("choose where to play (1-9)"))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Enter A valid Choice from 1 to 9")
            except ValueError:
                print("Enter A valid Choice from 1 to 9")
        self.switch_player()

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]] and \
                    self.board.board[combo[0]] != str(combo[0] + 1):
                return self.players[self.current_player_index]
        return None

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board) and not self.check_win()

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index=0
        self.play_game()

    def play_game(self):
        while True:
            self.play_turn()
            winner = self.check_win()
            if winner:
                self.board.display_board()
                print(f"Congratulations {winner.name}! You have won the game!")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            elif self.check_draw():
                self.board.display_board()
                print("The game is a draw!")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def quit_game(self):
        self.board.reset_board()
        print("Thank You For Playing")

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
