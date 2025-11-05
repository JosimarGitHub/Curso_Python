respostas = {}
condicao = True

while condicao :
    continuar = ''
    nome = input('Qual é o seu nome ?\n')
    lugar = input('Para onde você quer viajar nessas ferias ?\n')
    respostas[nome] = lugar 

    while continuar != 'n' and continuar != 'y':
        continuar = input('Você deseja continuar o enquete ? (y - sim ou n - não) ')
        if continuar == 'n':
            condicao = False
        elif continuar == 'y':
            condicao = True
        else:
            print('Resposta invalida, responda y - sim ou n - não')
print(respostas)



