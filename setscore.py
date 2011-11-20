import pygame
from pygame.locals import *
from statemanager import *
from scoremanager import *

class SetScore:
	instance = None
	def __new__(cls, *args, **kwargs):
		if not cls.instance:
			cls.instance = super(SetScore, cls).__new__(cls, *args, **kwargs)
		return cls.instance

	def __init__(self, res, screen):
		self.res = res
		self.screen = screen
		self.tscore = 0
		self.nameString = "__________"
		self.currplace = 0
		self.bspressed = False
		self.scorem = ScoreManager()
		#self.scorem.loadTheData()
		self.scoreSet = False

		# speed1 button names
		self.logo_imagename = "./images/endgame.png"

		self.logoImage = pygame.image.load(self.logo_imagename).convert()

	def setScore(self, score):
		self.score = score

	def printScore(self):
		scorestring = str("Your score: " + str(self.score))
		self.font_size = 48
		self.font = pygame.font.SysFont("arial", self.font_size)
		self.w, self.h = self.font.size(scorestring)
		self.font_image = self.font.render(scorestring, 1, (255, 255, 255))
		self.screen.blit(self.font_image, (100, self.res[1]/2))

	def printName(self):
		self.font_size = 48
		self.font = pygame.font.SysFont("arial", self.font_size)
		self.w, self.h = self.font.size(self.nameString)
		self.font_image = self.font.render(self.nameString, 1, (255, 255, 255))
		self.screen.blit(self.font_image, (130, self.res[1]/2 - 60))

	def insert(self, original, new, pos):
		#Inserts new inside original at pos
		return original[:pos] + new + original[pos:]

	def replace(self, original, new, pos):
		#Inserts new inside original at pos
		return original[:pos] + new + original[pos + 1:]

	def getKeys(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				keyname = pygame.key.name(event.key)
				print(event.key, keyname)
				if not len(keyname) > 1 and self.currplace < len(self.nameString) and self.nameString[len(self.nameString) - 1] == "_":
					if self.bspressed and self.currplace != 0:
						self.currplace += 1
					self.nameString = self.replace(self.nameString, keyname, self.currplace)
					self.currplace += 1
					self.bspressed = False
					if self.currplace > len(self.nameString) - 1:
						self.currplace = len(self.nameString) - 1
				elif keyname == "backspace" and self.currplace >= 0:
					self.nameString = self.replace(self.nameString, "_", self.currplace)
					self.bspressed = True
					self.currplace -= 1
					if self.currplace == -1:
						self.currplace = 0
				elif keyname == "return":
					# write to file here
					# call gamemenu
					print("ENTEER")
					self.scorem.addScore(self.nameString, self.score)
					self.scoreSet = True
				print(self.nameString)

	def Draw(self):
		self.screen.fill((0,0,0))
		self.getKeys()
		self.logo = self.screen.blit(self.logoImage, (80, 60))
		self.printName()
		self.printScore()


	def Update(self, frameDeltaTime):
		pygame.display.update()
