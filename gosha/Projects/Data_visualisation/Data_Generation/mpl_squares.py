import matplotlib.pyplot as plt

def Squares():
	input_values = [1, 2, 3, 4, 5]
	squares = [1, 4, 9, 16, 25]

	plt.style.use('bmh')
	fig, ax = plt.subplots()
	ax.plot(input_values, squares, linewidth = 3)

	# Назначение заголовка диаграммы и меток осей
	ax.set_title("Square Numbers", fontsize = 24)
	ax.set_xlabel("Value", fontsize = 14)
	ax.set_ylabel("Square of Value", fontsize = 14)

	# Назначение размера шрифта на осях
	ax.tick_params(axis = 'both', labelsize = 14)

	plt.show()

	# как узнать какие стили цвета фона, линий сетки,
	# 	толщины линий, шрифтов, размера шрифтов есть в моей системе
	# >>> import matplotlib.pyplot as plt
	# >>> plt.style.available
	# ['seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks', 'fivethirtyeight',
	# ...