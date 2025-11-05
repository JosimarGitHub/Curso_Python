import unittest 
import Funções.city_functions as funcao

class CityCountryTest(unittest.TestCase):
    """Testes para city_functions.py"""

    def test_city_country(self):
        """Cidade santiago e Pais chile funcionam ?"""
        funcao.city_country("santiago", "chile")

    def test_city_country_population(self):
        """Cidade santiago, Pais chile e população 5000000 funcionam ?"""
        funcao.city_country("santiago", "chile", 5000000)


unittest.main()