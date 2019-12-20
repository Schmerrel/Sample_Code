#SNAAAAKEman

class Snake:
	def __init__(self, init_body, init_direction):
		self.direction = init_direction
		self.body = init_body

	def step(self, pos):
		new_head_pos = self.body[0] + pos
		for x,length in self.body:
			if x == 0:
				continue
			self.body[x] = self.body[x-1]
		self.body[0] = new_head_pos

	def set_direction(self, direction):
		self.direction = direction

	def get_head(self):
		head = self.body[0]



class Apple:{}

class Game:
	def __init__(self, height, width):
		self.height = height
		self.width = width
		
	
	def render(self):
		matrix = [[None for y in range(self.width)] for x in range(self.height)]
		topper = ["+-"]
		render_board = []
		for x in range(self.width):
			topper.append("--")
		topper.append("-+")
		print(''.join(topper))
		for x in range(self.height):
			board_row = []
			board_row.append("| ")
			for y in range(self.width):
				if (matrix[x][y] == None):
					board_row.append("  ")
			board_row.append(" |")
			print(''.join(board_row))
			render_board.append(board_row)
		print(''.join(topper))

		


game = Game(10,20)

game.render()