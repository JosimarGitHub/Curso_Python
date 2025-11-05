nike = {'tipo':'cachorro','dono':'Josimar'}
cherry = {'tipo':'gato','dono':'Juliana'}
loro = {'tipo':'passaro','dono':'Benedita'}
filó = {'tipo':'tartaruga','dono':'Ana Clara'}
nemo = {'tipo':'peixe','dono':'Rodrigo'}
pets = [nike,cherry,loro,filó,nemo]

for pet in pets:
    for k, v in pet.items():
        print(str(k) + ' --> ' + str(v))
    print('\n')