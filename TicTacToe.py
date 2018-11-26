# Simple Tic Tac Toe Game

class Board:
	def __init__(self):
		self.game_board = [["-","-","-"],["-","-","-"],["-","-","-"]]
		self.moves = 0

	def print_board(self):
		print "  1 2 3"
		for i in range(3):
			print str(i+1) + " " + "|".join(self.game_board[i])
		print ""

	def add_move(self, move, r, c):
		self.game_board[r][c] = move
		self.moves += 1
		self.check_board(move)

	def row_winner(self, move):
		for i in range(3):
			if self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2] == move:
				return True
		return False

	def col_winner(self, move):
		for i in range(3):
			if self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i] == move:
				return True
		return False

	def diag_winner(self, move):
		return (self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == move) \
		or (self.game_board[2][0] == self.game_board[1][1] == self.game_board[0][2] == move)

	def is_game_won(self, move):
		return self.row_winner(move) or self.col_winner(move) or self.diag_winner(move)
			
	def is_full(self):
		return self.moves == 9

	def check_board(self, move):
		if self.is_full() and not self.is_game_won():
			print "\nTie! The Board is full - game over!"
			self.print_board()
			exit()
		elif self.is_game_won(move):
			winner = player_name if move == "X" else "AI"
			print "\nGame over - " + winner + " wins!!!"
			self.print_board()
			exit()
		
			
def simple_ai(board):
	print "\nAI's move:"
	for i in range(3):
		for j in range(3):
			if board.game_board[i][j] == "-":
				board.add_move("O", i, j)
				return

# Method to 	
def user_move(board):
	while True:
		print "Your turn, where would you like to move?"
		try:
			row = int(raw_input("row: "))
			col = int(raw_input("col: "))
		except NameError:
			print("Must use integers to play tic tac toe!")
			continue

		if row < 1 or row > 3 or col < 1 or col > 3 or board.game_board[row-1][col-1] != "-":
			print("Invalid row or column, retry")
			continue
		else:
			board.add_move("X", row-1, col-1)
			board.print_board()
			return

# Global Variables
player_name = "user"


# Main game loop
if __name__ == "__main__":
	player_name = str(raw_input("\nWelcome to Tic-Tac-Toe. What is your name: ")).capitalize()
	b = Board()
	b.print_board()
	ongoing = True
	while ongoing:
		user_move(b)
		simple_ai(b)
		b.print_board()

