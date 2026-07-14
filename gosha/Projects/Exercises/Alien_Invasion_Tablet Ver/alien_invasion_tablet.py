# упражнение Боковая стрельба 2.07.26

import sys

import pygame

from settings_tablet import Settings
from ship_tablet import Ship
from bullet_tablet import Bullet
from alien_tablet import Alien_tablet

class AlienInvasion:

	def __init__(self):
		pygame.init() # инициализация игры и ресурсов
		self.settings_tablet = Settings()

		self.screen = pygame.display.set_mode((1000, 800))
		self.settings_tablet.screen_width = self.screen.get_rect().width
		self.settings_tablet.screen_height = self.screen.get_rect().height

		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption("Alien Invasion")

		self.ship_tablet = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		while True: # отслеживание событий клавиатуры и мыши
			self._check_events()
			self.ship_tablet.update()
			self._bullets_update()
			self._update_aliens()
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

	def _bullets_update(self):
		self.bullets.update()

		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.screen_rect.right:
				self.bullets.remove(bullet)
		# print(len(self.bullets))

		self._check_collision()
		self._check_fleet()

	def _check_collision(self):
		collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

	def _check_fleet(self):
		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()

	def _create_fleet(self):
		alien_tablet = Alien_tablet(self)
		alien_width, alien_height = alien_tablet.rect.size
		ship_width = self.ship_tablet.rect.width
		available_space_x = self.settings_tablet.screen_width - alien_width - 2 * ship_width
		num_aliens_x = available_space_x // (3 * alien_width)

		ship_height = self.ship_tablet.rect.height
		available_space_y = self.settings_tablet.screen_height - (alien_height * 2 ) + ship_height // 2
		num_rows = available_space_y // (2 * alien_height)
		for row_num in range(num_rows):
			for alien_num in range(num_aliens_x):
				self._create_alien(alien_num, row_num)

	def _create_alien(self, alien_num, row_num):
		alien_tablet = Alien_tablet(self)
		alien_width, alien_height = alien_tablet.rect.size
		alien_tablet.x = self.settings_tablet.screen_width - alien_width - (2 * alien_width * alien_num)
		alien_tablet.rect.x = alien_tablet.x
		alien_tablet.rect.y = alien_height + 2 * alien_height * row_num
		self.aliens.add(alien_tablet)

	def _update_aliens(self):
		self.aliens.update()

		if pygame.sprite.spritecollideany(self.ship_tablet, self.aliens):
			print("-1 alien")


	def _update_screen(self):
		self.screen.fill(self.settings_tablet.bg_color)
		self.ship_tablet.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		# отображение последнего прорисованного экрана
		pygame.display.flip()

if __name__ == '__main__':
	# создание экземпляра и запуск игры
	ai = AlienInvasion()
	ai.run_game()
