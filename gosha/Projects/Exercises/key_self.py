# упражнение Клавиши 30.06.26

import pygame

from key_settings import Key_settings

class Key_self():
	def __init__(self, key_prog):
		self.screen = key_prog.screen
		self.key_settings = key_prog.key_settings
		self.screen_rect = key_prog.screen.get_rect()

		self.image = pygame.image.load('images/square.png')
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
			self.x += self.key_settings.key_speed
			print("You are moving on right")
		if self.moving_left and self.rect.left > 0:
			self.x -= self.key_settings.key_speed
			print("You are moving on left")

		if self.moving_up and self.rect.top > 0:
			self.y -= self.key_settings.key_speed
			print("You are moving up")
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.key_settings.key_speed
			print("You are moving down")

		self.rect.x = int(self.x)
		self.rect.y = int(self.y)

	def show(self):
		self.screen.blit(self.image, self.rect)