# упражнение Боковая стрельба 2.07.26

class Settings():

	def __init__(self):
		self.screen_width = 1920
		self.screen_height = 1080
		self.bg_color = (100, 150, 200)
		self.ship_speed = 3
		self.alien_speed = 1
		self.fleet_direction = -1

		self.bullet_speed = 3
		self.bullet_width = 30
		self.bullet_height = 10
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 10