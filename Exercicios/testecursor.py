import matplotlib.pyplot as plt
import mplcursors

x = ["A", "B", "C"]
y = [10, 20, 15]

fig, ax = plt.subplots()
barras = ax.bar(x, y)

cursor = mplcursors.cursor(barras)

@cursor.connect("add")
def on_hover(sel):
    index = sel.index
    nome_x = x[index]
    valor_y = y[index]

    # Texto personalizado
    sel.annotation.set_text(f"Categoria: {nome_x}\nValor: {valor_y}")

plt.show()
