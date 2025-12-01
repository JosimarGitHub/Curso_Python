import matplotlib.pyplot as plt

from dados_grafico import DadosGrafico

path1 = '/home/dev_net/Desktop/Curso_Python/Projetos/' \
'Generating_Data/weather_data/SE-CGE-SP.csv'

path2 = '/home/dev_net/Desktop/Curso_Python/Projetos/' \
'Generating_Data/weather_data/Extrema.csv'

sao_paulo = DadosGrafico(path1)
extrema = DadosGrafico(path2)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
#plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(sao_paulo.dates,sao_paulo.temperatures, color='red', alpha=0.5, label="São Paulo")
ax.plot(extrema.dates,extrema.temperatures, color='magenta', alpha=0.5, label="Extrema")

# Format plot.
ax.set_title("Media de Temperaturas Ano 2025", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (C°)', fontsize=16)
ax.tick_params(labelsize=16)
plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))

plt.tight_layout()

plt.show()