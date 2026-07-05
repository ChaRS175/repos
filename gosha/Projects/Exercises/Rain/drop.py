# упражнение Дождь и Капля 5.07.26

import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
	def __init__(self, rain):
		super().__init__()
		self.screen = rain.screen
		self.rain_settings = rain.rain_settings

		self.image = pygame.image.load('images/drop.jpg')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		
		self.y = float(self.rect.y)

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		self.y += self.rain_settings.drop_speed
		self.rect.y = self.y