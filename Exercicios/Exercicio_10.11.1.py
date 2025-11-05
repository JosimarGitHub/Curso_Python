import json

while True:

    try:
        pergunta = (input("Qual seu numero favorito ? \n"))
        numero_1 = int(pergunta)
    except ValueError:
        print("Valor numérico invalido, digite novamente outro numero")
    else:
        break

path = "/home/dev_net/Desktop/Curso_Python/files/"
filename = 'numero_favorito.json'

with open(path + filename, 'w') as f_obj:
    json.dump(numero_1, f_obj)







