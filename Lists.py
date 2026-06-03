bicycles = ['specialized', 'basic', 'nebasic', 'nespecialized']
print(bicycles[2].upper())
print(bicycles[1])
print(bicycles[-1])
print(bicycles[-3].title())
mes = f"My first bicycle was a {bicycles[2]}."
print(mes)
# ниже упражнения
vegetables = ['totato', 'waterlemon', 'cicimber', 'pupkin']
message = f"I like vegetables such as {vegetables[0]}, {vegetables[3]}."
print(message)

names = ['Misha', 'Dima', 'Vayas']
mesmes = f"My friends:\n\t{names[0]} - pituh\n\t{names[1]} - pidro\n\t{names[2]} - jiffri robinson"
print(mesmes)

Kars = ['motosrycle', 'kar', 'Vertoletik']
karsiki = f"I would like to buy the {Kars[2]}"
print(karsiki)
# тема
motocrysers = ['honda', 'kawasaki','porno']
motocrysers[2] = 'estriper'
print(motocrysers)
motocrysers.append('kago')
print(motocrysers)

crycers = []
crycers.append('crico')
crycers.append('piper')
crycers.append('broke')
print(crycers)

motocrysers.insert(0, 'criko')
print(motocrysers)

del motocrysers[1]
print(motocrysers)

popped_motocrycer = motocrysers.pop(2)
print(motocrysers)
# упражнился
mes = f"Bedni motocryser {popped_motocrycer}."
print(mes)
# дальше
motocrysers.remove('kawasaki')
print(motocrysers)
# упражнения
guests = ['chel', 'human', 'chelik', 'bratok']
popped_g = guests.pop(2)
m = f"I would like to invite guest - {guests[1]}"
print(m)
print(guests)
print(popped_g)
guests.insert(0, 'piplik')
guests.insert(2, 'peple')
guests.append('peoples')
print(guests)
popped_guest = guests.pop(1)
poppd_guest = guests.pop(4)
mesasageo = f"I so apologize, {poppd_guest}, {popped_guest}, table is full of another guests"
print(mesasageo)
# сортировка
Kars = ['bmw', 'audi', 'hentai', 'changan']
print(Kars)
print(sorted(Kars))
print(Kars)
Kars.reverse()
print(Kars)
Kars.reverse()
print(Kars)
# упражнения
Countries = ['Norway', 'Germany', 'USA', 'Greece', 'Ciprus']
print(Countries)
print(sorted(Countries))
print(Countries)
print(sorted(Countries, reverse=True))
print(Countries)
Countries.reverse()
print(Countries)
Countries.reverse()
print(Countries)
Countries.sort(reverse=True)
print(Countries)

anything = []
anything.append('rivers')
anything.append('cities')
anything.append('towns')
anything.append('cars')
anything.append('planes')
anything.append('ships')
anything.sort()
anything[3] = 'spaceships'
anything.insert(6, 'countries')
del anything [2]
popped = anything.pop(1)
mes = f"I like big {popped}, but {anything[3]} always calm."
print(anything)
print(mes)
print(anything[-2])
# конец темы списки 26.05.26 (сегодня был выпускной)
# тут работа со списками 27.05.26
magicians = ['avdol', 'red', 'gudini']
for magician in magicians:
	print(f"{magician.title()}, you are a good magician")
	print(f"Suck my dick, {magician.title()}.\n")
print("Sixseven")
# упражнения
pizzas = ['mozarella', 'pepperoni', 'four cheeses']
for pizza in pizzas:
	print(f"I like {pizza.upper()} pizza")
print("I really like pizzas!")	
animals = ['misha', 'dima', 'cat', 'dog', 'turtle']
for animal in animals:
	print(f"{animal.title()} can be pet.")
print("Every animal can be pet")
# числовые списки
for value in range(-2, 8):
	print(value)
numbers = list(range(1,6))
print(numbers)
even_nums = list(range(2,11,7))
print(even_nums)
squares = []
for value in range(1,21):
	square = value**2
	squares.append(square)
print(squares)
# генераторы списков
squares = [value**2 for value in range(1,11)]
print(squares)
# упражнения
nums = []
for num in range(1,21,5):
	nums.append(num)
print(nums)
millions = []
for mil in range(1,1000001):
	millions.append(mil)
nechetkiy = list(range(1,20,2))
print(nechetkiy)
for three in range(3,30,3):
	print(three)
cubes = []
for cube in range(1,11):
	value = cube**3
	cubes.append(value)
print(cubes)
cubess = [value**3 for value in range(1,11)]
print(cubess)
# кончил
# работа с частями списка 28.05.26
players = ['ronalido', 'messisi', 'missisipi', 'neumar', 'vkamineshestutra']
print(players[0:3])
print(players[2:6])
print(players[:4])
print(players[3:])
print(players[-3:])
print(players[:-3])
print(players[0:5:2])
for player in players[2:4]:
	print(player.title())
print(players[:])
food = ['pizda', 'apples', 'bananas', 'pines']
friend_f = food[:]
food.append('avocado')
friend_f.append('ice cream')
print(f"My favorite foods are:\n{food}\n")
print(f"My friend's favorite foods are:\n{friend_f}")
# упражнения
balloons = ['green', 'blue', 'yellow', 'red', 'pink']
print(balloons[0:2]) 
print(f"The first three balloons in the list are:\n{balloons[:3]}")
print(f"Three balloons from the middle of the list are:\n{balloons[1:4]}")
print(f"The last three balloons in the list are:\n{balloons[2:]}")
fr_pizdas = pizzas[:]
fr_pizdas.append('pineapples')
pizzas.append('apples')
print(f"My pizzas are:\n\t{pizzas}\nMy friend's pizzas are:\n\t{fr_pizdas}")
for pizza in pizzas:
	print(pizza)
for pizza in fr_pizdas:
	print(pizza)
# кортежи(списки с неизменяемыми значениями)
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
print('Original dimensions:')
for dim in dimensions:
	print(dim)
dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
# упражнения
sweden_s_table = ('chiken', 'kurito', 'losos', 'lemonchiki')
for bludo in sweden_s_table:
	print(bludo)
sweden_s_table = ('chiken', 'losos', 'karasik', 'crocodile')
for food in sweden_s_table:
	print(food)
# кончил 28.05.26