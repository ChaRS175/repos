# упражнение Ракета 29.06.26

import pygame

from rocket_settings import Rocket_settings

class Rocket():
	def __init__(self, rf_game):
		self.screen = rf_game.screen
		self.rocket_settings = rf_game.rocket_settings
		self.screen_rect = rf_game.screen.get_rect()

		self.image = pygame.image.load('images/ship.jpg')
		self.rect = self.image.get_rect()

		self.rect.center = self.screen_rect.center

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.rocket_settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.rocket_settings.ship_speed

		if self.moving_up and self.rect.top > 0:
			self.y -= self.rocket_settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.rocket_settings.ship_speed

		self.rect.x = int(self.x)
		self.rect.y = int(self.y)

	def demonstrate(self):
		self.screen.blit(self.image, self.rect)
