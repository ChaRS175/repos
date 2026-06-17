class User():
	def __init__(self, firstname, lastname, age):
		self.firstname = firstname.title()
		self.lastname = lastname.title()
		self.age = age

	def describe_user(self):
		print("You are user pidore")

	def greet_user(self):
		print(f"Hi, poshol nahui, {self.firstname}")