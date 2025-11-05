sandwiches = ['x-burguer','pastrami','x-salada','pastrami','x-frango','x-lombo','pastrami','x-churrasco','x-tudo','pastrami']
finished_sandwiches  = []

print('Estamos sem pastrami,não é pssivel fazer o seu pedido')

while 'pastrami' in sandwiches :
    sandwiches.remove('pastrami')
    
print('Sandwiches preparados são:')

for sandwiche in sandwiches:
    print(sandwiche)