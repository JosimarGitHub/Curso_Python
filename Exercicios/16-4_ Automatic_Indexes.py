from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('/home/dev_net/Desktop/Curso_Python/Projetos/' \
'Generating_Data/weather_data/sitka_weather_2021_simple.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, collumn in enumerate(header_row):
    if collumn == "NAME":
        index_name = index

    if collumn == "DATE":
        index_date = index
    
    if collumn == "TMAX":
        index_high = index
    
    if collumn == "TMIN":
        index_low = index
    
# Extract dates and high temperatures.
highs, dates, lows = [], [], []
name = ""

for row in reader:

    current_date = datetime.strptime(row[index_date], '%Y-%m-%d')

    if name == "":
        name = row[index_name]
    try:
        high = int(row[index_high])
        low = int(row[index_low])
    except ValueError:
        pass
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
#plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, color='blue', alpha=0.1)

# Format plot.
ax.set_title(f"Daily High and Low Temperatures, 2021\n{name}", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()