import unittest
from modulos_classes.Employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Criando atributos que podem ser 
        usados em todos os testes de Employee"""

        self.my_employee = Employee("Josimar", "Simões", 17000)
        
    def test_give_default_raise(self):
        """Testando give_raise com valor defaut"""
        self.my_employee.give_raise()

    def test_give_custom_raise(self):
        """Testando give_raise com valor custom"""
        self.my_employee.raise_aux = 3000
        self.my_employee.give_raise()

unittest.main()