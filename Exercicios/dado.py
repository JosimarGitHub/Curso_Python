""" Modulo de gera numeros randomicos de acordo com o range dado"""
from random import randint

class Dado():

    """Fazendo a modelagem de um dado determinando a quantidade de lados via atributo"""
    def __init__(self,lados=6):
        self.lados = lados
    
    def rolar_dado(self):
        x = randint(1, self.lados)
        print(x)