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

mySurface = None

def initialise(windowWidth, windowHeight, windowName, windowColour):
  global mySurface
  pygame.init()
  mySurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
  pygame.display.set_caption(windowName)
  mySurface.fill(color=windowColour)

def render():
  pygame.draw.rect(mySurface, RED, (10,10,15,15))
  pygame.draw.polygon(mySurface, YELLOW, ((146,0), (291, 106), (236, 277), (56, 277), (0, 106)))
  pygame.draw.line(mySurface, GREEN, (60, 60), (120, 60), 20)
  pygame.draw.circle(mySurface, BLACK, (300, 50), 20, 0)
  pygame.draw.ellipse(mySurface, WHITE, (300, 250, 40, 80), 0)
  pygame.display.update()

initialise(width, height, caption, BLUE)
while True:
  render()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

