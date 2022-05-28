import random

class Player():
    def __init__(self, letter):
        self.letter = letter

    def getLetter(self):
        return self.letter

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def make_move(self, board):
        valid_input = False
        coordinate = 0

        while not(valid_input):
            coordinate = input("Enter index of place where you want to put your mark. For help type [h]: ")
            if coordinate .upper() == "H":
                board.print_board_with_coordinates()
                continue
            elif not(coordinate.strip().isdigit()):
                print("You did not enter a number [" + coordinate + "]. Try again:")
                continue
            elif int(coordinate) > 9 or int(coordinate) < 1:
                print("Your input needs to be between 1 and 9. Like this: ")
                board.print_board_with_coordinates()
                continue
            elif not(board.check_is_input_valid(int(coordinate))):
                print("Place with your input is already taken. Pick some other place. Here is the board: ")
                continue

            valid_input = True
        
        board.put_letter(self.letter, int(coordinate))
        return board.isWinner(self.letter, coordinate)

    
class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def make_move(self, board):
        valid_input = False
        coordinate = 0

        while not(valid_input):
            coordinate = random.randint(1,9)
            if board.check_is_input_valid(coordinate):
                valid_input = True
        
        board.put_letter(self.letter, coordinate)
        return board.isWinner(self.letter, coordinate)