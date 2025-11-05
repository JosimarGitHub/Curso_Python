path = "/home/dev_net/Desktop/Curso_Python/files/"
filename = path + "guests.txt"

with open(filename, 'a') as file_object:
    
    while True:
        nome = input('Escreva seu nome ou digite sair para terminar: ')
        nome = nome.title()
        if nome == 'Sair':
            break
        else:
            file_object.write(nome + '\n')