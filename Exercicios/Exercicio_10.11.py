import json

path = "/home/dev_net/Desktop/Curso_Python/files/"
filename = 'numero_favorito.json'

try:
    with open(path + filename) as f_obj:
        numero_2 = json.load(f_obj)

except:
    while True:

        try:
            pergunta = (input("Qual seu numero favorito ? \n"))
            numero_1 = int(pergunta)
        except ValueError:
            print("Valor numérico invalido, digite novamente outro numero")
        else:
            break

    with open(path + filename, 'w') as f_obj:
        json.dump(numero_1, f_obj)
        
else:
    print("Eu sei qual é o seu numero favorito!\n" \
    "Ele é " + str(numero_2))





