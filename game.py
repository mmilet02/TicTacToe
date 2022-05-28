from ast import Index
from players import HumanPlayer, ComputerPlayer
import math

class Board():
    def __init__(self) -> None:
        self.board = [" " for i in range(9)]
        self.winner = None

    def print_board(self):
        a = (' ---' *  3 )
        coordinate = 0
        for i in range(1, 8):
            if i%2 == 1:
                print(a)
            else:
                print("| " + " | ".join([self.board[coordinate], self.board[coordinate + 1], self.board[coordinate + 2]]) + " |")
                coordinate += 3
    
    def print_empty_board(self):
        a = (' ---' *  3 )
        coordinate = 0
        for i in range(1, 8):
            if i%2 == 1:
                print(a)
            else:
                print("| " + " | ".join([" ", " ", " "]) + " |")
                coordinate += 3

    def print_board_with_coordinates(self):
        a = (' ---' *  3 )
        coordinate = 1
        for i in range(1, 8):
            if i%2 == 1:
                print(a)
            else:
                print("| " + " | ".join([str(coordinate), str(coordinate + 1), str(coordinate + 2)]) + " |")
                coordinate += 3
    
    def check_is_input_valid(self, coordinate):
        return self.board[coordinate - 1] == " "

    def put_letter(self, letter, coordinate):
        self.board[coordinate - 1] =  letter

    def check_if_the_end(self):
        for i in self.board:
            if i == " ":
                return False
        
        return True

    def isWinner(self, letter, index):
        # check the row
        index = int(index) - 1
        row_ind = math.floor(index / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            print("The End. Player " + letter.upper() + " is winner :)")
            self.print_board()
            return True
        col_ind = index % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            print("The End. Player " + letter.upper() + " is winner :)")
            self.print_board()
            return True
        if index % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                print("The End. Player " + letter.upper() + " is winner :)")
                self.print_board()
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                print("The End. Player " + letter.upper() + " is winner :)")
                self.print_board()
                return True
        return False


def play(player1, player2, board):
    print("Game is starting. Good Luck!")
    print("Here is Board indexes template:")
    board.print_board_with_coordinates()

    the_end = False
    round = 0

    while not(the_end):
        round += 1
        print("ROUND " + str(round) + ".")
        the_end = player1.make_move(board)
        if the_end:
            continue
        print("Board after Player1:")
        board.print_board()

        if board.check_if_the_end():
            print("THE END. It is tie")
            the_end = True
            continue

        the_end = player2.make_move(board)
        if the_end:
            continue
        print("Board after Player2:")
        board.print_board()


if __name__ == '__main__':
    game_mode = 0
    player1 = None
    player2 = None
    valid_input = False
    board = Board()

    print("Welcom to Tic-Tac-Toe. Here is some rules about the game:")
    print("RULES:")
    print("1. The game is played on a grid that's 3 squares by 3 squares.")
    board.print_empty_board()
    print("2. One player is X, and the other one is O. Players take turns putting their marks in empty squares.")
    print("3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
    print("4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")

    print("Now pick type of the game you want to play:")
    print("Type [1] - for Human vs Human")
    print("Type [2] - for Human vs Computer")
    print("Type [3] - for Computer vs Computer")
    print("Type [4] - for Human vs Smart Computer")

    while not(valid_input):
        game_mode = input("Enter Game type: ")
        if not(game_mode.strip().isdigit()):
            print("You did not enter a number [" + game_mode + "]. Try again:")
            continue
        
        game_mode = int(game_mode)
        if game_mode >= 1 and game_mode <= 4:
            valid_input = True
        else:
            print("You did not enter a number between 1 and 4 [" + game_mode + "]. Try again:")  


    if game_mode == 1:
        player1 = HumanPlayer("X")
        player2 = HumanPlayer("O")
    elif game_mode == 2:
        player1 = HumanPlayer("X")
        player2 = ComputerPlayer("O")
    elif game_mode == 3:
        player1 = ComputerPlayer("X")
        player2 = ComputerPlayer("O")
    elif game_mode == 4:
        pass

    play(player1, player2, board)