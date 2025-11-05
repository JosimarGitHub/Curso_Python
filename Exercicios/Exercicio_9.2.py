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



restaurant01 = Restaurant('pertinho de minas', 'comida mineira')
restaurant02 = Restaurant('porteira de minas', 'churrascaria')
restaurant03 = Restaurant('so massas', 'massas')

restaurant01.describe_restaurant()
restaurant02.describe_restaurant()
restaurant03.describe_restaurant()