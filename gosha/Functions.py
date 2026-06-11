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

def make_album(name, title, lines = ''):
	alb = {'Name': name.title(), 'Title': title.title()} 
	if lines:
		alb['lines'] = lines
	return alb

while True:
	print("\nEnter name of musician and title of album: ")
	name = input("Name of musician: ")
	if name == 'q' and 'quit':
		break
	title = input("Title of album: ")
	if title == 'q' and 'quit':
		break
	album = make_album(name, title)
	print(f"{album}")

	message = input("\nWould you like to add other albums? (y/n) ")
	if message == 'n':
		break

# передача списка 12.06.26





