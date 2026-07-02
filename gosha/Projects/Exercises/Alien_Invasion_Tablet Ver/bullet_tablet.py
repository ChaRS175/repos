# упражнение Боковая стрельба 2.07.26

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings_tablet = ai_game.settings_tablet
		self.color = self.settings_tablet.bullet_color

		self.rect = pygame.Rect(0, 0, self.settings_tablet.bullet_width, self.settings_tablet.bullet_height)
		self.rect.midleft = ai_game.ship_tablet.rect.midright

		self.x = float(self.rect.x)

	def update(self):
		self.x += self.settings_tablet.bullet_speed
		self.rect.x = self.x

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)