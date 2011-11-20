import pygame
from pygame.locals import *
from statemanager import *

class MainMenu:
    instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(MainMenu, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self, res, screen):
        self.res = res
        self.screen = screen
        # new game button names
        self.new_game_imagename = "./images/new_game.png"
        self.new_game_pres_imagename = "./images/new_game_pres.png"
        self.MousePos()
        # about button names
        self.about_imagename = "./images/about_but.png"
        self.about_pres_imagename = "./images/about_but_pres.png"

        # settings button names
        self.settings_imagename = "./images/settings_but.png"
        self.settings_pres_imagename = "./images/settings_but_pres.png"

        # scores button names
        self.scores_imagename = "./images/scores.png"
        self.scores_pres_imagename = "./images/scores_pres.png"

        self.logo_imagename = "./images/gotetris_logo.png"

        self.newGameImage = pygame.image.load(self.new_game_imagename).convert()
        self.newGameImage_pres = pygame.image.load(self.new_game_pres_imagename).convert()

        self.aboutImage = pygame.image.load(self.about_imagename).convert()
        self.aboutImage_pres = pygame.image.load(self.about_pres_imagename).convert()

        self.settingsImage = pygame.image.load(self.settings_imagename).convert()
        self.settingsImage_pres = pygame.image.load(self.settings_pres_imagename).convert()

        self.scoresImage = pygame.image.load(self.scores_imagename).convert()
        self.scoresImage_pres = pygame.image.load(self.scores_pres_imagename).convert()

        self.logoImage = pygame.image.load(self.logo_imagename).convert()

    def Draw(self):
        self.newGame = self.screen.blit(self.newGameImage, (120, self.res[1]/2))
        self.settings = self.screen.blit(self.settingsImage, (150, self.res[1]/2 + 60))
        self.about = self.screen.blit(self.aboutImage, (165, self.res[1]/2 + 120))
        self.scores = self.screen.blit(self.scoresImage, (160, self.res[1]/2 + 180))
        self.logo = self.screen.blit(self.logoImage, (80, 60))


        if self.settings.collidepoint(self.mouse_pos):
            self.screen.blit(self.settingsImage_pres, (150, self.res[1]/2 + 60))
#            for event in pygame.event.get():
#                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
#                    from statemanager import StateManager
#                    StateManager.setState(StateManager.instance, 'STATE_SETTINGS')
        else:
            self.screen.blit(self.settingsImage, (150, self.res[1]/2 + 60))

        if self.newGame.collidepoint(self.mouse_pos):
            self.screen.blit(self.newGameImage_pres, (120, self.res[1]/2))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    from statemanager import StateManager
                    StateManager.setState(StateManager.instance, 'STATE_GAME')
        else:
            self.screen.blit(self.newGameImage, (120, self.res[1]/2))

        if self.about.collidepoint(self.mouse_pos):
            self.screen.blit(self.aboutImage_pres, (165, self.res[1]/2 + 120))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    from statemanager import StateManager
                    StateManager.setState(StateManager.instance, 'STATE_ABOUT')
        else:
            self.screen.blit(self.aboutImage, (165, self.res[1]/2 + 120))

        if self.scores.collidepoint(self.mouse_pos):
            self.scores = self.screen.blit(self.scoresImage_pres, (160, self.res[1]/2 + 180))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    from statemanager import StateManager
                    StateManager.setState(StateManager.instance, 'STATE_HIGHSCORES')
        else:
            self.scores = self.screen.blit(self.scoresImage, (160, self.res[1]/2 + 180))

    def Update(self, frameDeltaTime):
        pygame.display.update()
        self.MousePos()

    def MousePos(self):
        self.mouse_pos = pygame.mouse.get_pos()