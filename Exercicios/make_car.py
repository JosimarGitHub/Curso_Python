def make_car(
        marca,
        modelo,
        **caracteristicas):
    
    """ Fazer um carro """ 
    car = {}

    car['Marca'] = marca
    car['Modelo'] = modelo
    for key, value in caracteristicas.items():
        car[key] = value
    return car