import pygame
from button import Button

class Difficulty_menu:
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		self.easy_difficulty_button = Button(ai_game, "Легко", (0, 250, 0))
		self.medium_difficulty_button = Button(ai_game, "Средне", (255, 255, 0))
		self.hard_difficulty_button = Button(ai_game, "Сложно", (255, 0, 0))
		self.impossible_difficulty_button = Button(ai_game, "Невозможно", (200, 0, 200))

		self._arrange_buttons()

	def _arrange_buttons(self):
		center_x = self.screen_rect.centerx
		center_y = self.screen_rect.centery

		self.easy_difficulty_button.rect.center = (center_x, center_y - 85)
		self.medium_difficulty_button.rect.center = (center_x, center_y - 30)
		self.hard_difficulty_button.rect.center = (center_x, center_y + 30)
		self.impossible_difficulty_button.rect.center = (center_x, center_y + 85)
		
		self.easy_difficulty_button.msg_image_rect.center = self.easy_difficulty_button.rect.center
		self.medium_difficulty_button.msg_image_rect.center = self.medium_difficulty_button.rect.center
		self.hard_difficulty_button.msg_image_rect.center = self.hard_difficulty_button.rect.center
		self.impossible_difficulty_button.msg_image_rect.center = self.impossible_difficulty_button.rect.center
	def draw_menu(self):
		self.easy_difficulty_button.draw_button()
		self.medium_difficulty_button.draw_button()
		self.hard_difficulty_button.draw_button()
		self.impossible_difficulty_button.draw_button()


