import pygame
from pygame.locals import *
from statemanager import *

RES = [480, 640]

pygame.init()
screen = pygame.display.set_mode(RES)
pygame.display.set_caption("Gotetris")

from statemanager import StateManager
manager = StateManager(RES, screen)

manager.Run()