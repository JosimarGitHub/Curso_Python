favorite_places = {'Josimar' : ['Maceió', 'Natal', 'Miami'],
                   'Juliana' : ['Madri', 'Paris', 'Barcelona'],
                   'Marina' : ['Roma', 'Veneza', 'Londres']}
lugares_print = ''
i = 1

for name, lugares in favorite_places.items() :
    print('Os lugares favoritos do(a) '+ str(name) + ' são:')

    for lugar in lugares:
        if i == 1 :
            lugares_print = lugares_print + lugar + ', '
            i = i + 1
        elif i > 1 and i < len(lugares) :
            lugares_print = lugares_print + lugar + ', '
            i = i + 1
        elif i == len(lugares) :
            lugares_print = lugares_print + lugar + '.'
            i = 1
         
    print(lugares_print)
    lugares_print = ''
    print('\n')
        
