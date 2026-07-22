import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, column_header in enumerate(header_row):
		print(index, column_header)

	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		high = int(row[5])
		low = int(row[6])
		dates.append(current_date)
		highs.append(high)
		lows.append(low)

# нанесение данных на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red')
plt.plot(dates, lows, c = 'blue')
# форматирование диаграммы
plt.title("Daily high and low temperatures - 2018", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()

#>>> from datetime import datetime
# >>> first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
# >>> print(first_date)
# 2018-07-01 00:00:00

# %A - Название дня недели (например, Monday)
# %B - Название месяца (например, January)
# %m - Порядковый номер месяца (от 01 до 12)
# %d - День месяца (от 01 до 31)
# %Y - Год из четырех цифр (например, 2019)
# %y - Две последние цифры года (например, 19)
# %H - Часы в 24-часовом формате (от 00 до 23)
# %I - Часы в 12-часовом формате (от 01 до 12)
# %p - AM или PM
# %M - Минуты (от 00 до 59)
# %S - Секунды (от 00 до 61)