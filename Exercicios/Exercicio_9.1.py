class Restaurant():

    """Modelando um Restaurante"""
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Descrição do Restaurante:')
        print('Nome - ' + self.restaurant_name.title())
        print('Tipo - ' + self.cuisine_type.title())
        
    def open_restaurant(self):
        print('Restaurante aberto ás 19:00')


restaurant = Restaurant('pertinho de minas','comida mineira')

print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()