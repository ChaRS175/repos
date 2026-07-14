# упражнение Стрельба по мишени 9.07.26

import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import Game_stats
from play_button import Button
from ship import Ship
from bullet import Bullet
from target import Target

class Shoot_game:
	def __init__(self):
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption("Shoot Game")

		self.stats = Game_stats(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.target = Target(self)

		self.play_button = Button(self, "Нажми для старта игры")

	def run_game(self):
		while True:
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._bullets_update()
				self.target.update()

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
				self._check_play_button(mouse_pos)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _check_play_button(self, mouse_pos):
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self.stats.reset_stats()
			self.stats.game_active = True

			self.bullets.empty()

			self.target.center_target()
			self.ship.center_ship()

			pygame.mouse.set_visible(False)

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _bullets_update(self):
		self.bullets.update()

		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.screen_rect.right:
				self.bullets.remove(bullet)
				self._bullets_missed()

		self._check_collision()

	def _check_collision(self):
		collision = pygame.sprite.spritecollideany(self.target,self.bullets)
		if collision:
			self.bullets.remove(collision)
			self._target_hit()

	def _target_hit(self):
		if self.stats.targets_left > 1:
			self.stats.targets_left -= 1

			self.bullets.empty()

			self.ship.center_ship()
			self.target.center_target()

			sleep(1)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _bullets_missed(self):
		if self.stats.misses_left > 1:
			self.stats.misses_left -= 1
		else:
			self.stats.misses_left = 0
			self.bullets.empty()
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		self.target.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		
		if not self.stats.game_active:
			self.play_button.draw_button()

		pygame.display.flip()

if __name__ == '__main__':
	sg = Shoot_game()
	sg.run_game()



