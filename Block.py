import random
from Defs import Defs
from Board import Board

class Block:
	def __init__(self, board):
		self.defs = Defs()
		self.board = board
		self.deltaX = 0
		self.block_shapes = [
#			[[0, 1, 0],
			[[1, 1, 1],
			 [0, 1, 0]],
#
			[[0, 2, 2],
			 [2, 2, 0]],
#            [[2, 2, 2, 0, 2],
#             [0, 0, 2, 0, 2],
#             [2, 2, 2, 2, 2],
#             [2, 0, 2, 0, 0],
#             [2, 0, 2, 2, 2]],

			[[3, 3, 0],
			 [0, 3, 3]],
#            [[3, 0, 3, 3, 3],
#             [3, 0, 3, 0, 0],
#             [3, 3, 3, 3, 3],
#             [0, 0, 3, 0, 3],
#             [3, 3, 3, 0, 3]],

			[[4, 0, 0],
			 [4, 4, 4]],
#            [[0, 4, 0],
#             [0, 4, 0],
#             [4, 4, 4],
#             [0, 4, 0]
#            ],

			[[0, 0, 5],
			 [5, 5, 5]],
#            [[0, 0, 5, 0, 0],
#             [0, 5, 0, 5, 0],
#             [0, 5, 5, 5, 0],
#             [0, 0, 5, 0, 0],
#             [0, 0, 5, 0, 0]],

			[[6, 6, 6, 6]],

			[[7, 7],
			 [7, 7]],

#            [[0, 7, 7, 0],
#             [7, 0, 0, 7],
#             [7, 0, 0, 7],
#             [7, 7, 7, 7]],

#			[[0, 8, 0],
#			 [8, 8, 8], 
#			 [0, 8, 0],
#			 [0, 8, 0]]
		]
		self.shape = self.block_shapes[random.randint(0, len(self.block_shapes) - 1)]
		self.x = int(self.defs.cols / 2 - len(self.shape[0])/2)
		self.y = 0
		self.prevX = 0
		self.prevY = 0
		self.nshape = self.block_shapes[random.randint(0, len(self.block_shapes) - 1)]
		self.nx = int(self.defs.cols / 2 - len(self.shape[0])/2)
		self.ny = 0

	def rotate_clockwise(self, shape):
		# we take each part of subarray in array
		# so that in case of L
		# we'll have
		# [5, 5]
		# [0, 5]
		# [0, 5]
		self.shape = [ [ shape[y][x] for y in range(len(shape)) ] for x in range(len(shape[0]) - 1, -1, -1) ]

	def new_block(self):
		self.shape = self.nshape
		self.x = self.nx
		self.y = self.ny
		self.nshape = self.block_shapes[random.randint(0, len(self.block_shapes) - 1)]
		self.nx = int(self.defs.cols / 2 - len(self.shape[0])/2)
		self.ny = 0

	def drop(self):
		if self.y < self.defs.rows - 1:
			self.prevY = self.y
			self.prevX = self.x
			self.y += 1
			self.deltaX = 0

	def move(self, dx):
		print("Drop!", self.x)
		if self.x > 1 and self.x < (self.defs.cols - 3) and not self.defs.check_collision(self.board, self.shape, (self.x + dx, self.y)):
			print("Drop!", self.defs.cols)
			self.prevY = self.y
			self.prevX = self.x
			self.x += dx
			self.deltaX = dx