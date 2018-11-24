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

	def is_full(self):
		if self.moves == 9:
			print("Board is full - game over!")
			exit()

	def row_winner(self):
		for i in range(3):
			if self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2]:
				return True
		return False

	def col_winner(self):
		for i in range(3):
			if self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i]:
				return True
		return False

	def diag_winner(self):
		return ((self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2]) \
		or (self.game_board[2][0] == self.game_board[1][1] == self.game_board[0][2]))

	def is_game_won(self):
		if self.row_winner() or self.col_winner() or self.diag_winner():
			print "Game Won!"
			exit()



def simple_ai(board):
	for i in range(3):
		for j in range(3):
			if board.game_board[i][j] == "-":
				board.add_move("O", i, j)
				return
	

def user_move(board):
	while True:
		print "Your turn, where would you like to move?"
		try:
			row = int(input("row: "))
			col = int(input("col: "))
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


def main():
	ongoing = True
	b = Board()
	print "\nWelcome to Tic-Tac-Toe. Make your first move"
	while ongoing:
		b.is_game_won()
		b.is_full()	
		user_move(b)
		b.is_game_won()
		b.is_full()
		simple_ai(b)
		b.print_board()


if __name__ == "__main__":
	main()


