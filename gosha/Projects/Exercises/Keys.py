# упражнение Клавиши 30.06.26

import pygame
import sys

from key_self import Key_self
from key_settings import Key_settings

from pygame.color import THECOLORS

class Keys:
	def __init__(self):
		 pygame.init()
		 self.key_settings = Key_settings()
		 self.screen = pygame.display.set_mode((1000, 600))
		 pygame.display.set_caption("Keys")

		 self.key_self = Key_self(self)

	def run_prog(self):
		while True:
			self._check_events()
			self.key_self.update()
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
			self.key_self.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.key_self.moving_left = True
		elif event.key == pygame.K_UP:
			self.key_self.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.key_self.moving_down = True	
		elif event.key == pygame.K_ESCAPE:
			sys.exit()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.key_self.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.key_self.moving_left = False
		elif event.key == pygame.K_UP:
			self.key_self.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.key_self.moving_down = False

	def _update_screen(self):
		self.screen.fill(THECOLORS['gray'])
		self.key_self.show()
		pygame.display.flip()

if __name__ == '__main__':
	keys = Keys()
	keys.run_prog()
