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


restaurant = Restaurant('pertinho de minas','comida mineira')

print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
print('Pessoas servidas ' + str(restaurant.number_served))

restaurant.set_number_served(145)
print('Pessoas servidas ' + str(restaurant.number_served))

restaurant.increment_number_served(246)
print('Pessoas servidas ' + str(restaurant.number_served))

restaurant.describe_restaurant()
restaurant.open_restaurant()
