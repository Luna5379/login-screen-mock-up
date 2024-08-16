import pygame, sys
from pygame.constants import QUIT
from pygame.locals import *

width = 360
height = 740
caption = "login"
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
bgColour = (19,31,36)
empytTextBoxColour = (32,47,54)
emptyTextColor = (149,161,168)
mySurface = None
sysfont = pygame.font.get_default_font()

def initialise(windowWidth, windowHeight, windowName, windowColour):
  global mySurface
  pygame.init()
  mySurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
  pygame.display.set_caption(windowName)
  mySurface.fill(color=windowColour)

def render():
  pygame.draw.rect(mySurface, empytTextBoxColour, (55,100,250,40))
  boxtext1 = pygame.font.SysFont('enter email', 60)
  box1 = boxtext1.render('enter email', True, emptyTextColor)
  mySurface.blit(box1, (65,100))
  pygame.display.update()

initialise(width, height, caption, bgColour)
while True:
  render()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()


