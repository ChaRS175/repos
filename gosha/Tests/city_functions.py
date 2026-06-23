def city_functions(city, country, river = ''):
	if river:
		city_f = f"{city}, {river}, {country}"
	else:
		city_f = f"{city}, {country}"
	return city_f.title()