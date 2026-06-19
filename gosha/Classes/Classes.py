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

	def fill_gas_tank(self):
		print("Gas tank has been filled")

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
my_used_car.fill_gas_tank()

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
		print(f"\nFirstname: {user.firstname}, Lastname: {user.lastname}, Age: {user.age}")

	def describe_another_user(self):
		print(f"Firstname: {user_another.firstname}, Lastname: {user_another.lastname}, Age: {user_another.age}")

	def greet_user(self):
		print(f"Hi, poshol nahui, {self.firstname}")

	def login_attempts_f(self):
		print(f"Attempts: {self.login_attempts}")

	def increment_login_attepmts(self, increase):
		self.login_attempts += increase

	def reset_login_attempts(self):
		self.login_attempts = 0

user = User('gesha', 'pines', 148)
user.describe_user()
user.greet_user()

user_another = User('misha', 'gummy', 'ded_stariy')
user_another.describe_another_user()
user_another.greet_user()

user.increment_login_attepmts(5)
user.login_attempts_f()
user.reset_login_attempts()
user.login_attempts_f()
user.increment_login_attepmts(3)
user.login_attempts_f()

# наследование 16.06.26

class Battery():
	def __init__(self, battery_size = 75):
		self.battery_size = battery_size

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh battery")

	def get_range(self):
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge")

	def upgrade_battery(self):
		if self.battery_size <= 100:
			self.battery_size = 100

class ElecticCar(Car):
 	def __init__(self, make, model, year):
 		super().__init__(make, model, year)
 		self.battery = Battery()

 	def fill_gas_tank(self):
 		print("Electric car has not gas tank")

my_tesla = ElecticCar('tesla', 'model_s', 2019)
print(f"\n{my_tesla.get_descriptive_name()}")
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# упражнения

class IceCreamStand(Restaraunt):
	def __init__(self, *flavors):
		self.flavors = flavors

	def icecream_flavors(self):
		print(f"IceCream flavors: ")
		for flavor in self.flavors:
			print(f"\t{flavor}")


icecream = IceCreamStand('piska', 'cum', 'creampie')
icecream.icecream_flavors()

class Privileges():
	def __init__(self, *privileges):
		self.privileges = privileges

	def show_privileges(self):
		print(f"Your privileges:")
		for privilege in self.privileges:
			print(f"\tYou can {privilege}")


class Admin(User):
	def __init__(self, first_name, last_name, *privileges):
		self.privileges = Privileges(*privileges)

adminchek = Admin('gesha', 'pines', "write messages", "ban users", "delete users", "mute users")
adminchek.privileges.show_privileges()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# импортирование классов 17.06.26

from Module_for_Classes import Car

print('')

my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

from Module_for_ElectricCar import ElecticCar

print('')

my_tesla = ElecticCar('tesla', 'model_s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

from Module_for_Classes import Car
from Module_for_ElectricCar import ElecticCar

print('')

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

print('')

my_tesla = ElecticCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

import Module_for_Classes as MfC
import Module_for_ElectricCar as MfE

print('')

my_beetle = MfC.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

print('')

my_tesla = MfE.ElecticCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

from Module_for_Classes import Car
from Module_for_ElectricCar import ElecticCar as EC

print('')

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

print('')

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# упражнения

import Module_Restaraunt as MR

print('')

restaraunt = MR.Restaraunt('pineseses', '6.7 stars')
print(restaraunt.describe_restaraunt())


import Module_Admin as MA

print('')

adminchek = MA.Admin('gesha', 'pines', "write messages", "ban users", "delete users", "mute users")
print(adminchek.privileges.show_privileges())


adminik = MA.Admin('pines', 'fibr', "write messages", "ban users")
print(adminik.privileges.show_privileges())

# стандартная библиотека Python 18.06.26

# >>> from random import randint
# >>> randint(1, 6)
# 3

# >>> from random import choice
# >>> players = ['charles', 'martina', 'michael', 'florence', 'eli']
# >>> first_up = choice(players)
# >>> first_up
# 'florence'

#упражнения

import random

class Die():
	def __init__(self, sides = 20):
		self.sides = sides

	def roll_die(self):
		num = random.randint(1, self.sides)
		print(f"Num: {num}")

cube = Die()
for chislo in range(10):
	cube.roll_die()

from random import choice

listik = [2, 'a', 3, 5, 'v', 7, 11, 'd', 'e', 'w', 13, 17, 23, 29, 31]

def get_biletik(*args):
	num = str(choice(args))
	return num

ticket = get_biletik(*listik) + get_biletik(*listik) + get_biletik(*listik) + get_biletik(*listik)
print(F"Biletik code: {ticket}")

my_ticket = ['a', 7, 11, 'w']

def generate_ticket(nums, length = 4):
	return random.choices(nums, k = length)

attempts = 0
win_ticket = []

while win_ticket != my_ticket:
	win_ticket = generate_ticket(listik)
	attempts += 1

print(f"Win Biletik: {win_ticket}")
print(f"Your Biletik: {my_ticket}")
print(f"Attempts: {attempts}")

# кончил 18.06.26




