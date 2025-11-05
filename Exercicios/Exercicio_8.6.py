def city_country(city,country):
    message = (city.title()  + ', ' + country.title() + '.')
    return message

while True :
    city = input('Digite uma cidade: ')
    if city == 'quit':
        break
    country = input('Digite o pais que ela pertence: ')
    if country == 'quit':
        break
    
    message = city_country(city,country)
    print(message)