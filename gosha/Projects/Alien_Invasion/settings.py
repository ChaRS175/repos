class Settings():

	def __init__(self):
		self.screen_width = 800
		self.screen_height = 500
		self.bg_color = (100, 150, 200)
		self.ship_speed = 3.5
		self.alien_speed = 1
		self.fleet_drop_speed = 10
		# fleet_direction = 1 это движение вправо, а -1 движение влево
		self.fleet_direction = 1

		self.bullet_speed = 3
		self.bullet_width = 10
		self.bullet_height = 30
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 10