# упражнение Боковая стрельба 2 6.07.26 

import pygame
from pygame.sprite import Sprite

class Alien_tablet(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings_tablet = ai_game.settings_tablet

		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	

