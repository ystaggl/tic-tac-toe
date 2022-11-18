"""
A simple tic tac toe program in python
"""
class TicTacToeGame():
    """
    Instance of a game of tic tac toe
    """
    def __init__(self):
        self.current_player = 1
        self.board = [0,0,0,0,0,0,0,0,0]
        self.winner = None


    def switch_player(self):
        """
        Switch which players turn it is
        """
        if self.current_player == 1:
            self.current_player = 2
            return
        self.current_player = 1


    def is_over(self):
        """
        Test if the game has been won
        """
        winstates = ([1,1,1],[2,2,2])
        self.winner = self.current_player

        #Check if either player has all spaces in a row
        for i in range(0,9,3):
            if self.board[0+i:3+i] in winstates:
                return True

        #Check if either player has all spaces in a column
        for i in range(3):
            if self.board[0+i::3] in winstates:
                return True

        #Test if either player has the top-left to bottom-right diagonal
        if [self.board[0],self.board[4],self.board[8]] in winstates:
            return True

        #test if either player has the top-right to bottom-left diagonal
        if [self.board[2],self.board[4],self.board[6]] in winstates:
            return True

        self.winner = None
        if all(self.board) != 0:
            return True

        return False


    def play_move(self,move):
        """
        Updates board to match move
        """
        self.board[int(move)] = self.current_player


    def display_board(self):
        """
        Displays the current state of the game board
        """
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])


    def ask_for_move(self):
        """
        Allows players to input a move
        """
        print("")
        move = input(f"Player {self.current_player} to move ")

        #Ensure that the move is valid
        try:
            self.board[int(move)]
        except IndexError:
            print("Please choose a valid space")
            self.display_board()
            return

        #Ensures that players cannot take spaces that have already been taken
        if game.board[int(move)] != 0:
            print("That space has already been taken. Please select a valid move.")
            self.display_board()
            return

        return move


    def print_game_over(self):
        """
        Prints whether the game was a tie, or which player won.
        """
        if self.winner is None:
            print("The game was a tie.")
            return
        print(f"Player {self.winner} wins!")


if __name__ == "__main__":
    game = TicTacToeGame()
    game.display_board()
    while True:
        move = game.ask_for_move()

        #Restarts the current turn if the move was invalid.
        if move is None:
            continue

        game.play_move(move)
        game.display_board()

        if game.is_over():
            game.print_game_over()
            break

        #changes which players turn it is for the next turn
        game.switch_player()
