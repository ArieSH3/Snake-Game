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
import time


# Define COLOURS
WHITE    = (255,255,255)
BLACK    = (0  ,0  ,0  )
GREY     = (15 ,15 ,15 )
GREEN    = (0  ,255,0  )
RED      = (255,0  ,0  )
BLUE     = (0  ,0  ,255)
TURQOISE = (0  ,230,153)
ORANGE   = (226,152,  4)

# ____________________SET PARAMETERS____________________
# Set FPS
FPS = 10
# Set GRID BLOCK size
BLOCK_SIZE = 50  # 60 #_________Size of the individual square in grid
# Set SNAKE head colour
SNAKE_COL_1 = WHITE
# Set SNAKE body colour
SNAKE_COL_2 = TURQOISE
# Set GRID_1 colour
GRID_COL_1 = BLACK
# Set GRID_2 colour
GRID_COL_2 = GREY
# Set GRID size
GRID_SIZE = 20  # 15
# Set FOOD rate
#FOOD_RATE = 1 		################# NOT USED YET (Supposed to determine how many food elements on grid at one time)
# Set FOOD colour
FOOD_COL = ORANGE
# Set CONTROLS type
CONTROLS = 0  # ___________Control type 0 = arrows, 1 = WASD

# Set WINDOW size (Not yet optimized to be changed by user)
WIN_SIZE = GRID_SIZE * BLOCK_SIZE


pygame.init()
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()


class Snake:

	# Initializing all the parameters as default so class doesn't need to have arguments when called
	def __init__(
		self,
		grid_size=GRID_SIZE,
		controls_type=CONTROLS,
		fps=FPS,
		snake_colour_1=SNAKE_COL_1,
		snake_colour_2=SNAKE_COL_2,
		grid_colour_1=GRID_COL_1,
		grid_colour_2=GRID_COL_2,
		food_colour=FOOD_COL,
		block_size=BLOCK_SIZE
		#game_display = (480, 480)
	):

		self.grid_size = grid_size
		self.controls_type = controls_type
		self.fps = fps
		self.snake_colour_1 = snake_colour_1
		self.snake_colour_2 = snake_colour_2
		self.grid_colour_1 = grid_colour_1
		self.grid_colour_2 = grid_colour_2
		self.food_colour = food_colour
		self.block_size = block_size

		self.positions = [((self.grid_size//2),(self.grid_size//2))]
		self.snake_length = 2
		self.food = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
		self.score = 0

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

		# Moves snake head and following parts
	def move_snake(self):
		new = self.positions[0]
		
		if self.direction == self.right:
			new = (new[0]+1,new[1])
		elif self.direction == self.left:
			new = (new[0]-1,new[1])
		elif self.direction == self.up:
			new = (new[0],new[1]-1)
		elif self.direction == self.down:
			new = (new[0],new[1]+1)

			# Inserts new head position to first place in list
		self.positions.insert(0, new)
			# If snake length doesnt match the current number of elements in snake it removes last element
			# That is how snake follows head.
		if len(self.positions) > self.snake_length:
			self.positions.pop()

			# Check if food in same spot as snake head
		if self.food == self.positions[0]:
			self.score += 1
			self.snake_length += 1
			self.place_food()


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

		# Draws snake on grid
	def draw_snake(self):
		for pos in self.positions:
			rect = pygame.Rect((pos[0]*self.block_size, pos[1]*self.block_size), (self.block_size, self.block_size))
			pygame.draw.rect(screen, self.snake_colour_2, rect)

		# Draws food on grid
	def draw_food(self):
		rect = pygame.Rect((self.food[0]*self.block_size, self.food[1]*self.block_size), (self.block_size, self.block_size))
		pygame.draw.rect(screen, self.food_colour, rect)		

		# Handles key inputs
	def handle_keys(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT and self.direction != self.left:
					self.direction = self.right
					#print('right')
				if event.key == pygame.K_LEFT and self.direction != self.right:
					self.direction = self.left
					#print('left')
				if event.key == pygame.K_UP and self.direction != self.down:
					self.direction = self.up
					#print('up')
				if event.key == pygame.K_DOWN and self.direction != self.up:
					self.direction = self.down
					#print('down')

		# Check for self and border collision
	def is_collision(self):
		# If hits boundary
		if self.positions[0][0] >= self.grid_size or self.positions[0][0] < 0:
			return True
		elif self.positions[0][1] >= self.grid_size or self.positions[0][1] < 0:
			return True

		# If hits self
		if self.positions[0] in self.positions[1:]:
			return True

		#print(self.grid_size-1)

		return False

		# Place food on grid
	def place_food(self):
		x = random.randint(0,self.grid_size-1)
		y = random.randint(0,self.grid_size-1)
		self.food = (x,y)
		# If food position in snake position then call again for another random position
		if self.food in self.positions:
			self.place_food()

def main():
	snake = Snake()
	
	while True: 
		snake.draw_grid()
		snake.handle_keys()
		snake.move_snake()
		snake.draw_snake()
		snake.draw_food()

		pygame.display.update()
		clock.tick(FPS)

		# If collides with self or wall then game over
		if snake.is_collision():
			print("GAME OVER!")
			pygame.quit()
			time.sleep(2)
			sys.exit()

if __name__ == '__main__':
	main()