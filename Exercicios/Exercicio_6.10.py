cidades = {
    'Extrema':{'estado' : 'Minas Gerais',
            'população' : 40000,
            'fato' : 'primeira cidade do sul de Minas Gerais'},
    'São Paulo':{'estado' : 'São Paulo',
                'população' : 500000,
                'fato' : 'Maior cidade do Brasil'},
    'Maceió':{'estado' : 'Alagoas',
                'população' : 100000,
                'fato' : 'As mais belas praias do Brasil'}
    }

for cidade, informacoes in cidades.items() :
    print(str(cidade.title()) + ':')
    for chave, informacao in informacoes.items():
        print(str(chave.title()) + ': ' + informacao)
    print('############################################')