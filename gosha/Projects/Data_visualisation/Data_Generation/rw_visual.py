# 19.07.26

import matplotlib.pyplot as plt

from random_walk import RandomWalk

def rw_visual():
	while True:
		rw = RandomWalk()
		rw.fill_walk()

		plt.style.use('classic')
		fig, ax = plt.subplots(figsize = (15, 11))
		point_nums = range(rw.num_points)
		ax.scatter(rw.x_values, rw.y_values, c = point_nums, cmap = plt.cm.Blues,
			edgecolors = 'none', s = 10)
		ax.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
		ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)

		plt.show()

		keep_running = input("Make another walk? (y/n): ")
		if keep_running == 'n':
			break
		else:
			continue

# упражнения

def exercise():
	while True:
		rw = RandomWalk()
		rw.fill_walk()

		plt.style.use('classic')
		fig, ax = plt.subplots(figsize = (15, 11))
		point_nums = range(rw.num_points)
		ax.plot(rw.x_values, rw.y_values, linewidth = 3)
		ax.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
		ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)

		plt.show()

		keep_running = input("Make another walk? (y/n): ")
		if keep_running == 'n':
			break
		else:
			continue

exercise()

# кончил 20.07.26