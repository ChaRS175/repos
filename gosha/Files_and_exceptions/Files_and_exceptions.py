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

# упражнение 10.2 осталось, а дальше Запись в файл 20.06.26




