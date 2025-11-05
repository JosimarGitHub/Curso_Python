def city_country(city, country, population = 0):
    if population == 0:
        print(city.title() + ", " + country.title())
    else:
        print(city.title() + ", " + country.title() + " - população " + str(population))