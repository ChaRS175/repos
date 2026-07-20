# начал вроде 26.06.26

import sys
from time import sleep
from random import randint
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Score_board
from button import Button
from difficulty_menu import Difficulty_menu
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

		self.stats = GameStats(self)
		self.scoreboard = Score_board(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.stars = pygame.sprite.Group()

		self._create_row_stars()
		self._create_fleet()

		self.play_button = Button(self, "Нажми, если хочешь обстрелять лысых")
		self.difficulty_menu = Difficulty_menu(self)
		self.show_difficulty_menu = False

	def run_game(self):
		while True: # отслеживание событий клавиатуры и мыши
			self._check_events()
			if self.stats.game_active:
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
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_mouse_clicks(mouse_pos)
				
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

	def _check_mouse_clicks(self, mouse_pos):
		if self.stats.game_active:
			return

		if not self.show_difficulty_menu:
			if self.play_button.rect.collidepoint(mouse_pos):
				self.show_difficulty_menu = True
		else: 
			if self.difficulty_menu.easy_difficulty_button.rect.collidepoint(mouse_pos):
				self._start_game('Легко')
			elif self.difficulty_menu.medium_difficulty_button.rect.collidepoint(mouse_pos):
				self._start_game('Средне')
			elif self.difficulty_menu.hard_difficulty_button.rect.collidepoint(mouse_pos):
				self._start_game('Сложно')
			elif self.difficulty_menu.impossible_difficulty_button.rect.collidepoint(mouse_pos):
				self._start_game('Невозможно')

	def _start_game(self, difficulty):
		if difficulty == 'Средне':
			self.stats.reset_stats()
			self.settings.medium_increase_speed()
		elif difficulty == 'Сложно':
			self.stats.reset_stats()
			self.settings.hard_increase_speed()
		elif difficulty == 'Невозможно':
			self.stats.reset_stats()
			self.settings.impossible_increase_speed()

		self.stats.reset_stats()
		self.stats.game_active = True
		self.scoreboard.prep_score()
		self.scoreboard.prep_level()
		self.scoreboard.prep_ships()
		self.show_difficulty_menu = False

		self.aliens.empty()
		self.bullets.empty()

		self._create_fleet()
		self.ship.center_ship()
		pygame.mouse.set_visible(False)

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

		self._check_collision()
		self._check_fleet()

	def _check_collision(self):
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
		if collisions:
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_points
			self.scoreboard.prep_score()
			self.scoreboard.check_high_score()

	def _check_fleet(self):
		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()
			self.stats.level += 1
			self.scoreboard.prep_level()

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

	def _check_aliens_bottom(self):
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break

	def _change_fleet_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_aliens(self):
		self._check_fleet_edges()
		self.aliens.update()

		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		self._check_aliens_bottom()

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

	def _ship_hit(self):
		if self.stats.ships_left > 1:
			self.stats.ships_left -= 1
			self.scoreboard.prep_ships()

			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()

			sleep(0.5)
		else:
			self.stats.game_active = False
			self.stats.reset_stats()
			pygame.mouse.set_visible(True)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.stars.draw(self.screen)
		self.aliens.draw(self.screen)
		self.scoreboard.show_score()

		if not self.stats.game_active:
			if not self.show_difficulty_menu:
				self.play_button.draw_button()
			else:
				self.difficulty_menu.draw_menu()
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

# уничтожение прищельцев 6.07.26(сиксевеееееееен)

# возобновление игры после проигрыша 7.07.26

# добавление кнопки Play 8.07.26

# с 9.07.26 по 10.07.26 делал усложнение и ускорение игры

# с 11.07.26 по 13.07.26 делал кнопки сложности

# полностью кончил 17.07.26
