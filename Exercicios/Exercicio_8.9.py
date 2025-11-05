def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great (magicians):
    for i in range(len(magicians)):
        magicians[i] = 'The Great ' + magicians[i]
    return magicians
        

list_magicians = ['Josimar', 'Gerson', 'Juliana', 'Marina', 'José']

list_great_magicians = make_great(list_magicians[:])

show_magicians(list_magicians)
show_magicians(list_great_magicians)