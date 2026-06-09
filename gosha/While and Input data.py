# начал тему 07.06.26(сегодня в америке 06.07.26 типа сиксевен)

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Enter your name: ")
# print(f"Hello {name.title()}")

# prompt = "If you tell us who are you, we can personalize tha messages that you will see.\nWhat is your name?\n"

#ИЛИ

# prompt = "If you tell us who are you, we can personalize tha messages that you will see.\n"
# prompt += "What is your name?\n"

# name = input(prompt)
# print(f"Hello, {name.title()}")

# height = input("How tall are you, in centimeteres?\n")
# height = int(height)
# if height >= 150:
# 	print("\nYou are tall enough to ride")
# else:
# 	print("\nYou are not tall enough to ride")

# num = input("Enter a number, and I will tell you if it's even or odd:\n")
# num = int(num)
# if num % 2 == 0:
# 	print(f"The number {num} is even")
# else:
# 	print(f"The number {num} is odd")

# упражнения

# car = input("What car you like:\n")
# print(f"I will find car like a {car}")

# num_of_ppl = input("How much people will come with you?\n")
# num_of_ppl = int(num_of_ppl)
# if num_of_ppl > 8:
# 	print(f"{num_of_ppl} people too much, please wait")
# else:
# 	print(f"We have table for {num_of_ppl} people")

# num10 = input("Write number, and I tell you if it's even or odd:\n")
# num10 = int(num10)
# if num10 % 10 == 0:
# 	print(f"Number {num10} is divisible by 10")
# else: 
# 	print(f"Number {num10} is not divisible by 10")

# продолжил 08.06.26

current_num = 1
while current_num <= 5:
	print(current_num)
	current_num += 1

prompt = "\nEnter the name of city, that you want visit: " + "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
# 	message = input(prompt)
# 	if message != 'quit':
# 		print(message)

# active = True
# while active:
# 	message = input(prompt)
# 	if message == 'quit':
# 		active = False
# 	else:
# 		print(message)

# while True:
# 	city = input(prompt)
# 	if city == 'quit':
# 		break
# 	else:
# 		print(f"I'd to go to {city.title()}")

cur_num = 0
while cur_num < 10:
	cur_num += 1
	if cur_num % 2 == 0:
		continue
	print(cur_num)

x = 1
while x <= 5:
	print(x)
	x += 1

# упражнения 

# pizza = "\nWrite name of pizza, that you would like to order: "
# while True:
# 	mes = input(pizza)
# 	if mes == 'quit':
# 		break
# 	else:
# 		print(mes)

# age = input("Write your age: ")
# age = int(age)
# while True:
# 	if age < 3:
# 		cost = "$0"
# 		print(f"Your ticket cost is {cost}")
# 		break
# 	elif age >= 3 and age < 12:
# 		cost = "$10"
# 		print(f"Your ticket cost is {cost}")
# 		break
# 	elif age >= 12:
# 		cost = "$15"
# 		print(f"Your ticket cost is {cost}") 
# 		break
	
# Использование цикла While со списками и словарями 09.06.26

unconfirmed_users = ['zoophil', 'pdidi', 'brinemaps']
confirmed_users = []
while unconfirmed_users: 
	current_user = unconfirmed_users.pop()
	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'cat', 'swordfish', 'cat', 'hamstercombat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
while 'dog' in pets:
	pets.remove('dog')

print(pets)

# answers = {}

# active = True

# while active:
# 	name = input("What is your name? ")
# 	answer = input("\nWhat mountain would you like to climb? ")
# 	answers[name] = answer

# 	repeat = input("Would you like to let another people answer? (y/n)")
# 	if repeat == 'n':
# 		active = False
# print("\n---Poll Results---")
# for name, answer in answers.items():
# 	print(f"{name.title()} would you like to climb {answer.title()}?")

# упражнения

sandwich_orders = ['burger', 'buter', 'bulochka']
finished_in_sandwiches = []
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"Order: {sandwich}")
	finished_in_sandwiches.append(sandwich)
print(f"Finished in sandwiches: ")
for sandwich in finished_in_sandwiches:
	print(f"\t{sandwich}")


sandwiches = ['pastrami', 'pastrami', 'pepperoni', 'cheese', 'pastrami']
print(sandwiches)

while 'pastrami' in sandwiches:
	sandwiches.remove('pastrami')
print(sandwiches)

poll = {}
active = True

while active:
	name = input("What is your name? ")
	prefer = input("Where would you like have a rest? ")
	poll[name] = prefer

	repeat = input("Would you like let other people answer? (y/n)")
	if repeat == 'n':
		active = False

print("---Poll Results---")
for name, prefer in poll.items():
	print(f"{name.title()}, are you serious would like to visit {prefer.title()} for rest?")

# кончил 09.06.26 