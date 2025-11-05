#import make_car
#from make_car import make_car
#from make_car import make_car as construa_carro
#import make_car as construa_carro
from make_car import * 

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
