	# начал вроде 26.06.26

import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:

	def __init__(self):
		pygame.init() # инициализация игры и ресурсов
		self.settings = Settings()

		self.screen = pygame.display.set_mode((800, 550))
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		while True: # отслеживание событий клавиатуры и мыши
			self._check_events()
			self.ship.update()
			self.bullets.update()

			for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
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
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_UP:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# отображение последнего прорисованного экрана
		pygame.display.flip()

if __name__ == '__main__':
	# создание экземпляра и запуск игры
	ai = AlienInvasion()
	ai.run_game()

# вывод корабля на экран 248стр 27.06.26

# управление кораблём 28.06.26

# в двух словах 29.06.26

# упражнение Ракета 29.06.26 

# упражнение Клавиши 30.06.26

# не помню 31.06.26

# добавление снарядов и стрельбы 1.07.26

# ограничение снарядов и удаление их при выходе за границу окна 2.07.26
# упражнение Боковая стрельба 2.07.26