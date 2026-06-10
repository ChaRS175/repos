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