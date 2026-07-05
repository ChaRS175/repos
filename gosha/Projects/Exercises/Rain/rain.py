# упражнение Дождь и Капля 5.07.26

import sys
from random import randint
import pygame

from rain_settings import Rain_settings as R_settings
from drop import Drop

class Rain:
	def __init__(self):
		pygame.init()
		self.rain_settings = R_settings()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.rain_settings.screen_width = self.screen.get_rect().width
		self.rain_settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("November Rain")

		self.drop = Drop(self)
		self.drops = pygame.sprite.Group()

		self._create_rain()

	def run_rain(self):
		while True:
			self._check_events()
			self._update_drops()
			self._update_screen()


	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_ESCAPE:
			sys.exit()

	def _create_rain(self):
		drop = Drop(self)
		drop_width, drop_height = drop.rect.size
		available_space_x = self.rain_settings.screen_width - (2 * drop_width)
		self.num_drops_x = available_space_x // (2 * drop_width)
		
		available_space_y = self.rain_settings.screen_height - (3 * drop_height) - 100
		num_rows = available_space_y // (drop_height // 2)
		for row_num in range(num_rows):
			for drop_num in range(self.num_drops_x):
				self._create_drop(drop_num, row_num)

	def _create_drop(self, drop_num, row_num):
		drop = Drop(self)
		drop_width, drop_height = drop.rect.size

		random_move_x = randint(-100, 100) 
		random_move_y = randint(-100, 100)
		
		drop.x = drop_width + 2 * drop_width * drop_num + random_move_x
		drop.rect.x = drop.x
		drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_num + random_move_y
		drop.y = float(drop.rect.y)
		self.drops.add(drop)

	def _update_drops(self):
		self.drops.update()
		self.screen_rect = self.screen.get_rect()

		make_new_row = False

		for drop in self.drops.copy():
			if drop.rect.bottom >= self.screen_rect.bottom:
				self.drops.remove(drop)
				make_new_row = True

		if make_new_row and len(self.drops) < self.rain_settings.drops_allowed:
			for drop_num in range(self.num_drops_x):
				self._create_drop(drop_num, row_num = -2)

	def _update_screen(self):
		self.screen.fill(self.rain_settings.bg_color)
		self.drops.draw(self.screen)

		pygame.display.flip()

if __name__ == '__main__':
	R = Rain()
	R.run_rain()
