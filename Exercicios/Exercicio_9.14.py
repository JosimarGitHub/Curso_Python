from dado import Dado

for i in range(10):
    dado = Dado()
    dado.rolar_dado()

print('###############################################')

for i in range(10):
    dado = Dado(10)
    dado.rolar_dado()

print('###############################################')

for i in range(10):
    dado = Dado(20)
    dado.rolar_dado()