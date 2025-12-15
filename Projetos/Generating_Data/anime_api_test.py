from operator import itemgetter
import requests
import plotly.express as px
import xmltodict
import json

# URL AD API. 
url = "https://www.animenewsnetwork.com/encyclopedia/reports.xml?id=155"

# CHAMADA DA URL
r = requests.get(url)

# MOSTRANDO O RESULTADO DA CONSULTA 200:OK 404: NÃO ENCONTRADO
print(f"Status code: {r.status_code}")

# RESPOSTA XML EM TEXTO
xml_response = r.text

# CONVERTENDO A RESPOSTA TEXTO EM DICIONARIO PARA CONSULTA
response_dicts_xml = xmltodict.parse(xml_response)

# CONVERTENDO PARA UMA STRING JSON, FACILITANDO A LEITURA
response_dicts_json = json.dumps(response_dicts_xml, indent=4)

# CRIANDO UM DICIONÁRIO SÓ DOS ITENS
response_dicts_items = response_dicts_xml['report']['item']

# Criando um dicionário dos itens relevantes
dict_ids = [dict_id['id'] for dict_id in response_dicts_items] 
dict_names = [dict_name['name'] for dict_name in response_dicts_items]
dict_types = [dict_type['type'] for dict_type in response_dicts_items]
dict_descrits = []

found_text = False

for anime_dict in dict_ids:
    
    found_text = False
    url = f"https://cdn.animenewsnetwork.com/encyclopedia/api.xml?title={anime_dict}"
    r = requests.get(url)
    #print(f"Status code: {r.status_code}")
    xml_response = r.text
    response_dicts_xml = xmltodict.parse(xml_response)
    try:
        dict_infos=response_dicts_xml['ann']['anime']['info']
    except KeyError:
        dict_infos=response_dicts_xml['ann']['manga']['info']
    else:
        pass

    for dict_info in dict_infos:
        if dict_info['@type'] == 'Plot Summary':
            dict_descrits.append(dict_info['#text'])
            found_text = True
    if not found_text:
        dict_descrits.append("No comments")

for i in range(len(dict_ids)):

    if dict_types[i]== 'manga':
        title = f"############ Manga {i} ############"
    else:
        title = f"############ Anime {i} ############"

    print(title + "\n"
        f"Id: {dict_ids[i]}\n"+
        f"Name: {dict_names[i]}\n"+
        f"Type: {dict_types[i]}\n"+
        f"Description: {dict_descrits[i]}"
        )

    