# упражнение 27.06.26

import pygame

from settings import Settings
from Player import Player

class Player_field:
	def __init__(self):
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Player field")

		self.player = Player(self)

	def run_game(self):
		self._update_screen()

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.player.draw_player()
		# отображение последнего прорисованного экрана
		pygame.display.flip()


if __name__ == '__main__':
	Pf = Player_field()
	Pf.run_game()