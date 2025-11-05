import json

path = "/home/dev_net/Desktop/Curso_Python/files/"
filename = 'numero_favorito.json'

try:
    with open(path + filename) as f_obj:
        numero_2 = json.load(f_obj)
except FileNotFoundError:
    print("O arquivo " + filename + " não existe")
else:
    print("Eu sei qual é o seu numero favorito!\n" \
    "Ele é " + str(numero_2))