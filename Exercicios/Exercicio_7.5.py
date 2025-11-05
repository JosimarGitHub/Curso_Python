active = True
while active :
    idade = (input('Informe sua idade: '))
    if idade.upper() == 'SAIR':
        active = False
    else:
        idade = int(idade)
        if idade < 3 :
            print('Ingresso gratuito')
        elif idade >= 3 and idade <= 12 :
            print('Custo do ingresso $10,00')
        elif idade > 12 :
            print("Custo do ingresso $15,00")