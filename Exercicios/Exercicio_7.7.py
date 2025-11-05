sandwiches = ['x-burguer','x-salada','x-frango','x-lombo','x-churrasco','x-tudo']
finished_sandwiches  = []

while sandwiches :
    sandwiche = sandwiches.pop()
    print('Preparei seu sanduíche de ' + str(sandwiche.title()) + '.')
    finished_sandwiches.append(sandwiche)

print('Sandwiches preparados são:')

for sandwiche in finished_sandwiches:
    print(sandwiche)