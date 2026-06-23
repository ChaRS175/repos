from city_functions import city_functions

print("Enter 'q' to quit")

while True:
	city = input("Enter city name: ")
	if city == 'q':
		break
	country = input("Enter country name: ")
	if country == 'q':
		break

	cityty = city_functions(city, country)
	print(f"City functions: {cityty}")