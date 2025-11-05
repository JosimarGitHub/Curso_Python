class Restaurant():

    """Modelando um Restaurante"""
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def set_number_served(self, new_value):
        self.number_served = new_value
    
    def increment_number_served(self, increment_value):
        self.number_served += increment_value

    def describe_restaurant(self):
        print('Descrição do Restaurante:')
        print('Nome - ' + self.restaurant_name.title())
        print('Tipo - ' + self.cuisine_type.title())
        
    def open_restaurant(self):
        print('Restaurante aberto ás 19:00')


class IceCreamStand(Restaurant):
    
    """Definindo Modelo Pai"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['baunilha', 'chocolate', 'leite condensado', 'flocos', 'morango']
    
    def show_flavors(self):
        print('Os sabores de sorvete disponiveis são:')
        for flavor in self.flavors:
            print(flavor.title())




restaurant = IceCreamStand('mix', 'sorveteria')
restaurant.describe_restaurant()
restaurant.show_flavors()
    
    