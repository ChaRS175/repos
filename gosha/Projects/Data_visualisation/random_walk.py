# 19.07.26

from random import choice

class RandomWalk():
	def __init__(self, num_points = 5000):
		self.num_points = num_points

		# все блуждания начинаются с точки (0, 0)
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		# шаги генерируются до достижения нужной длины
		while len(self.x_values) < self.num_points:
			# определение направления и длины перемещения
			# рефакторинг 20.07.26
			self.get_xstep()
			self.get_ystep()
			
	def get_xstep(self):
		x_direction = choice([1, -1])
		x_distance = choice(range(1, 5))
		x_step = x_direction * x_distance

		# отклонение нулевых значений
		if x_step == 0:
			return

		# вычисление следующих значений x
		x = self.x_values[-1] + x_step
		self.x_values.append(x)

	def get_ystep(self):
		y_direction = choice([1, -1])
		y_distance = choice(range(1, 5))
		y_step = y_direction * y_distance

		# отклонение нулевых значений
		if y_step == 0:
			return

		# вычисление следующих значений y
		y = self.y_values[-1] + y_step
		self.y_values.append(y)

# кончил 20.07.26