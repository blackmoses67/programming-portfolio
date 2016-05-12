import pygame
import sys

from pygame.locals import *

pygame.init()

FPS = 60 # frames per second
fpsClock = pygame.time.Clock()

DISPSURF = pygame.display.set_mode((600, 400), 0, 32)
pygame.display.set_caption('cat moves')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10

direction = 'right'

while True: #main game loop
	DISPSURF.fill(WHITE)
	if direction == 'right':
		catx += 5
		if catx == 450:
			direction = 'down'
	elif direction == 'down':
		caty += 5
		if caty == 225:
			direction == 'left'
	elif direction == 'left':
		catx -= 5
		if catx == 10:
			direction == 'up'
	elif direction == 'up':
		caty += 5
		if caty == 10:
			direction == 'right'

	DISPSURF.blit(catImg, (catx, caty))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				catx += 10
			if event.key == pygame.K_LEFT:
				catx -= 10
			if event.key == pygame.K_DOWN:
				caty += 10

	pygame.display.update()
	fpsClock.tick(FPS)
