from math import *
import sys

W = 800
H = 600

# check if there're not enough args
if len(sys.argv) != 4:
    print ("Nyaa! Nya nya nya nyan >:3")
    sys.exit()
    
# check if there're not enough vals
try:
    print (sys.argv[1], sys.argv[2])
    leftval = float(sys.argv[1])
    rightval = float(sys.argv[2])
    print(leftval, rightval)
except:
    print("NYAAA!!!!1!! >:(")
    sys.exit()
    
# fill the list of args
try:
    values = list()
    x = leftval
    step = (rightval - leftval) / W
    while x < rightval:
        values.append(eval(sys.argv[3]))
        x += step
except:
    print("nyaa ;__;")

theY = max(values, key = abs)
if theY:
    k = H / 2 / theY
else:
    k = 1

for i in range (len(values)):
    values[i] = H/2 - k*values[i]

points = [num for num in enumerate(values, 0)]

import pygame
from pygame import *

pygame.init()
res = (W, H)
screen = pygame.display.set_mode(res, 0)

font = pygame.font.Font(None, 36)
text = sys.argv[3]
size = font.size(text)

ren = font.render(text, 0, (250, 200, 240), (0, 0, 0))
screen.blit(ren, (res[0] / 2 - size[0] / 2, 0 + H/8))

while True:
    if pygame.event.wait().type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
        break
    screen.blit(ren, (res[0] / 2 - size[0] / 2, 0 + H/8))
    pygame.draw.line(screen, (255,0,0), (0, H/2), (W, H/2))
    pygame.draw.line(screen, (255,0,0), (W/2, 0), (W/2, H))
    pygame.draw.lines(screen, (0,255,255), 0, points)
    pygame.display.update()

pygame.quit()

