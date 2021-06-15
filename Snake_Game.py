"""								Grid Based Snake Game 													"""

"""	
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
"""


import pygame
import sys
import random


# Define COLOURS
WHITE = (255,255,255)
BLACK = (0  ,0  ,0  )
GREY  = (15 ,15 ,15 )
GREEN = (0  ,255,0  )
RED   = (255,0  ,0  )
BLUE  = (0  ,0  ,255)

# ____________________SET PARAMETERS____________________
# Set FPS
FPS = 10
# Set GRID BLOCK size
BLOCK_SIZE = 50  # 60 #_________Size of the individual square in grid
# Set SNAKE colour
SNAKE_COL = WHITE
# Set SNAKE speed
SNAKE_VEL = 10
# Set GRID_1 colour
GRID_COL_1 = BLACK
# Set GRID_2 colour
GRID_COL_2 = GREY
# Set GRID size
GRID_SIZE = 20  # 15
# Set FOOD rate
FOOD_RATE = 1
# Set FOOD colour
FOOD_COL = GREEN
# Set CONTROLS type
CONTROLS = 0  # ___________Control type 0 = arrows, 1 = WASD

# Set WINDOW size (Not yet optimized to be changed by user)
WIN_SIZE = GRID_SIZE * BLOCK_SIZE


pygame.init()
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))

clock = pygame.time.Clock()


class Snake:

	# Initializing all the parameters as default so class doesn't need to have arguments when called
	def __init__(
		self,
		grid_size=GRID_SIZE,
		snake_speed=SNAKE_VEL,
		food_rate=FOOD_RATE,
		controls_type=CONTROLS,
		fps=FPS,
		snake_colour=SNAKE_COL,
		grid_colour_1=GRID_COL_1,
		grid_colour_2=GRID_COL_2,
		food_colour=FOOD_COL,
		block_size=BLOCK_SIZE
		#game_display = (480, 480)
	):

		self.grid_size = grid_size
		self.snake_speed = snake_speed
		self.food_rate = food_rate
		self.controls_type = controls_type
		self.fps = fps
		self.snake_colour = snake_colour
		self.grid_colour_1 = grid_colour_1
		self.grid_colour_2 = grid_colour_2
		self.food_colour = food_colour
		self.block_size = block_size

		self.positions = [((self.grid_size/2),(self.grid_size/2))]
		self.snake_length = 2

		self.right = 1
		self.left  = 2
		self.up	   = 3
		self.down  = 4
			# Initial snake direction
		self.direction = random.choice([self.right, self.left, self.up, self.down])
			# Size of the game window
		#self.screen = pygame.display.set_mode()
			# Size of the playable area
		#self.game_display = game_display


	def move_head(self):
		x = self.positions[0][0]
		y = self.positions[0][1]

		if self.direction == self.right:
			x += self.block_size
		elif self.direction == self.left:
			x -= self.block_size
		elif self.direction == self.up:
			y -= self.block_size
		elif self.direction == self.down:
			y += self.block_size

		self.positions.insert(0, (x,y))
		

	def move_snake(self):
		pass

		# Drawing a grid in pygame
	def draw_grid(self):
		for y in range(self.grid_size):
			for x in range(self.grid_size):
				rect = pygame.Rect((x*self.block_size, y*self.block_size), (self.block_size, self.block_size))
					# This if/else used to create a checkered grid
				if (x+y)%2 == 0:
					pygame.draw.rect(screen, self.grid_colour_1, rect)
				else:
					pygame.draw.rect(screen, self.grid_colour_2, rect)

	def draw_snake(self):
		for pos in self.positions:
			rect = pygame.Rect((pos[0]*self.block_size, pos[1]*self.block_size), (self.block_size, self.block_size))
			pygame.draw.rect(screen, self.snake_colour, rect)

	def handle_keys(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT and self.direction != self.left:
					self.direction = self.right
				if event.key == pygame.K_LEFT and self.direction != self.right:
					self.direction = self.left
				if event.key == pygame.K_UP and self.direction != self.down:
					self.direction = self.up
				if event.key == pygame.K_DOWN and self.direction != self.up:
					self.direction = self.down




def main():
	snake = Snake()
	
	while True:
		snake.draw_grid()
		snake.draw_snake()
		snake.handle_keys()
		snake.move_head()

		pygame.display.update()


main()