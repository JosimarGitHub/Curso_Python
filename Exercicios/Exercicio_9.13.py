from collections import OrderedDict

glossario = OrderedDict()

while True :

    chave = input("Insira uma palavra (para sair digite 'exit'): ")

    if chave == 'exit':
        break

    else:
        valor = input('Agora digite o seu significado: ')
    
    glossario[chave]= valor

print(glossario)