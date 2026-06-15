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

class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage

		else:
			print("You can't roll back an odometer") 

	def increment_odometer(self, miles):
		self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 563
my_new_car.update_odometer(56)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(f"\n{my_used_car.get_descriptive_name()}")

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
	
my_used_car.increment_odometer(44176)
my_used_car.read_odometer()

# упражнения

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

restaraunt = Restaraunt('dick', '5 stars')
print(f"\nI like restaraunt {restaraunt.title}")
print(f"And people give a grade {restaraunt.type} for it")
restaraunt.describe_restaraunt()
restaraunt.open_restaraunt()

restaraunt1 = Restaraunt('tiki tiki tiki tiiiiki', '6.7 stars')
print(f"But my favourite restaraunt is {restaraunt1.title}")
print(f"And this restaraunt has a grade in  {restaraunt1.type}")

restaraunt.set_num_served(12)
restaraunt.increment_number_served(10)
restaraunt.served() 


class User():
	def __init__(self, firstname, lastname, age):
		self.firstname = firstname.title()
		self.lastname = lastname.title()
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		print("You are user pidore")

	def greet_user(self):
		print(f"Hi, poshol nahui, {self.firstname}")

	def login_attempts_f(self):
		print(f"Attempts: {self.login_attempts}")

	def increment_login_attepmts(self, increase):
		self.login_attempts += increase

	def reset_login_attempts(self):
		self.login_attempts = 0

user = User('gesha', 'pines', 148)
print(f"\nFirstname: {user.firstname}, Lastname: {user.lastname}, Age: {user.age}")
user.describe_user()
user.greet_user()

user_another = User('misha', 'gummy', 'ded_stariy')
print(f"Firstname: {user_another.firstname}, Lastname: {user_another.lastname}, Age: {user_another.age}")
user_another.describe_user()
user_another.greet_user()

user.increment_login_attepmts(5)
user.login_attempts_f()
user.reset_login_attempts()
user.login_attempts_f()
user.increment_login_attepmts(3)
user.login_attempts_f()




