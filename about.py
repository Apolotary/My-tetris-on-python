from statemanager import *
class About:
	instance = None
	def __new__(cls, *args, **kwargs):
		if not cls.instance:
			cls.instance = super(About, cls).__new__(cls, *args, **kwargs)
		return cls.instance

	def __init__(self, res, screen):
			self.res = res
			self.screen = screen
			self.aboutBack = False
			self.logo_imagename = "./images/about_g.png"

			self.logoImage = pygame.image.load(self.logo_imagename).convert()
        
	def getKeys(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				keyname = pygame.key.name(event.key)
				print(event.key, keyname)
				if keyname == "return":
					# write to file here
					# call gamemenu
					print("ENTEER")
					self.aboutBack = True

	def Draw(self):
		self.screen.fill((0,0,0))
		self.getKeys()
		self.logo = self.screen.blit(self.logoImage, (0, 0))


	def Update(self, frameDeltaTime):
		pygame.display.update()
