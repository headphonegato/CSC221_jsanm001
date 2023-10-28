def city_country(city, country):
 return f"{city.title()}, {country.title()}"
city = city_country('NYC', 'USA')
print(city)

city = city_country('Ossining', 'USA')
print(city)

city = city_country('Peekskill', 'USA')
print(city)


def city_country(city, country, population):
    """Return a string like 'Santiago, Chile - population 5000000'."""
    output_string = f"{city.title()}, {country.title()}"
    output_string += f" -population {population}"
    return output_string
