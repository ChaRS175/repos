# упражнение Стрельба по мишени 9.07.26

class Game_stats():
	def __init__(self, shoot_game):
		self.settings = shoot_game.settings
		self.reset_stats()
		self.game_active = False

	def reset_stats(self):
		self.targets_left = self.settings.targets_limit
		self.misses_left = self.settings.miss_limit
		













