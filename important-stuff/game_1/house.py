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

def drawMain():
	#draw
	DISPSURF.fill(SKY)
	#Hill
	pygame.draw.ellipse(DISPSURF, GRASS, (-50,240, 540,80))
	#House_rect
	pygame.draw.rect(DISPSURF, GRAY, (170, 190, 60, 60))
	#Door
	pygame.draw.rect(DISPSURF, BLUE, (175, 210, 20, 40))
	#window
	pygame.draw.rect(DISPSURF, WHITE, (205, 210, 20, 20))
	pygame.draw.line(DISPSURF, BLACK, (215, 210),(215, 229), 1)
	pygame.draw.line(DISPSURF, BLACK, (216, 210),(216, 229), 1)
	pygame.draw.line(DISPSURF, BLACK, (205, 220),(224, 220), 1)
	pygame.draw.line(DISPSURF, BLACK, (205, 221),(224, 221), 1)
	#chimney
	pygame.draw.rect(DISPSURF, BLACK, (207, 162, 18, 25))
	#House_poly
	pygame.draw.polygon(DISPSURF, RED, ((168,190),(200,160),(201,160),(231,190)))
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
	#sun
	pygame.draw.circle(DISPSURF, YELLOW, (350, 30), 7)
	#path
	pygame.draw.rect(DISPSURF, GRAY, (175, 250, 20, 50))
	pygame.draw.line(DISPSURF, BLACK, (184, 250), (184, 300), 2)
	pygame.draw.line(DISPSURF, BLACK, (175, 258), (194, 258), 1)
	pygame.draw.line(DISPSURF, BLACK, (175, 270), (194, 270), 1)
	pygame.draw.line(DISPSURF, BLACK, (175, 282), (194, 282), 1)
	pygame.draw.line(DISPSURF, BLACK, (175, 294), (194, 294), 1)

def randperson(FPS, fpsClock):
	"""
	FPS = 30 #frames per second
	fpsClock = pygame.time.Clock()
"""
	person = pygame.image.load('guy1.png')
	personx = 200
	persony = 250
	direction = 'right'

	while True: # the main game loop
		DISPLAYSURF.fill(WHITE)	
    
		if direction == 'right': 
			personx += 2
			if personx >= 390:
				direction = 'down'
		if direction == 'down': 
			persony += 2
			if persony >= 290:
				direction = 'left' 
		if direction == 'left': 
			personx -= 2 
			if personx <= 5:
				direction = 'up'
		if direction == 'up': 
			persony -= 2 
			if persony <= 230:
				direction = 'right' 

		DISPLAYSURF.blit(person, (personx, persony)) 	
		
		pygame.display.update()
		fpsClock.tick(FPS)

def player(FPS, fpsClock):
	"""
	FPS = 30 #frames per second
	fpsClock = pygame.time.Clock()
"""
	person = pygame.image.load('player.png')
	personx = 200
	persony = 250

	while True:
		DISPSURF.blit(person, (personx, persony))
	
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
    
		keys=pygame.key.get_pressed()
		if keys[K_RIGHT]: 
			personx += 5
			print personx, persony 
			if personx == 395:
				personx -= 5
		if keys[K_LEFT]: 
			personx -= 5
			print personx, persony 
			if personx == 0:
				personx += 5
		if keys[K_DOWN]: 
			persony += 5
			print personx, persony 
			if persony == 295:
				persony -= 5 
		if keys[K_UP]: 
			persony -= 5
			print personx, persony 
			if persony == 235:
				persony += 5 	
		
		pygame.display.update()
		fpsClock.tick(FPS)

def main():
	FPS = 30 #frames per second
	fpsClock = pygame.time.Clock()

	"""person = pygame.image.load('player.png')
	personx = 200
	persony = 250
	direction = 'right'"""

	while True: # the main game loop
		drawMain()
		player(FPS, fpsClock)
		randperson(FPS, fpsClock)

		pygame.display.flip()
		fpsClock.tick(FPS)

main()
