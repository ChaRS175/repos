# упражнение Боковая стрельба 2.07.26

import pygame

class Ship():
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.settings_tablet = ai_game.settings_tablet
		self.screen_rect = ai_game.screen.get_rect()
		# загружает изображение корабля и получает прямоугольник(все объекты имеют невидимую форму прямоугольника)
		self.image = pygame.image.load('images/ship_tablet.jpg')
		self.image = pygame.transform.rotate(self.image, -90)
		self.rect = self.image.get_rect()
		# каждый новый корабль появляется внизу по центру
		self.rect.left = self.screen_rect.left

		self.y = float(self.rect.y)

		self.moving_up = False
		self.moving_down = False

	def update(self):
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings_tablet.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings_tablet.ship_speed

		self.rect.y = self.y

	def blitme(self):
		# рисует корабль в текущей позиции
		self.screen.blit(self.image, self.rect)

	