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
	# Set SNAKE colour
SNAKE_COL = WHITE
	# Set SNAKE speed
SNAKE_VEL = 10
	# Set GRID colour
GRID_COL  = BLACK
	# Set GRID size
GRID_SIZE = 15
	# Set FOOD rate
FOOD_RATE = 1
	# Set CONTROLS type
CONTROLS  = 0 #___________Control type 0 = arrows, 1 = WASD
	

pygame.init()

class Snake:
	def _init__(self, grid_size = 15, snake_speed = 10, food_rate = 1, controls_type = 0):
		self.grid_size = grid_size
		self.snake_speed = snake_speed
		self.food_rate = food_rate
		self.controls_type = controls_type
	

	





