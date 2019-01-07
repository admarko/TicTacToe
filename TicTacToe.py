'''
Simple Tic Tac Toe game that lets users play in Terminal vs. 3 different AIs
By Alex Markowitz
github.com/admarko/TicTac/Toe
Last Modified January 2019
'''
import random

#############################
#### Board Class ####
#############################
class Board:
	def __init__(self):
		self.game_board = [["-","-","-"],["-","-","-"],["-","-","-"]]
		self.moves = 0
		self.player_score = [0,0,0]
		self.ai_score = [0,0,0]
		self.leader = ""
		self.is_game_over = False
	
	def print_board(self):
		print "  1 2 3"
		for i in range(3):
			print str(i+1) + " " + "|".join(self.game_board[i])
		print ""

	def reset_board(self):
		self.game_board = [["-","-","-"],["-","-","-"],["-","-","-"]]
		self.moves = 0
		self.is_game_over = False

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

	def assign_current_leader(self):
		if self.player_score[0] > self.ai_score[0]:
			self.leader = player_name
		elif self.player_score[0] < self.ai_score[0]:
			self.leader = "AI"
		else:
			self.leader = ""

	def update_scores(self, move):
		if move == "X":
			self.player_score[0] += 1		# player win
			self.ai_score[1] += 1			# ai lose
			round_winner = player_name
		elif move == "O":
			self.ai_score[0] += 1			# ai win
			self.player_score[1] += 1		# player lose
			round_winner = "AI"		
		else:
			self.ai_score[2] += 1
			self.player_score[2] += 1
			return
			
		return round_winner

	def end_of_game(self):
		while True:
			answer = str(raw_input("Would you like to play again? [Y/N]: ")).capitalize()
			if answer == "N":
				print "*Final score* "
				print "{}: {}-{}-{}".format(player_name, self.player_score[0], self.player_score[1], self.player_score[2])
				print "AI: {}-{}-{}".format(self.ai_score[0], self.ai_score[1], self.ai_score[2])
				print self.leader + " wins!\n" if self.leader else "Tie - Everyone's a winner!"
				exit()
			elif answer == "Y":
				self.reset_board() # loser starts next game
				break
			else:
				print("Invalid option, please select either [Y] for Yes or [N] for No")



	def check_board(self, move):
		if self.is_full() and not self.is_game_won(move):
			print "\nTie! The Board is full - game over!"
			self.print_board()
			self.player_score[2] += 1
			self.ai_score[2] += 1
			self.update_scores("Tie")
			print "This round ends in a Tie!"
			self.is_game_over = True

		elif self.is_game_won(move):
			round_winner = self.update_scores(move)
			self.print_board()
			print round_winner + " wins this round!"
			self.assign_current_leader()
			self.is_game_over = True

		if self.is_game_over:
			self.end_of_game()
		
#############################
#### AI Methods #############
#############################
	
# Helper for Minimax algo for the Unbeatable AI
def evaluate(board):
	if board.is_game_won("O"):
		return 10
	elif board.is_game_won("X"):
		return -10
	return 0


# Minimax algorithm (helper for the unbeatable AI)
# Help from: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
def minimax(board, depth, isMax):
	score = evaluate(board)

	#maximizer wins, return evaluated score
	if score == 10:				
		return score
	
	#minimizer won, return evaluated score
	if score == -10:
		return score 			
	
	# if no more moves and no winner, then its a tie
	if board.is_full():			
		return 0

	# if this is maximizer's move
	if isMax:
		best = -1000
		for i in range(3):
			for j in range(3):
				if board.game_board[i][j] == "-":
					board.game_board[i][j] = "X"
					best = max(best, minimax(board, depth+1, not isMax))
					board.game_board[i][j]= "-"
		return best

	else:	# the minimizer's move
		best = 1000
		for i in range(3):
			for j in range(3):
				if board.game_board[i][j] == "-":
					board.game_board[i][j] = "O"
					best = min(best, minimax(board, depth+1, not isMax))
					board.game_board[i][j] = "-"
		return best

# Choose which AI to play against based on user input
def get_ai_type(ai_name):

	# Iteratively scrolls from top left to bottom right corner and moves in the next
	# open spot	
	def simple_ai(board):
		print "\nSimple AI's move:"
		for i in range(3):
			for j in range(3):
				if board.game_board[i][j] == "-":
					board.add_move("O", i, j)
					board.print_board()
					return

	# AI that randomly places valid move
	def random_ai(board):
		print "\nRandom AI's move:"
		while True:
			row = random.randint(0,2)
			col = random.randint(0,2)
			if board.game_board[row][col] == "-":
				board.add_move("O", row, col)
				board.print_board()
				return

	def unbeatable_ai(board):
		print "\nUnbeatable AI's move:"
		best_value = float('-inf')
		best_move_row = -1
		best_move_col = -1

		for i in range(3):
			for j in range(3):
				if board.game_board[i][j] == "-":
					board.game_board[i][j] = "O" 
	                move_value = minimax(board, 0, False)
	                board.game_board[i][j] = '-'

	                if (move_value > best_value):
	                    best_move_row = i 
	                    best_move_col = j
	                    best_value = move_value

		board.add_move("O", best_move_row, best_move_col)
		board.print_board()
		return 
              


	if ai_name == "random_ai":
		return random_ai
	elif ai_name == "unbeatable_ai":
		return unbeatable_ai
	else:
		return simple_ai



#############################
#### User + Main Methods ####
#############################

# Method to 	
def user_move(board):
	while True:
		print "It's your turn, where would you like to move?"
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

def select_opponent():
	while "Invalid Response":
		ai_input = str(raw_input("\nWhich AI do you want to play against? Random, Simple, or Unbeatable [R/S/U]: \n")).capitalize()
		if ai_input == "R":
			return "random_ai"
		elif ai_input == "S":
			return "simple_ai"
		elif ai_input == "U":
			return "unbeatable_ai"
		else:
			print("Invalid option, please select either [R] for Random, [S] for Simple or [U] Unbeatable")

# Main game loop
if __name__ == "__main__":
	player_name = str(raw_input("\nWelcome to Tic-Tac-Toe. What is your name: \n")).capitalize()
	ai_name = select_opponent()
	ai_move = get_ai_type(ai_name)
	b = Board()
	print "\nHi " + player_name + ", you get to start"
	b.print_board()
	while True:
		user_move(b)
		ai_move(b)
