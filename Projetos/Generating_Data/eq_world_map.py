from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('/home/dev_net/Desktop/Curso_Python/Projetos/' \
'Generating_Data/eq_data/eq_data_30_day_m1.geojson')

contents = path.read_text()
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties'] ['mag']
    eq_title = eq_dict['properties'] ['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    eq_titles.append(eq_title)
    lons.append(lon)
    lats.append(lat)

title = 'Global Earthquakes'
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
