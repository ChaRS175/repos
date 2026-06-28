# упражнение 27.06.26

import pygame

class Player():
	def __init__(self, player):
		self.screen = player.screen
		self.screen_rect = player.screen.get_rect()
		self.image = pygame.image.load('images/sonic.jpg')
		self.rect = self.image.get_rect()
		self.rect.center = self.screen_rect.center

	def draw_player(self):
		self.screen.blit(self.image, self.rect)