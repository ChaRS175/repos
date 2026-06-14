# начал 14.06.26

class Dog():
	def __init__(self, name, age):
		self.name = name.title()
		self.age = age

	def sit(self):
		print(f"{self.name} is now sitting")

	def roll_over(self):
		print(f"{self.name} rolled over")

my_dog = Dog('sphere', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('pistrun', 3)
print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")

your_dog.sit()

# упражнения

class Restaraunt():
	def __init__(self, title, type):
		self.title = title.title()
		self.type = type
	def describe_restaraunt(self):
		print(f"We call this restaraunt '{self.title}' and it has grade in {self.type}")

	def open_restaraunt(self):
		print(f"Restaraunt is open")

restaraunt = Restaraunt('dick', '5 stars')
print(f"\nI like restaraunt {restaraunt.title}")
print(f"And people give a grade {restaraunt.type} for it")
restaraunt.describe_restaraunt()
restaraunt.open_restaraunt()

restaraunt1 = Restaraunt('tiki tiki tiki tiiiiki', '6.7 stars')
print(f"But my favourite restaraunt is {restaraunt1.title}")
print(f"And this restaraunt has a grade in  {restaraunt1.type}")

class User():
	def __init__(self, firstname, lastname, age):
		self.firstname = firstname.title()
		self.lastname = lastname.title()
		self.age = age

	def describe_user(self):
		print("You are user pidore")

	def greet_user(self):
		print(f"Hi, poshol nahui, {self.firstname}")

user = User('gesha', 'pines', 148)
print(f"\nFirstname: {user.firstname}, Lastname: {user.lastname}, Age: {user.age}")
user.describe_user()
user.greet_user()

user_another = User('misha', 'gummy', 'ded_stariy')
print(f"Firstname: {user_another.firstname}, Lastname: {user_another.lastname}, Age: {user_another.age}")
user_another.describe_user()
user_another.greet_user()

# работа с классами и экземплярами 15.06.26







