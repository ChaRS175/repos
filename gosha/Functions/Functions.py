# начал 10.06.26
def greet_user(name):
	"""Выводит приветствие"""
	print(f"Hello, {name.title()}")

greet_user('pines')

# упражнения 

def message():
	print('Theme about functions')

message()

def favourite_book(title):
	print(f'One of my favourite books is {title.title()}')

favourite_book('alice in borderland')

# дальше

def describe_pet(pet_name, animal_type = 'dog'):
	print(f"\nI have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('cat', 'bonnie')
describe_pet('hamster', 'hamstercombat')

describe_pet('whale')

# упражнения

def make_shirt(size, text = 'pines'):
	print(f"\nShirt size: {size}")
	print(f"Text on shirt: {text.title()}")

make_shirt(48)
make_shirt(52)

def make_shirts(size = 'L', text = 'I love Python'):
	print(f"\nShirt size: {size}")
	print(f"Text on shirt: {text}")

make_shirts('M', 'I love Pines')

def describe_city(city = 'kair', country = 'egypt'):
	print(f"{city.title()} is in {country.title()}")

describe_city('berlin', 'germany')

# возвращение значения

def get_name(firstname, lastname, middlename = ''):
	if middlename:
		full_name = f"\n{firstname} {middlename} {lastname}"
	else:
		full_name = f"\n{firstname} {lastname}"
	return full_name.title()

musician = get_name('michael', 'jackson', 'king')
print(musician)

# возвращение словаря

def build_person(firstname, lastname, age = ''):
	person = {'first': firstname, 'last': lastname}
	if age:
		person['age'] = age
	return person

musician = build_person('michael', 'jackson', age = 50)
print(musician)

# использование функции в цикле while 11.06.26

def form_name():
	def get_formatted_name(first_name, last_name):
		full_name = f"{first_name} {last_name}"
		return full_name.title()

	while True:
		print("\nPlease tell me your name: ")
		print("Enter q or quit to exit")
		f_name = input("Firstname: ")
		if f_name == 'q' and 'quit':
			break
		l_name = input("Lastname: ")
		if l_name == 'q' and 'quit':
			break

		formatted_name = get_formatted_name(f_name, l_name)
		print(f"\nHello, {formatted_name.title()}")

		mes = input("\nWould you like let other people continue? (y/n) ")
		if mes == "n":
			break



# упражнения

def city_country(city, country):
	print(f"{city.title()}, {country.title()}")

city_country('brazilia', 'brazil')
city_country('kamyshin', 'russia')
city_country('london', 'united kingdom')

# def make_album(name, title, lines = ''):
# 	alb = {'Name': name.title(), 'Title': title.title()} 
# 	if lines:
# 		alb['lines'] = lines
# 	return alb

# while True:
# 	print("\nEnter name of musician and title of album: ")
# 	name = input("Name of musician: ")
# 	if name == 'q' and 'quit':
# 		break
# 	title = input("Title of album: ")
# 	if title == 'q' and 'quit':
# 		break
# 	album = make_album(name, title)
# 	print(f"{album}")

# 	message = input("\nWould you like to add other albums? (y/n) ")
# 	if message == 'n':
# 		break

# передача списка 12.06.26

def greet_users(names):
	for name in names:
		msg = f"Hello, {name.title()}"
		print(msg)

usernames = ['yan', 'pines', 'fibrik']
greet_users(usernames)

def print_models(unprinted, completed):
	while unprinted:
		cur_design = unprinted.pop()
		print(f"Printing model: {cur_design}")
		completed.append(cur_design)

def show_completed(completed):
	print("\nThe following models have been printed: ")
	for complete in completed:
		print(complete)

unprinted = ['phone case', 'robot pend']
completed = []

print_models(unprinted[:], completed)
show_completed(completed)

# упражнения

msgs = ['pines you are pines', 'msg msg msg', 'pst pst, pst pst']

def show_msgs(msg):
	for msg in msgs:
		print(msg)

show_msgs(msgs)


def send_msgs(msgs, sent_msgs):
	while msgs:
		msg = msgs.pop()
		print(f"Not sent messages: {msg}")
		sent_msgs.append(msg)

def show_msgs(msg):
	print("\nSent messages: ")
	for msg in sent_msgs:
		print(msg)

sent_msgs = []

send_msgs(msgs [:], sent_msgs)
show_msgs(msgs)

print(msgs)

# передача произвольного набора аргументов 13.06.26

def make_pizza(size, *toppings):
	print(f"Making pizza {size}-centimeters")
	for top in toppings:
		print(f"- {top}")

make_pizza(30, 'pepperoni\n')
make_pizza(35,'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **userinfo):
	userinfo['firstname'] = first
	userinfo['lastname'] = last
	return userinfo

user_profile = build_profile('albert', 'epstein', location = 'germany', interest = 'physics')
print(user_profile)

# упражнения

def sandwich_components(*component):
	print(component)

sandwich_components('lettuce')
sandwich_components('toast', 'meat')

def build_profile(name, surname, **list_of_smth):
	list_of_smth['name'] = name.title()
	list_of_smth['surname'] = surname.title()
	return list_of_smth

var = build_profile('gesha', 'pines', location = 'russia', age = 15, interest = 'math')
print(var)

def car(producer, mark, **car_info):
	car_info['producer'] = producer.title()
	car_info['mark'] = mark.title()
	return car_info

Kars = car('bmw', 'bmw', color = 'blue', model = 'X8')
print(Kars)

# хранение функций в модулях

import Module_for_Functions

Module_for_Functions.make_pizza(30, 'pepperoni')
Module_for_Functions.make_pizza(35, 'mushrooms', 'green peppers', 'cheese')

# импортирование конкретных функций

from Module_for_Functions import make_pizza
# from Module_for_Functions import 1function, 2function, 3function и т.д.
make_pizza(24, 'pepperoni')
make_pizza(67, 'mushrooms', 'green peppers', 'cheese')

# назначение псевдонима(alias(as)) для функции

from Module_for_Functions import make_pizza as mpz

mpz("6-7", 'pepperoni')
mpz(67, 'mushrooms', 'cheese')

# назначение псевдонима для модуля

import Module_for_Functions as MfF
MfF.make_pizza(14, 'pepperoni')
MfF.make_pizza(23, 'mushrooms', 'peppers')

# импортирование всех функций модуля

from Module_for_Functions import * # <-- импорт всех функций

make_pizza(27, 'mushrooms')
make_pizza(38, 'cheese\n')

# упражнения 

import Module_for_print_models as Mfpm

Mfpm.print_models(unprinted, completed)

from Module_for_print_models import print_models as pm

pm(unprinted, completed)

# кончил тему 13.06.26









