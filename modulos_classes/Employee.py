class Employee():
    """Modelando um objeto 'Funcionario' 
    com nome e salário anual"""

    def __init__(self,name, last_name, annual_salary):
        """Definindo atributos de um Employee"""

        self.name = name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.raise_aux = 5000
    
    def give_raise(self):
        self.annual_salary = self.annual_salary + self.raise_aux
        print("Novo salario anual após o aumento é: $" + str(self.annual_salary))

    
