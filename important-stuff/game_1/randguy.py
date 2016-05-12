#randguy.py
#, 0, 32
import pygame, sys
import
import time
from pygame.locals import *

pygame.init()

FPS = 30 #frames per second
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('randguy')

WHITE = (255, 255, 255)
person = pygame.image.load('guy3.png')
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
		
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.flip()
	fpsClock.tick(FPS)