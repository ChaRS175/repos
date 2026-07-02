# упражнение Боковая стрельба 2.07.26

import sys

import pygame

from settings_tablet import Settings
from ship_tablet import Ship
from bullet_tablet import Bullet

class AlienInvasion:

	def __init__(self):
		pygame.init() # инициализация игры и ресурсов
		self.settings_tablet = Settings()

		self.screen = pygame.display.set_mode((self.settings_tablet.screen_width, self.settings_tablet.screen_height))
		
		self.settings_tablet.screen_width = self.screen.get_rect().width
		self.settings_tablet.screen_height = self.screen.get_rect().height

		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption("Alien Invasion")

		self.ship_tablet = Ship(self)
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		while True: # отслеживание событий клавиатуры и мыши
			self._check_events()
			self.ship_tablet.update()
			self.bullets.update()

			for bullet in self.bullets.copy():
				if bullet.rect.left >= self.screen_rect.right:
					self.bullets.remove(bullet)
			print(len(self.bullets))
			
			self._update_screen()


	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
				
	def _check_keydown_events(self, event):
		if event.key == pygame.K_UP:
			self.ship_tablet.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship_tablet.moving_down = True
		elif event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_UP:
			self.ship_tablet.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship_tablet.moving_down = False

	def _fire_bullet(self):
		if len(self.bullets) < self.settings_tablet.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_screen(self):
		self.screen.fill(self.settings_tablet.bg_color)
		self.ship_tablet.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# отображение последнего прорисованного экрана
		pygame.display.flip()

if __name__ == '__main__':
	# создание экземпляра и запуск игры
	ai = AlienInvasion()
	ai.run_game()
