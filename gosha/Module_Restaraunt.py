class Restaraunt():
	def __init__(self, title, type):
		self.title = title.title()
		self.type = type
		self.number_served = 0

	def describe_restaraunt(self):
		print(f"We call this restaraunt '{self.title}' and it has grade in {self.type}")

	def open_restaraunt(self):
		print(f"Restaraunt is open")

	def served(self):
		print(f"\nNumber of served tables: {self.number_served}")

	def set_num_served(self, num):
		self.number_served = num

	def increment_number_served(self, summ):
		self.number_served += summ