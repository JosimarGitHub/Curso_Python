def make_car(marca, modelo, **caracteristicas):
    
    """ Fazer um carro """ 
    car = {}

    car['Marca'] = marca
    car['Modelo'] = modelo
    for key, value in caracteristicas.items():
        car[key] = value
    return car

car = make_car('Chevrolet', 'Prisma',
            cor='cinza',
            submodelo='LTZ',
            Auto_Manual = 'Automático',
            Alcoo_Gasolina='Alcoo/Gasolina',
            Rodas='Liga Leve')
car02 = make_car('Chevrolet', 'Prisma',
            cor='Preto')


print(car)
print(car02)

