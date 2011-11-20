import pygame
from pygame.locals import *
from statemanager import *

class SettingsMenu:
    instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(SettingsMenu, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self, res, screen):
        self.res = res
        self.screen = screen
        self.MousePos()

        # speed1 button names
        self.speed1_imagename = "./images/speed1.png"
        self.speed1_pres_imagename = "./images/speed1_pres.png"

        # speed2 button names
        self.speed2_imagename = "./images/speed2.png"
        self.speed2_pres_imagename = "./images/speed2_pres.png"

        # speed3 button names
        self.speed3_imagename = "./images/speed3.png"
        self.speed3_pres_imagename = "./images/speed3_pres.png"

        self.logo_imagename = "./images/speed_logo.png"

        self.speed1Image = pygame.image.load(self.speed1_imagename).convert()
        self.speed1Image_pres = pygame.image.load(self.speed1_pres_imagename).convert()

        self.speed2Image = pygame.image.load(self.speed2_imagename).convert()
        self.speed2Image_pres = pygame.image.load(self.speed2_pres_imagename).convert()

        self.speed3Image = pygame.image.load(self.speed3_imagename).convert()
        self.speed3Image_pres = pygame.image.load(self.speed3_pres_imagename).convert()

        self.logoImage = pygame.image.load(self.logo_imagename).convert()

    def Draw(self):
        self.screen.fill((0,0,0))
        self.speed1 = self.screen.blit(self.speed2Image, (150, self.res[1]/2 + 60))
        self.speed2 = self.screen.blit(self.speed1Image, (120, self.res[1]/2))
        self.speed3 = self.screen.blit(self.speed3Image, (165, self.res[1]/2 + 120))
      #  self.logo = self.screen.blit(self.logoImage, (80, self.res[1]/2))

        if self.speed1.collidepoint(self.mouse_pos):
            self.screen.blit(self.speed2Image_pres, (150, self.res[1]/2 + 60))
        else:
            self.screen.blit(self.speed2Image, (150, self.res[1]/2 + 60))

        if self.speed2.collidepoint(self.mouse_pos):
            self.screen.blit(self.speed1Image_pres, (120, self.res[1]/2))
        else:
            self.screen.blit(self.speed1Image, (120, self.res[1]/2))

        if self.speed3.collidepoint(self.mouse_pos):
            self.screen.blit(self.speed3Image_pres, (165, self.res[1]/2 + 120))
        else:
            self.screen.blit(self.speed3Image, (165, self.res[1]/2 + 120))
#
#        if self.scores.collidepoint(self.mouse_pos):
#            self.scores = self.screen.blit(self.scoresImage_pres, (160, self.res[1]/2 + 180))
#        else:
#            self.scores = self.screen.blit(self.scoresImage, (160, self.res[1]/2 + 180))
#
    def Update(self, frameDeltaTime):
        pygame.display.update()
        self.MousePos()

    def MousePos(self):
        self.mouse_pos = pygame.mouse.get_pos()