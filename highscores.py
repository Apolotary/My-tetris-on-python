from statemanager import *
class HighScores:
	instance = None
	def __new__(cls, *args, **kwargs):
		if not cls.instance:
			cls.instance = super(HighScores, cls).__new__(cls, *args, **kwargs)
		return cls.instance

	def __init__(self, res, screen):
			self.res = res
			self.screen = screen
			self.scorem = ScoreManager()
			self.scorem.loadTheData()
			self.scoreBack = False
			self.place, self.name, self.score = self.scorem.returnAllScores()
			self.logo_imagename = "./images/highscores.png"

			self.logoImage = pygame.image.load(self.logo_imagename).convert()

	def printAllScores(self):
		self.scorem.loadTheData()
		print(len(self.score))
		for i in range(len(self.score)):
			scorestring = str(self.place[i]) + "   " + self.name[i] + "   " + str(self.score[i])
			self.font_size = 30
			self.font = pygame.font.SysFont("arial", self.font_size)
			self.w, self.h = self.font.size(scorestring)
			self.font_image = self.font.render(scorestring, 1, (255, 255, 255))
			self.screen.blit(self.font_image, (120, 250 + i * 35))

	def getKeys(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				keyname = pygame.key.name(event.key)
				print(event.key, keyname)
				if keyname == "return":
					# write to file here
					# call gamemenu
					print("ENTEER")
					self.scoreBack = True

	def Draw(self):
		self.screen.fill((0,0,0))
		self.getKeys()
		self.logo = self.screen.blit(self.logoImage, (80, 60))
		self.printAllScores()


	def Update(self, frameDeltaTime):
		pygame.display.update()
