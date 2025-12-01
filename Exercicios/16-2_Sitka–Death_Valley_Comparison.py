from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('/home/dev_net/Desktop/Curso_Python/Projetos/' \
'Generating_Data/weather_data/sitka_weather_2021_simple.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures.
highs1, dates1, lows1 = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates1.append(current_date)
    highs1.append(high)
    lows1.append(low)

path = Path('/home/dev_net/Desktop/Curso_Python/Projetos/' \
'Generating_Data/weather_data/death_valley_2021_simple.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures.
highs2, dates2, lows2 = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
            print(f"Missing data for {current_date}")
    else:
        dates2.append(current_date)
        highs2.append(high)
        lows2.append(low)
path = Path('/home/dev_net/Desktop/Curso_Python/Projetos/' \
'Generating_Data/weather_data/death_valley_2021_simple.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures.
highs, dates, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
            print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
#plt.style.use('classic')
fig, ax = plt.subplots()

ax.plot(dates1, highs1, color='red', alpha=0.5)
ax.plot(dates1, lows1, color='blue', alpha=0.5)
ax.fill_between(dates1, highs1, lows1, color='blue', alpha=0.1)

ax.plot(dates2, highs2, color='green', alpha=0.5)
ax.plot(dates2, lows2, color='black', alpha=0.5)
ax.fill_between(dates2, highs2, lows2, color='yellow', alpha=0.1)

# Format plot.
ax.set_title("Daily High and Low Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()