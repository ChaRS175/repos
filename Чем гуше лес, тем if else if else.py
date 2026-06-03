Kars = ['audi', 'bmw', 'hentai', 'toyota', 'chevrolet']
for kar in Kars:
	if kar == 'bmw':
		print(kar.upper())
	else:
		print(kar.title())
requested_topping = 'mushrooms'
if requested_topping != 'anchovy':
	print("Nahuy mne tvoy anchous?")
answer = 39.5
if answer != 59.5:
	print("You are pizdabol, otvet 39.5, daun")
pidor_ban = ['picun', 'pidor', 'ueba', 'dima']
user = "piskotryas"
if user not in pidor_ban:
	print(f"{user.title()}, you are not banned :)")
# упражнения
ya = "pidor"
print("Am ya == 'pidor'? I predict True")
print(ya == 'pidor')
print("\n Am ya == 'gay'? I predict False")
print(ya == 'gay')
print(" ya == pidoras?")
print(ya == 'pidoras')

n = 'pines'
print(f"\n{n == 'pines'}")
print(n == 'penis')
print(f"\n{n.lower() == 'PINES'}")
print(f"{n.lower() == 'pines'}")
num = 67
if num == 6.7 or 67:
	print("SIIIIIIIIIIXXXSEVEEEEEEEEEEENNN")
else:
	print("ne sixseven :()")
if num > 67 and 6.7:
	print("number is more than SIIIIIIIIIIXXXSEVEEEEEEEEEEENNN")
else:
	print("SIIIIIIIIIIXXXSEVEEEEEEEEEEENNN")
# дальше робiть
vote_age = 18
if vote_age >= 18:
	print("You can vote")
else:
	print("You can disappear to dildo")

age = 17
if age < 4:
	price = 1
elif age > 4 and age < 18:
	price = 7
else:
	price = "dohuya, you will never pay this ticket"
print(f"Your ticket cost is $ {price}")

toppings = ['spirma', 'concha', 'molochko', 'milk']
if 'spirma' in toppings:
	top = 'spirma'
	print(f"Please add {top}")
if 'concha' in toppings:
	top = 'concha'
	print(f"Please add {top}")
if 'milk' in toppings:
	top = 'milk'
	print(f"Please add {top}")
if 'sperma-milk' in toppings:
	top = 'sperma-milk'
	print(f"Please add {top}")
# упражнения
color = 'green'
if color == 'green':
	print("You have got 5 points!")
else:
	print("You have got 10 points!")
color = 'red'
if color == 'green':
	print("You have got 5 points!")
elif color == 'yellow':
	print("You have got 10 points!")
elif color == 'red':
	print("You have got 15 points!")

age = 67
if age < 2:
	print("Newborn")
elif age >= 2 and age < 4:
	print("Baby")
elif age >= 4 and age < 13:
	print("Kid")
elif age >= 13 and age < 20:
	print("Teenager")
elif age >= 20 and age < 65:
	print("Adult")
elif age >= 65:
	print("Old")

fruits = ['apple', 'banana', 'kiwi', 'orange']
if 'kiwi' in fruits:
		print('You really like kiwi')
if 'banana' in fruits:
		print("You really like banana")
if 'apple' in fruits:
		print("You really like apple")
if 'orange' in fruits:
		print("You really like orange")
# дальше
top = ['pepperoni','shrooms', 'peppers', 'cheese']
for topp in top:
	if topp == 'pepperoni':
		print("Sorry, we are out of pepperoni")
	else:
		print(f"Add {topp}")

top = []
if top:
	for topp in top:
		print(f"Add {topp}")
else:
	print("OK")
tops = ['olives', 'marshmellow', 'french fries', 'pineapple', 'cheese']
tops_s = ['olives', 'apples', 'cheese']
for toppp in tops_s:
	if toppp in tops:
		print(f"Add {toppp}")
	else:
		print(f"Sorry, we dont have {toppp}")
# упражнения
users = ['adam', 'hussein', 'saddam', 'admin', 'peder']
if users:
	for user in users:
		if user == 'admin':
			print(f"Hello {user.title()}")
		elif user != 'admin':
			print(f"Hello random user {user.title()}")
else:
	print("We need to ind some users")

cur_users = ['adam', 'max', 'dima',  'geysha']
new_users = ['geysha', 'MAX', 'sergay', 'gayorgy', 'dima']
for name in cur_users:
	if name in new_users:
		print(f"Your name is old, {name.title()}, please write another name")
	else:
		print(f"Your name is new, {name.title()}, you can use this name")

nums = [1,2,3,4,5,6,7,8,9]
for num in nums:
	if num == 1:
		print(f"{num}st")
	if num == 2:
		print(f"{num}nd")
	if num == 3:
		print(f"{num}rd")
	if num >= 4:
		print(f"{num}th")
	# кончил 30.05.26