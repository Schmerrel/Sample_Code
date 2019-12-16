import numpy as np
import random



def random_state(height, width):
	board_state = np.zeros(shape = (height, width))
	new_board = []
	for row in board_state:
		new_board_row = []
		for cell in row:	
			rand_num = random.random()
			if rand_num <= 0.7:
				cell = 0
			else:
				cell = 1
			new_board_row.append(cell)
		new_board.append(new_board_row)
	return(new_board)

def render(board_state):
	board_top = []
	for col in board_state[0]:
		board_top.append(" ~")
	print (''.join(board_top))
	render_board = []
	for row in board_state:
		render_board_row = ["|"]
		for cell in row:
			if cell == 1:
				render_board_row.append("# ")
			else:
				render_board_row.append("  ")
		render_board_row.append("|")
		print(''.join(render_board_row))
		render_board.append(render_board_row)
	print(''.join(board_top))

def get_next_board_state(board_state):
	next_board = []
	for x, row in enumerate(board_state):
		next_board_row = []
		for y, col in enumerate(row):
			live_count = 0
			if (board_state[x-1][y] == 1) and (x>=1):
				live_count = live_count + 1
			if (board_state[x-1][y-1] == 1) and (x>=1) and (y>=1):
				live_count = live_count + 1
			if (board_state[x][y-1] == 1) and (y>=1): 
				live_count = live_count +1
			if (y>=1) and (x <= (len(board_state) - 2)):
				if (board_state[x+1][y-1] == 1):
					live_count = live_count +1
			if (x <= (len(board_state) - 2)):
				if (board_state[x+1][y] == 1):
					live_count = live_count +1
			if (x <= (len(board_state) - 2)) and (y <= (len(board_state[0]) - 2)):	
				if board_state[x+1][y+1] == 1:
					live_count = live_count +1
			if (y <= (len(board_state[0]) - 2)):
				if board_state[x][y+1] == 1:
					live_count = live_count +1
			if (y <= (len(board_state[0]) - 2)) and (x >= 1):
				if board_state[x-1][y+1] == 1:
					live_count = live_count +1
			
			if (board_state[x][y] == 1) and (live_count == 1 or live_count == 0):
				next_board_row.append(0)
				
			if (board_state[x][y] == 1) and (live_count == 2 or live_count == 3):
				next_board_row.append(1)
				
			if (board_state[x][y] == 1) and (live_count > 3):
				next_board_row.append(0)
				
			if (board_state[x][y] == 0) and (live_count == 3):
				next_board_row.append(1)
			
			if (board_state[x][y] == 0) and (live_count != 3):
				next_board_row.append(0)

		next_board.append(next_board_row)
	render(next_board)
	get_next_board_state(next_board)
	return(next_board)

board = random_state(20,20)
render(board)
board = get_next_board_state(board)
render(board)
