while True:

    i = input('Informe o primeiro numero ou tecle "sair" para terminar: ')
    exit = i.title()
    if exit == 'Sair' :
        break
    else:
         j = input('Informe o segundo numero ou tecle "sair" para terminar: ')
         exit = j.title()
    if exit == 'Sair' :
        break
    else:
        try:
            soma = int(i) + int(j)

        except ValueError :
            print("Não é possivel converter uma string," \
            "por favor informe um valor numérico")

        else:
            print('A soma dos numeros é: ' + str(soma))