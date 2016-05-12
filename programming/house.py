# fun with pygame
import pygame
import sys

from pygame.locals import *

pygame.init()

DISPSURF = pygame.display.set_mode((400, 300))
# R G B
RED    = ( 255,   0,   0)
BLUE   = (   0,   0, 255)
GREEN  = (   0, 255,   0)
WHITE  = ( 255, 255, 255)
BLACK  = (   0,   0,   0)
PURPLE = ( 255,   0, 255)
YELLOW = ( 255, 255,   0)
GRAY   = ( 128, 128, 128)
SKY    = (   3, 192, 255)
GRASS  = (   0, 174,  94)
BROWN  = ( 212, 129,  86)
LEAVES = (   0, 124,  94)
L_GRAY = ( 190, 190, 190)

#draw
DISPSURF.fill(SKY)
#Hill
pygame.draw.ellipse(DISPSURF, GRASS, (-50,240, 540,80))
#House_rect
pygame.draw.rect(DISPSURF, GRAY, (170, 190, 60, 60))
#Door
pygame.draw.rect(DISPSURF, BLUE, (175, 210, 20, 40))#window
pygame.draw.rect(DISPSURF, WHITE, (205, 210, 20, 20))
pygame.draw.line(DISPSURF, BLACK, (215, 210),(215, 230), 1)
pygame.draw.line(DISPSURF, BLACK, (216, 210),(216, 230), 1)
pygame.draw.line(DISPSURF, BLACK, (205, 220),(225, 220), 1)
pygame.draw.line(DISPSURF, BLACK, (205, 221),(225, 221), 1)
#chimney
pygame.draw.rect(DISPSURF, BLACK, (207, 162, 18, 25))
#House_poly
pygame.draw.polygon(DISPSURF, RED, ((168,190),(200,160),(201,160),(232,190)))
#door knob
pygame.draw.circle(DISPSURF, BLACK, (190, 230), 2)
#Trees
pygame.draw.rect(DISPSURF, BROWN, (85, 200, 20, 50))
pygame.draw.polygon(DISPSURF, LEAVES, ((75,220),(95,150),(115,220)))
pygame.draw.rect(DISPSURF, BROWN, (315, 200, 20, 50))
pygame.draw.polygon(DISPSURF, LEAVES, ((305,220),(325,150),(345,220)))
#clouds
pygame.draw.ellipse(DISPSURF, WHITE, (35, 35, 100, 50))
pygame.draw.ellipse(DISPSURF, WHITE, (55, 75, 100, 50))
pygame.draw.ellipse(DISPSURF, WHITE, (235, 55, 100, 50))
#path
pygame.draw.rect(DISPSURF, L_GRAY, (175, 250, 20, 50))

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	pygame.display.update()