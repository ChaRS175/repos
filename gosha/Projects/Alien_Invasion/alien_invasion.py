# начал вроде 26.06.26

import sys
from random import randint
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star

class AlienInvasion:

	def __init__(self):
		pygame.init() # инициализация игры и ресурсов
		self.settings = Settings()

		
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.stars = pygame.sprite.Group()

		self._create_row_stars()
		self._create_fleet()


	def run_game(self):
		while True: # отслеживание событий клавиатуры и мыши
			self._check_events()
			self.ship.update()
			self._bullets_update()
			self._update_aliens()
			self._update_screen()


	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
				
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

	def _bullets_update(self):
		self.bullets.update()

		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		# print(len(self.bullets))

	def _create_fleet(self):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		ship_height = self.ship.rect.height
		available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
		number_rows = available_space_y // (2 * alien_height)
		for row_num in range(number_rows):
			for alien_num in range(number_aliens_x):
				self._create_alien(alien_num, row_num)

	def _create_alien(self, alien_num, row_num):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_num
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_aliens(self):
		self._check_fleet_edges()
		self.aliens.update()

	def _create_row_stars(self):
		star = Star(self)
		star_width, star_height = star.rect.size
		available_space_x = self.settings.screen_width - (star_width // 2)
		num_stars_x = available_space_x // (2 * star_width)

		ship_height = self.ship.rect.height
		available_space_y = self.settings.screen_height - (star_height // 2) - ship_height
		num_rows_star = available_space_y // (2 * star_height)
		for row_star_num in range(num_rows_star):
			for star_num in range(num_stars_x):
				self._create_star(star_num, row_star_num)

	def _create_star(self, star_num, row_star_num):
		star = Star(self)
		star_width, star_height = star.rect.size

		random_move_x = randint(-100, 100)
		random_move_y = randint(-100, 100)

		star.x = star_width + 2 * star_width * star_num + random_move_x
		star.rect.x = star.x
		star.rect.y = star.rect.height + 2 * star.rect.height * row_star_num + random_move_y
		self.stars.add(star)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.stars.draw(self.screen)
		self.aliens.draw(self.screen)

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

# добавление на экран пришельцев 3.07.26

# упражнения Звезда, Звезда-2 4.07.26
# добавление движения прищельцев 4.07.26

# упражнения Капли и Дождь 5.07.26

# уничтожение прищельцев 6.07.26
