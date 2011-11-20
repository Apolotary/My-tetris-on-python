from Board import *
from Block import *
import pygame
from pygame import *

class Game:
	instance = None
	def __new__(cls, *args, **kwargs):
		if not cls.instance:
			cls.instance = super(Game, cls).__new__(cls, *args, **kwargs)
		return cls.instance

	def __init__(self, res, screen):
		self.res = res
		self.board = Board()
		self.defs = Defs()
		self.screen = screen
		self.board = self.board.new_board()
		self.block = Block(self.board)
		self.block.new_block()
		self.endgame = False
		self.score = 0
		self.scoreImageName = "./images/score.png"
		self.scoreImage = pygame.image.load(self.scoreImageName).convert()
		self.then = pygame.time.get_ticks()


	def draw_matrix(self, matrix, offset):
		#print(matrix, offset)
		off_x, off_y  = offset
		for y, row in enumerate(matrix):
			#print(y, row)
			for x, val in enumerate(row):
				#print(x, val)
				if val:
					pygame.draw.rect(
						self.screen,
						self.defs.colors[val],
						pygame.Rect(
							(off_x+x) *
							  self.defs.cell_size,
							(off_y+y) *
							  self.defs.cell_size,
							self.defs.cell_size,
							self.defs.cell_size),0)
					#print((off_x+x)*self.defs.cell_size, (off_y + y)*self.defs.cell_size)
	def Check_keys(self):
		for event in pygame.event.get():
			print("checking keys")
			if event.type == pygame.KEYDOWN:
				if not self.defs.check_collision(self.board, self.block.shape, (self.block.x, self.block.y)):
					self.score += 1
					if event.key == K_s:
						print("dropping~")
						self.block.drop()
					if event.key == K_d:
						self.block.move(1)
					if event.key == K_a:
						self.block.move(-1)
					if event.key == K_w:
						self.block.rotate_clockwise(self.block.shape)
					if event.key == K_ESCAPE:
						self.endgame = True
					if event.key == K_SPACE:
						self.score += 60
						while(not self.defs.check_collision(self.board, self.block.shape, (self.block.x, self.block.y))):
							self.block.drop()

		if not self.defs.check_collision(self.board, self.block.shape, (self.block.x, self.block.y)):
			self.now = pygame.time.get_ticks()
			if self.now - self.then > self.defs.maxfps * 8:
				self.then = self.now
				self.block.drop()

	def Run(self):
		self.Draw()

	def draw_next_block(self, matrix):
		for y, row in enumerate(matrix):
			#print(y, row)
			for x, val in enumerate(row):
				#print(x, val)
				if val:
					pygame.draw.rect(
						self.screen,
						self.defs.colors[val],
						pygame.Rect(
							300+x*self.defs.cell_size,
							self.res[1]-65+y*self.defs.cell_size,
							self.defs.cell_size,
							self.defs.cell_size),0)

	def Draw(self):
		self.board, bonus = Board().check_filled_rows(self.board)
		self.score += bonus
		#self.timer = pygame.time.Clock()
		self.scoreLabel = self.screen.blit(self.scoreImage, (60, self.res[1]-60))
		self.font_size = 48
		self.font = pygame.font.SysFont("arial", self.font_size)
		self.w, self.h = self.font.size(str(self.score))
		self.font_image = self.font.render(str(self.score), 1, (255, 255, 255))
		self.screen.blit(self.font_image, (200, self.res[1]-65))
		#print(self.block.shape, self.block.x, self.block.y)
		print("NSHAPE: ", self.block.nshape, self.block.nx, self.block.ny)
		self.draw_next_block(self.block.nshape)
		# check collision
		if not self.endgame:
			if self.defs.check_collision(self.board, self.block.shape, (self.block.x, self.block.y)):
				self.set_block(self.board, self.block.shape, (self.block.prevX, self.block.prevY))
				# if collides => make a new block
				self.block.new_block()
				print("collision!")
				if self.defs.check_collision(self.board, self.block.shape, (self.block.x, self.block.y)):
					print("endgame!")
					self.endgame = True
			else:
				# draw a block
				if not self.endgame:
					self.draw_matrix(self.block.shape, (self.block.x, self.block.y))
		# draw a board
		self.draw_matrix(self.board, (0,0))

	def set_block(self, board, shape, offset):
		print("setting a block")
		of_x, of_y = offset
		for cy, row in enumerate(shape):
			for cx, val in enumerate(row):
				if val:
					self.board[of_y + cy][of_x + cx] = val

	def Update(self, frameDeltaTime):
			self.Check_keys()
			pygame.display.update()