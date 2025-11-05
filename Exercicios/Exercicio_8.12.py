def ingredientesSanduiche (*ingredientes):
    print('Os ingredientes do seu sanduiche são:')
    for ingrediente in ingredientes:
        print('- ' + ingrediente)

ingredientesSanduiche('queijo')
ingredientesSanduiche('queijo', 'alface', 'tomate')
ingredientesSanduiche('hamburguer', 'cebola caramelizada', 'cheddar', 'molho especial', 'pão de brioche' )
