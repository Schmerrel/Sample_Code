
#create 3x3 matrix to represent game board
	#init 3x3 matrix of 0's at start of game
#function to render gameboard after each move
	#render 1's as X's and 2's os O's
#function to add user input into the board
	#player 1 changers matrix position to 1 on their move placement. player 2 changes to 2
	#prevent invalid moves (cant move on an already used spot)
	#sub function to check for a win after each move
		#input a game state, return bool
	#replay function
#function to add usernames for each player?

import numpy as np
import random
BOARD_HEIGHT = 3
BOARD_WIDTH = 3	
cache = {}

def init_game():
	turn_count = 1
	board = []
	for x in range(0,BOARD_HEIGHT):
		board_row = []
		for y in range(0, BOARD_WIDTH):
			board_row.append(0)
		board.append(board_row)
	render(board)
	(p1, p2) = num_players()
	while(((check_win(board)) == False) and (draw_check(board) == False)):
		if (turn_count % 2 == 0):
			current_player = 2
		else:
			current_player = 1
		get_move(current_player, p1, p2, board)
		turn_count += 1
	return()



def get_move(current_player, player_1, player_2, board):
	player_functions = [human_player, get_rand_AI_move, get_winning_AI_move, get_improved_AI, ultimate_AI]
	print("Player " + str(current_player) +", your move!")
	if (current_player == 1):
		(x,y) = player_functions[player_1](board, current_player)
	elif (current_player == 2):
		(x,y) = player_functions[player_2](board, current_player)
	if(make_move(x,y,current_player, board) == False):
		get_move(current_player, player_1, player_2)
	render(board)
	if(check_win(board)):
		print("Player " + str(current_player) +" Wins! Fuckin great for you. Initiating Taint_Poke.EXE")
		play_again = input("Would you like to play again? Enter Y to start new game or any other character to exit:")
		if((play_again == "y") or (play_again == "Y")):
			init_game()
		else:
			print("Goodbye")
			return()
	elif(draw_check(board)):
		play_again = input("DRAW! Everyone's a loser. To play again enter Y, to stop playing enter any other character:")
		if (play_again == "Y" or play_again == "y"):
			init_game()
		else:
			print("Goodbye")
			return()		
	return()


def make_move(x,y, current_player, board):
	if((x > 2) or (y > 2)):
		print("Invalid move, please make sure to enter only 0, 1, or 2 for your coordinate")
		return(False)
	if((board[x][y] != 0)):
		print("Invalid move, tile already taken, select another tile.")
		return(False)
	else:
		if(current_player == 1):
			board[x][y] = 1
		elif(current_player == 2):
			board[x][y] = 2
		return(True)

def check_win(board):
	
	if(board[0][0] == board[0][1] == board[0][2] != 0):
		return(True)
	if(board[1][0] == board[1][1] == board[1][2] != 0):
		return(True)
	if(board[2][0] == board[2][1] == board[2][2] != 0):
		return(True)
	if(board[0][0] == board[1][0] == board[2][0] != 0):
		return(True)
	if(board[0][1] == board[1][1] == board[2][1] != 0):
		return(True)
	if(board[0][2] == board[1][2] == board[2][2] != 0):
		return(True)
	if(board[0][0] == board[1][1] == board[2][2] != 0):
		return(True)
	if(board[2][0] == board[1][1] == board[0][2] != 0):
		return(True)
	else:
		return(False)

def render(board):
	print("   0   1   2")
	render_board = []
	for x,row in enumerate(board):
		render_board_row = []
		render_board_row.append(str(x) + "|")
		for y,col in enumerate(row):
			if(board[x][y] == 0):
				render_board_row.append("   |")
			if(board[x][y] == 1):
				render_board_row.append(" X |")
			if(board[x][y] == 2):
				render_board_row.append(" O |")
		print(''.join(render_board_row))
		render_board.append(render_board_row)
	return()

def draw_check(board):
	open_tile_count = 0
	for x,row in enumerate(board):
		for y,col in enumerate(row):
			if (board[x][y] == 0):
				open_tile_count += 1
	if (open_tile_count > 0):
		return(False)
	else:
		return(True)

def num_players():
	player_1 = int(input("Select a 1st player: 0-human, 1-randomAI, 2-winningAI, 3-improvedAI, 4-UltimateAI: "))
	player_2 = int(input("Select a 2nd player: 0-human, 1-randomAI, 2-winningAI, 3-improvedAI, 4-UltimateAI: "))
	return(player_1, player_2)

def get_rand_AI_move(board, current_player):
	AI_board = np.zeros((3,3))
	open_tile_count = 1
	for x,row in enumerate(board):
		for y,col in enumerate(row):
			if (board[x][y] == 0):
				AI_board[x][y] = open_tile_count
				open_tile_count += 1
	AI_move = random.randint(1,(open_tile_count - 1))
	for x, AI_row in enumerate(AI_board):
		for y, AI_col in enumerate(AI_row):
			while(AI_board[x][y] == AI_move):
				return(x,y)

def get_winning_AI_move(board, current_player):
	AI_board = make_AI_board(board)	#fill AI board with current board state
	for x,row in enumerate(board):
		for y,col in enumerate(row):
			if(AI_board[x][y] == 0):
				AI_board[x][y] = current_player
				if(check_win(AI_board)):
					return(x,y)
				else:
					AI_board[x][y] = 0				
	(x,y) = get_rand_AI_move(board, current_player)
	return(x,y)

def get_improved_AI(board, current_player):
	AI_board = make_AI_board(board)
	for x, row in enumerate(board):
		for y, col in enumerate(row):
			if(AI_board[x][y] == 0):
				(AI_board[x][y]) = current_player
				if(check_win(AI_board)):
					print("Found a winning move!")
					print(x,y)
					return(x,y)
				AI_board[x][y] = get_opponent(current_player)
				if(check_win(AI_board)):
					print("Blocked a winning move!")
					print(x,y)
					return(x,y)
				else:
					AI_board[x][y] = 0
	print("Couldn't find or block a win")
	(x,y) = get_rand_AI_move(board, current_player)
	return(x,y)

def get_minimax_score(board_state, move_player, optimize_player):
	#minimax Pseudocode
	#asssume AI is player 1 (X)
	#check through all legal open spaces for a terminal state
	#assign -10 if O wins, +10 if X wins
	#if open space is not a terminal state, reursively iterate through all possible moves from that state
	if check_win(board_state):
		if (move_player == optimize_player):
			return -10
		else:
			return 10
	elif draw_check(board_state):
		return 0
	scores = [] 
	legal_moves = get_open_moves(board_state)
	for move in legal_moves:
		AI_board = make_AI_board(board_state)
		(AI_x, AI_y) = move
		make_move(AI_x, AI_y, move_player, AI_board)
		board_key = str(AI_board)
		if board_key not in cache:
			opponent = get_opponent(move_player)
			score = get_minimax_score(AI_board, opponent, optimize_player)
			cache[board_key] = score
		else:
			score = cache[board_key]
		scores.append(score)
	if move_player == optimize_player:
		return (max(scores))
	else:
		return (min(scores))

def ultimate_AI(board, current_player):
	AI_move = None
	AI_Max_Score = None
	optimize_player = current_player
	scores = []
	legal_moves = []
	legal_moves = get_open_moves(board)
	for move in legal_moves:
		AI_board = make_AI_board(board)
		(AI_x, AI_y) = move
		make_move(AI_x, AI_y, current_player, AI_board)
		opponent = get_opponent(current_player)
		score = get_minimax_score(AI_board, opponent, optimize_player)
		scores.append(score)
		if ((AI_Max_Score == None) or (score > AI_Max_Score)):
			AI_Max_Score = score
			AI_move = move
	(x,y) = AI_move
	return(x,y)


def make_AI_board(board):
	AI_board = np.zeros((3,3))
	for x,row in enumerate(board):
		for y,col in enumerate(row):
			AI_board[x][y] = board[x][y]
	return(AI_board)

def get_open_moves(board):
	legal_moves =[]
	for x,row in enumerate(board):
		for y,col in enumerate(row):
			if board[x][y] == 0:
				legal_moves.append((x,y))
	return(legal_moves)

def human_player(board, current_player):
	y = int(input("Please enter the X coordinate of your move:"))
	x = int(input("Please enter the Y coordinate of your move:"))
	return(x,y)

def get_opponent(current_player):
	if current_player == 1:
		return 2
	elif current_player == 2:
		return 1


#test_board = [[1,2,1],
#			  [0,2,0],
#			  [0,0,0]]
#move = ultimate_AI(test_board, 1)
#print(move)
init_game()
