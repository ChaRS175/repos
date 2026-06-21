with open('Ya_Pi_ya_Pi_ya_Pi_Pi_Pi.txt') as file_object:
# with open('папка_в_которой_хранится_файл/имя_файла.txt') as file_object:
	contents = file_object.read()

print(contents.rstrip())

print('')

file_path = "/Users/minec/OneDrive/Рабочий стол/repos/gosha/Files_and_exceptions/Ya_Pi_ya_Pi_ya_Pi_Pi_Pi.txt"
with open(file_path) as file_object:
	contents = file_object.read()

print(contents)

print('')

filename = 'Ya_Pi_ya_Pi_ya_Pi_Pi_Pi.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

Ya_Pi_ya_Pi_ya_Pi_Pi_Pi = ''
for line in lines:
	Ya_Pi_ya_Pi_ya_Pi_Pi_Pi += line.strip()

print(f"{Ya_Pi_ya_Pi_ya_Pi_Pi_Pi[:52]}...")
print(len(Ya_Pi_ya_Pi_ya_Pi_Pi_Pi))

def birthday_file():

	birthday = input("Enter your birthday, in the form mmddyy: ")
	if birthday in Ya_Pi_ya_Pi_ya_Pi_Pi_Pi:
		print("Your birthday appears in the first million digits of Pi")
	else:
		print("Your bithday does not appear in the first million digits of Pi")

	

# упражнения

with open('python.txt') as piton:
	data = piton.read()

print(data)

print('')

with open('python.txt') as piton:
	lines = piton.readlines()
	for line in lines:
		print(line.rstrip())

print('')

with open('python.txt') as piton:
	lines = piton.readlines()
	python = ''
	for line in lines:
		python += line.strip()


print(python[:30])
print(python[30:77])
print(python[77:])

# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'

# запись в файл 20.06.26

filename = 'programming.txt'

with open(filename, 'w') as file:
	file.write('I love programming\n')
	file.write('pines\n')
	file.write('I love pines')

# упражнения

filekurinoe = 'guest.txt'

def guest():
	with open(filekurinoe, 'a') as file:
		while True:
			filegovyazhye = input("Enter your name: ")
			if filegovyazhye == 'q':
				break
			else:
				file.write(f"{filegovyazhye}\n")
		
filekurinoe = 'guest_book.txt'

def guest_book():
	with open(filekurinoe, 'a') as file:
		while True:
			filebaranye = input("Enter your name: ")
			if filebaranye == 'q':
				break
			else:
				file.write(f"New guest {filebaranye.title()}\n")

filekurini = 'plot_about_programming.txt'

def krisi_ne_lublu_eti_vashi_mishi():
	with open(filekurini, 'a') as file:
		while True:
			file_krisi_ne_lublu_eti_vashi_mishi = input("Why you like the programming? ")
			if file_krisi_ne_lublu_eti_vashi_mishi == 'q':
				break
			else:
				file.write(f"{file_krisi_ne_lublu_eti_vashi_mishi}\n")

# исключения 21.06.26

print('')

try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero\n")

def divide_by_zero():
	print("Enter two numbers, and i'll divide them")
	print("Enter 'q' to quit")

	while True:
		first_num = input("\nFirst num: ")
		if first_num == 'q':
			break
		second_num = input("Second num: ")
		if second_num == 'q':
			break
		try:
			answer = int(first_num)/int(second_num)
		except ZeroDivisionError:
			print("You can't divide by zero")
		else:
			print(answer)

print('')

def count_words(filename):
	try:
		with open(filename, encoding = 'utf-8') as file:
			contents = file.read() 
	except FileNotFoundError:
		print(f"File {filename} does not exist") # pass просто скипает файл, который вызывает ошибку
	else:
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words")

filenames = ['txt.txt', 'python.txt', 'programming.txt']
for filename in filenames:
	count_words(filename)

# >>> title = "Alice in Borderland"
# >>> title.split()
# ['Alice', 'in', 'Borderland']

# упражнения

print('')
def sum():
	num1 = input("\nNum №1: ")
	num2 = input("Num №2: ")
	try:
		answer = int(num1) + int(num2)
	except ValueError:
		print("Ты даун блять складывать буквы и символы??")
	else:
		print(answer)

def multiplication():
	print("Enter two numbers, and I'll sum them")
	print("Enter 'q' to quit")

	while True:
		num1 = input("\nNum №1: ")
		if num1 == 'q':
			break
		num2 = input("Num №2: ")
		if num2 == 'q':
			break
		try:
			answer = int(num1) * int(num2)
		except ValueError:
			print("Ты даун блять умножать буквы и символы??")
		else:
			print(answer)

def cats_and_dogs(file):
	try:
		with open(file, encoding = 'utf-8') as f:
			content = f.read()
	except FileNotFoundError:
		print(f"File {file} does not exist")
	else:
		words = content.split()
		num_words = len(words)
		print(f"Num of words in {file}: {num_words}")

files = ['cats.txt', 'dogs.txt']
for file in files:
	cats_and_dogs(file)

line = "Pines, pines, pines, pines, PINES, pineapples"
print(line.count('pines'))
print(line.lower().count('pines'))

# сохранение данных 22.06.26


