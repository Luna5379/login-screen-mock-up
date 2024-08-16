import pygame, sys
from pygame.constants import QUIT
from pygame.locals import *

width = 393
height = 852
caption = "login"
bgColour = (22,19,36)
empytTextBoxColour = (38,32,54)
emptyTextColor = (189,174,232)
mySurface = None
sysfont = pygame.font.get_default_font()
fonts = pygame.font.get_fonts()
for i in range(len(fonts)):
  print(fonts[i])

def initialise(windowWidth, windowHeight, windowName, windowColour):
  global mySurface
  pygame.init()
  mySurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
  pygame.display.set_caption(windowName)
  mySurface.fill(color=windowColour)

def render():
  pygame.draw.rect(mySurface, empytTextBoxColour, (55,100,250,40))
  boxtext1 = pygame.font.SysFont('dejavusans', 35)
  box1 = boxtext1.render('Email', True, emptyTextColor)
  mySurface.blit(box1, (65,100))

  pygame.draw.rect(mySurface, empytTextBoxColour, (55,160,250,40))
  boxtext2 = pygame.font.SysFont('dejavusans', 35)
  box2 = boxtext2.render('Password', True, emptyTextColor)
  mySurface.blit(box2, (65,160))
  
  pygame.display.update()

initialise(width, height, caption, bgColour)
while True:
  render()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()


