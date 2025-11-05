def make_album (autor,album,faixas=''):
    if faixas:
        out = {'autor':autor, 'album':album,'faixas':faixas}
    else:
        out = {'autor':autor, 'album':album}
    return out

while True :

    autor = input('Digite o nome de um autor: ')
    album = input('Digite o nome do album que ele fez: ')
    faixas = input('Quantas faixas o album possui: ')

    out = make_album(autor, album, faixas)

    print(out)
    saida = input('Deseja continuar ? (s - sim / n - não)')

    if saida.lower() == 'n':
        break
    else:
        continue