import matplotlib.pyplot as plt

def scatter_squares():
	x_values = list(range(1, 1001))
	y_values = [x**2 for x in x_values]

	plt.style.use('bmh')
	fig, ax = plt.subplots()
	# можно задать цвет аргументом c = 'цвет'
	# еще цвет можно задать, используя RGB, но от 0 до 1(дробными): c = (0, 0.8, 0)
	# существует цветовая карта(colormap), образующая градиент точек(например чем больше значение, тем точка темнее)
	# 	Все цветовые карты, доступные в pyplot, можно просмотреть на сайте
	# 	http://matplotlib org/; откройте раздел Examples, прокрутите содержимое до пункта Color
	# 	и щелкните на ссылке Colormaps_reference
	ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Greens, s = 10) 

	ax.set_title("Square nums", fontsize = 24)
	ax.set_xlabel('Value', fontsize = 14)
	ax.set_ylabel('Square of value', fontsize = 14)

	ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

	# Метод axis() получает четыре значения: минимум и максимум по осям x и y
	ax.axis([0, 1100, 0, 1100000]) 

	plt.show()
	#	Если вы хотите, чтобы программа автоматически сохраняла диаграмму в файле,
	#	замените вызов plt.show() вызовом plt.savefig():
	#	plt.savefig('squares_plot.png', bbox_inches='tight'). Второй аргумент отсекает от диа-
	#	граммы лишнее пространство. Если вы хотите оставить пустые места вокруг диа-
	#	граммы, этот аргумент можно опустить.

# упражнения Кубы и Цветные кубы 18.07.26


	# values = [1, 2, 3, 4, 5]
	# cubes = [1, 8, 27, 64, 125]
values = list(range(1, 1001))
cubes = [x**3 for x in values]

plt.style.use('bmh')
fig, ax = plt.subplots()

ax.scatter(values, cubes, c = cubes, cmap = plt.cm.Reds, s = 20)

ax.set_title("Cubes", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Cube of value", fontsize = 14)

ax.tick_params(axis = 'both', which = 'major', labelsize = 14 )

ax.axis([0, 1000, 0, 1000000000])

plt.show()

