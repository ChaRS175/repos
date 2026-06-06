alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])
new_points = alien['points']
print(f"You just earned {new_points} points!")
alien['x'] = 0
alien['y'] = 25
print(alien)

al = {}
al['color'] = 'red'
al['points'] = 10
print(f"alien is {al['color']} and give you {al['points']} points")
al['color'] = 'yellow'
al['points'] = 15
print(f"alien is {al['color']} and give you {al['points']} points now")

alien = {'x': 0, 'y': 25, 'speed': 'medium'}
print(f"Position: {alien['x']}")
alien['speed'] = 'fast'
if alien['speed'] == 'slow':
	x_increment = 1
elif alien['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien['x'] = alien['x'] + x_increment
print(f"New position: {alien['x']}")
print(al)
del al['points']
print(al)

fav_lang = {
	'zoophil': 'python',
	'sisis': 'c',
	'radik': 'ruby',
	'mojang': 'java'
}
lang = fav_lang['sisis'].title()
print(f"Sisis's favourite language is {lang}")

alien = {'color': 'green', 'speed': 'slow'}
point_value = alien.get('points', 'Nihuya u tebya points\n')
print(point_value)

# упражнения

person = {'name': 'kurtka', 'surname': 'brain', 'age': '27', 'place': 'none'}
print(person['name'].title())
print(person['surname'].title())
print(f"{person['age']} old")
print(person['place'])

fav_nums = {
	'kurtka': 27,
	'saddam': 15,
	'goida': 1488,
	'mista': 4,
	'pucci': 67
}
print(fav_nums['kurtka'])
print(fav_nums['saddam'])
print(fav_nums['goida'])
print(fav_nums['mista'])
print(fav_nums['pucci'])

glossary = {'if': 'если', 'else': 'иначе', 'del': 'delete', 'title': 'заголовок', 'upper': 'CAPS'}
print(f"if - {glossary['if']}")
print(f"else - {glossary['else']}")
print(f"del - {glossary['del']}")
print(f"title - {glossary['title'].title()}")
print(f"upper - {glossary['upper']}")

# перебор списков 1.06.26

user = {
	'username': 'kitagarin',
	'firstname': 'enrico',
	'lastname': 'pucci'
}
for key, value in user.items():
	print(f"\nKey: {key}")
	print(f"\nValue: {value.title()}")

for name, language in fav_lang.items():
	print(f"{name.title()}'s favourite language is {language.title()}")
for name in fav_lang.keys():
	print(name.title())
friends = ['zoophil', 'sisis', 'radiumik']
for name in fav_lang.keys():
	print(f"Hi {name.title()}")
	if name in friends:
		language = fav_lang[name].title()
		print(f"{name.title()}, I see you love {language}")
for name in friends:
		if name not in fav_lang.keys():
			print(f"{name.title()}, please take our poll")
for name in sorted(fav_lang.keys()):
	print(f"{name.title()}, thank you for taking the poll")
print("The following languages have been mentioned:")
for language in fav_lang.values():
	print(language.title())

langs = {'Java', 'C', 'Java', 'C++'}
print(langs)
# упражнения
glossary = {
			'if': 'если',
			'else': 'иначе',
			'del': 'delete',
			'title': 'Заголовок',
			'upper': 'CAPS',
			'lower': 'without CAPS',
			'print': 'write',
			'... = ...': 'variable',
			'... = [...]': 'list',
			'... = {}': 'dictionary'
			}
for word, PS in glossary.items():
	print(f"{word} - {PS}")

rivers_of_countries = {
	'nile': 'egypt',
	'volga': 'russia',
	'amazon': 'brazil',
}
for river, country in rivers_of_countries.items():
	print(f"The {river.title()} runs through {country.title()}")
for river in rivers_of_countries.keys():
	print(river.title())
print("")
for country in rivers_of_countries.values():
	print(country.title())

peoples = {
			'chel': 'c',
			'peple': 'java',
			'brok': 'python',
			'pepchik': 'php'
			}
peoples1 = ['chel', 'brotik']
for name, language in peoples.items():
	print(f"{name.title()}, I see you like {language.title()}")
	if name in peoples1:
		print(f"{name.title()}, you really love {language.title()}?")
	print(f"Thank you, {name.title()}, for your vote")
for name in peoples1:
	if name not in peoples:
		print(f"{name.title()}, please vote for your favourite language")

# дальше "Вложение" 2.06.26

alien1 = {'color': 'green', 'points': 5}
alien2 = {'color': 'yellow', 'points': 10}
alien3 = {'color': 'red', 'points': 15}
aliens = [alien1, alien2, alien3]

for alien in aliens:
	print(alien)

aliens = []

for alien_num in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

for alien in aliens[:5]:
	print(alien)

print("...")

print(f"Total number of aliens : {len(aliens)}")

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'cheese', 'pepperoni']
}

print(f"You ordered a {pizza['crust']} - crust pizza "
	"with following toppings:")

for top in pizza['toppings']:
	print("\t" + top)

fav_langs = {
	'Zane': ['python', 'C'],
	'saray':['java'],
	'grig': ['java_script', 'html'],
	'zoophil': ['python', 'C#']
}

for name, languages in fav_langs.items():
	if len(languages) == 1:
		print(f"\n {name.title()}'s favourite language is:")
	else:
		print(f"\n{name.title()}'s favourite languages are:")
	for language in languages:
		print(f"\t{language.title()}")

# дальше словарь в словаре 3.06.26

users = {'aepstein': {
			'firstname': 'albert',
			'lastname': 'epstein',
			'location': 'princeton'},
		 'cmarie': {
		 	'firstname': 'marie',
		 	'lastname': 'curie',
		 	'location': 'paris'
		 			}
		 }
for username, user_info in users.items():
	print(f"\nUsername: {username.title()}")
	full_name = f"{user_info['firstname']} {user_info['lastname']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")

# упражнения 

people = {
	'kurtka': {
	'name': 'kurtka',
	'surname': 'brain',
	'age': 27,
	'place': 'none'
	},
	'kurt': {
	'name': 'kurt',
	'surname': 'kombain',
	'age': 27,
	'place': 'land'
	}
}

for fname, lname in people.items():
	print(f"Name: {fname.title()}")
	f_name = f"{lname['name']} {lname['surname']}"
	age = lname['age']
	place = lname['place']
	print(f"\tFull name: {f_name.title()}")
	print(f"\tAge: {age}")
	print(f"\tPlace: {place.title()}")



sphere = {
			'name': 'sphere',
			'kind': 'hotdog',
			'name_owner': 'stan\n'
		 }

bosik = {
			'name': 'bonnie',
			'kind': 'cat',
			'name_owner': 'gesha'
		}

pets = [sphere, bosik]

for pet in pets:
	print(f"Name: {pet['name'].title()}")
	print(f"Kind: {pet['kind'].title()}")
	print(f"Owner name: {pet['name_owner'].title()}")

fav_places = {
	'forest': ['gesha', 'misha'],
	'town': 'nobody',
	'river': 'everybody'
			 }
for place, names in fav_places.items():
	if names == ['gesha', 'misha']:
		print(f"People, who likes {place}: {names[0].title()}, {names[1].title()}")
	else:
		print(f"People, who likes {place}: {names.title()}")

print('')

fav_nums = {
	'kurtka': [27],
	'saddam': [15],
	'goida': [1488],
	'mista': [4,44,444,4444],
	'pucci': [67]
		   }

for name, nums in fav_nums.items():
	if len(nums) == 1:
		print(f"{name.title()} likes this number:", *nums)
	else:
		print(f"{name.title()} likes these numbers:", *nums)

cities = {
	'kamyshin': {
		'country': 'russia',
		'population': 100000
				},
	'moscow': {
		'country': 'russia',
		'population': 13000000
			  },
	'berlin': {
		'country': 'germany',
		'population': 4000000 
			  }
		}

for city, city_info in cities.items():
	country = city_info['country']
	population = city_info['population']
	print(f"There is a {city.title()} in the country {country.title()}, and have population about {population} ")

# кончил всю главу 06.06.26

