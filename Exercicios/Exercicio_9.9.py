class Car ():

    """Uma tentativa simples de representar um carro."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    
    """Uma tentativa simples de modelar uma bateria para um carro
    elétrico."""

    def __init__(self, battery_size=70):

        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size

    def describe_battery(self):

        """Exibe uma frase que descreve a capacidade da bateria."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de
        percorrer com essa bateria."""
        if self.battery_size == 70:
            range = 240

        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."

        print(message)
    
    def upgrade_battery(self):

        """Define batery size em 85 caso 
        o valor seja diferente de 85"""
        if self.battery_size != 85:
            self.battery_size = 85
    
class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""
    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai
        Em seguida, inicializa os atributos específicos de um carro
        elétrico
        """
        super().__init__(make, model, year)
        self.battery = Battery()

############## Main Program ##################

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()