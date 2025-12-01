from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('/home/dev_net/Desktop/Curso_Python/Projetos/' \
'Generating_Data/weather_data/sitka_weather_2021_full.csv')

path1 = Path('/home/dev_net/Desktop/Curso_Python/Projetos/' \
'Generating_Data/weather_data/death_valley_2021_full.csv')

lines = path.read_text().splitlines()
lines1 = path1.read_text().splitlines()

reader = csv.reader(lines)
reader1 = csv.reader(lines1)
header_row = next(reader) #row 5
header_row1 = next(reader1)

dates, PRCPs = [], []

for row in reader:

    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    PRCP = float(row[5])

    dates.append(current_date)
    PRCPs.append(PRCP)

dates1, PRCPs1 = [], []

for row in reader1:

    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    PRCP = float(row[5])

    dates1.append(current_date)
    PRCPs1.append(PRCP)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
#plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, PRCPs, color='red', alpha=0.5)
ax.plot(dates1, PRCPs1, color='green', alpha=0.5)

# Format plot.
ax.set_title("Quantidade de chuvas diárias", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Porcentagem (%)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()