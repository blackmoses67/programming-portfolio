#Objects
import pygame
import sys

from pygame.locals import *
from house.py import *

class Block(pygame.sprite.Sprite):
	#Constructor
	color = WHITE
	height = 60
	width = 60
	def __init__(self, color, width, height):
		#call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		#create an image of the block, and fill it with a color
		#this could also be an image loaded from the disk
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		#getch the rectangle object that has the dimensions of the image
		#update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect(50, 50)