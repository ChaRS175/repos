class Employee():
	def __init__(self, name, lastname, money = 5000):
		self.name = name
		self.lastname = lastname
		self.money = int(money) if money else 5000
		self.employee_data = []

	def give_raise(self, amount):
		self.money += int(amount)

	def question(self):
		print(self.question)

	def show_data(self):
		print("Your data: ")
		print(f"Name: {self.name.title()}")
		print(f"Lastname: {self.lastname.title()}")
		print(f"Raise: {self.money}")


	





