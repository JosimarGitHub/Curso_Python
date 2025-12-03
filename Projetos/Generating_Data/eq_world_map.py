from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('/home/dev_net/Desktop/Curso_Python/Projetos/' \
'Generating_Data/eq_data/earthquakes_20251201.geojson')

all_eq_data = json.loads(path.read_text())

all_eq_dicts = all_eq_data['features']
title = all_eq_data['metadata']['title']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    if eq_dict['properties'] ['mag'] > 0:
        mags.append(eq_dict['properties'] ['mag'])
        eq_titles.append(eq_dict['properties'] ['title'])
        lons.append(eq_dict['geometry']['coordinates'][0])
        lats.append(eq_dict['geometry']['coordinates'][1])

fig = px.scatter_geo(lat=lats, 
                     lon=lons, 
                     size=mags, 
                     title=title,
                     color=mags, 
                     color_continuous_scale='solar',
                     labels={'color' : 'Magnitude'}, 
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()
