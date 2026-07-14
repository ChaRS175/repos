# упражнение Стрельба по мишени 9.07.26

import pygame
from pygame.sprite import Sprite

class Target(Sprite):
	def __init__(self, shoot_game):
		super().__init__()

		self.screen = shoot_game.screen
		self.settings = shoot_game.settings
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load('images/target.png')
		self.rect = self.image.get_rect()

		self.center_target()

	def center_target(self):
		self.rect.midright = self.screen_rect.midright
		self.y = float(self.rect.y)

	def check_edges(self):
		if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
			return True
		return False

	def update(self):
		if self.check_edges():
			self.settings.target_direction *= -1

		self.y += self.settings.target_speed * self.settings.target_direction
		self.rect.y = self.y

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def center_target(self):
		self.rect.midright = self.screen_rect.midright
		self.y = float(self.rect.y)