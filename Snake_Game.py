'''								Grid Based Snake Game 													'''

'''	
	TODO:
		-Create nested lists to form a grid and put a starting position in it
		-Create pygame window to represent that grid graphically with the snake (Black and White)
		-Add player controls to the snake
		-Snake continues moving in the same direction the players last input pointed to
		-If snake 'head' touches any other part of snake body or edges of map the game ends
			(Make sure only snake head because I think game will end just by snake motion since its
			 parts follow eachother and depending which way it moves because its rendered top down)
		-Randomly put food every few seconds after previous food is eaten by the snake and eating food
			will make the snake grow.
		-Implement some sort of UI and endscreen when game ends
		-Add the ability to choose size of map
		-Ability to choose snake speed
		-Ability to choose amount of food that can exist at one time on the map
'''



import pygame



	# Define COLOURS
WHITE = (255,255,255)
BLACK = (0  ,0  ,0  )
GREEN = (0  ,255,0  )
RED   = (255,0  ,0  )
BLUE  = (0  ,0  ,255)

#____________________SET PARAMETERS____________________
	# Set FPS
FPS = 60
	# Set GRID BLOCK size
BLOCK_SIZE = 10 #_________Size of the individual square in grid
	# Set SNAKE colour
SNAKE_COL  = WHITE
	# Set SNAKE speed
SNAKE_VEL  = 10
	# Set GRID colour
GRID_COL   = BLACK
	# Set GRID size
GRID_SIZE  = 15
	# Set FOOD rate
FOOD_RATE  = 1
	# Set FOOD colour
FOOD_COL   = GREEN
	# Set CONTROLS type
CONTROLS   = 0 #___________Control type 0 = arrows, 1 = WASD
	



class Snake:

	grid = []

		# Initializing all the parameters as default so class doesn't need to have arguments when called
	def __init__(self, grid_size = GRID_SIZE, snake_speed = SNAKE_VEL, food_rate = FOOD_RATE, \
			 	controls_type = CONTROLS, fps = FPS, snake_colour = SNAKE_COL, grid_colour = GRID_COL, \
			 	food_colour = FOOD_COL, block_size = BLOCK_SIZE):

		self.grid_size     = grid_size
		self.snake_speed   = snake_speed
		self.food_rate     = food_rate
		self.controls_type = controls_type
		self.fps           = fps
		self.snake_colour  = snake_colour
		self.grid_colour   = grid_colour
		self.food_colour   = food_colour

		# Creating nested lists filled with values 0(inactive) and one 1(active)
		# Value 1 represents the starting point in grid for player
	def create_grid(self):
		for i in range(self.grid_size):
			sub_grid = []
			for j in range(self.grid_size):
				sub_grid.append(0)

			self.grid.append(sub_grid)
			# Set value 1 in the middle of the middle of grid
		self.grid[self.grid_size//2][self.grid_size//2] = 1
	
	





