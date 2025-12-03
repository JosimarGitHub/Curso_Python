from pathlib import Path
import csv
from datetime import datetime
import pandas as pd
import plotly.express as px

# Caminho da pasta onde está o arquivo
path = Path('/home/dev_net/Desktop/Curso_Python/Projetos/' \
'Generating_Data/eq_data/World_Fires_20251202.csv')

#ler as linhas do arquivo
lines = path.read_text().splitlines()

# ler em formato csv
reader = csv.reader(lines)

# pegar o nome das colunas do arquivo
header_row = next(reader)

# pegar a posição dos valores desejados
for index, collumn in enumerate(header_row):
    if collumn == "latitude":
        index_lat = index

    if collumn == "longitude":
        index_log = index
    
    if collumn == "bright_ti4":
        index_bright = index
    
    if collumn == "acq_date":
        index_dat = index
    
# Criar uma lista com as informações desejadas
lats, longs, brights, dates = [], [], [], []
for row in reader:
    
    current_date = datetime.strptime(row[index_dat], '%Y-%m-%d')
    lats.append(row[index_lat])
    longs.append(row[index_log])
    brights.append(float(row[index_bright]))
    dates.append(row[index_dat])

# Criar um dicionario com os dados coletados
dados = {'latitude' : lats,
         'longitude' : longs,
         'brightness' : brights,
         'dates' : dates
        }

# criar um data flame pandas para o grafico plotly 
df = pd.DataFrame(dados)

# Criar o grafico
fig = px.scatter_geo(df,
                     lat='latitude', 
                     lon='longitude', 
                     size='brightness', 
                     title="Mapa Global de Queimadas",
                     color='brightness', 
                     color_continuous_scale='solar',
                     labels={'color' : 'Brightness', 'dates' : 'Data'}, 
                     projection='natural earth',
                     hover_data=['latitude', 'longitude', 'brightness', 'dates']
                     )
fig.show()