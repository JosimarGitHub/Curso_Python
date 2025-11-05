sandwiches = ['x-burguer','pastrami','x-salada','pastrami','x-frango','x-lombo','pastrami','x-churrasco','x-tudo','pastrami']
finished_sandwiches  = []

while sandwiches :
    sandwiche = sandwiches.pop()
    print('Preparei seu sanduíche de ' + str(sandwiche.title()) + '.')
    finished_sandwiches.append(sandwiche)

print('Sandwiches preparados são:')

for sandwiche in finished_sandwiches:
    print(sandwiche)