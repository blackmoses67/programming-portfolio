#person.py

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 #frames per second
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((600, 400), 0, 32)
pygame.display.set_caption('person')

WHITE = (255, 255, 255)
person = pygame.image.load('player.png')
personx = 10
persony = 10
direction = 'right'

while True: # the main game loop
	DISPLAYSURF.fill(WHITE)
	
	
	
	DISPLAYSURF.blit(person, (personx, persony))
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
    
	keys=pygame.key.get_pressed()
	if keys[K_RIGHT]: 
		personx += 5
	if keys[K_LEFT]: 
		personx -= 5
	if keys[K_DOWN]: 
		persony += 5
	if keys[K_UP]: 
		persony -= 5    	
		
	pygame.display.update()
	fpsClock.tick(FPS)