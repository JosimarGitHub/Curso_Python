path = "/home/dev_net/Desktop/Curso_Python/files/"
filename = path + "enquete_programacao.txt"

with open(filename, 'a') as file_object:
    
    while True:
        resposta = input('Porque voçê gosta de programação, digite sair para terminar: ')
        sair = resposta.title()
        if sair == 'Sair':
            break
        else:
            file_object.write(resposta + '\n')