Josimar = {'first_name':'Josimar','last_name':'Simões','age':39,'city':'Extrema'}
Mercedes = {'first_name':'Mercedes','last_name':'Moraes','age':78,'city':'Lorena'}
Jorg = {'first_name':'Jorg','last_name':'Fontana','age':35,'city':'Bragança'}
pessoas = [Josimar,Mercedes,Jorg]

for pessoa in pessoas :
    for k, v in pessoa.items():
        print(str(k) + '--> ' + str(v))
    print('\n')
