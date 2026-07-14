class Settings():

	def __init__(self):
		self.screen_width = 800
		self.screen_height = 500
		self.bg_color = (100, 150, 200)
		self.ships_limit = 3
		self.fleet_drop_speed = 10
		# fleet_direction = 1 это движение вправо, а -1 движение влево
		self.fleet_direction = 1

		
		self.bullet_width = 10
		self.bullet_height = 30
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 10

		self.medium_speedup_scale = 2
		self.hard_speedup_scale = 5
		self.impossible_speedup_scale = 10

		self.medium_score_scale = 1.5
		self.hard_score_scale = 3
		self.impossible_score_scale = 5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed = 3.5
		self.alien_speed = 1.5
		self.bullet_speed = 3
		self.alien_points = 50

		self.fleet_direction = 1

	def medium_increase_speed(self):
		self.ship_speed *= self.medium_speedup_scale
		self.bullet_speed *= self.medium_speedup_scale
		self.alien_speed *= self.medium_speedup_scale

		self.alien_points = int(self.alien_points * self.medium_score_scale)

	def hard_increase_speed(self):
		self.ship_speed *= self.hard_speedup_scale
		self.bullet_speed *= self.hard_speedup_scale
		self.alien_speed *= self.hard_speedup_scale

		self.alien_points = int(self.alien_points * self.hard_score_scale)

	def impossible_increase_speed(self):
		self.ship_speed *= self.impossible_speedup_scale
		self.bullet_speed *= self.impossible_speedup_scale
		self.alien_speed *= self.impossible_speedup_scale

		self.alien_points = int(self.alien_points * self.impossible_score_scale)