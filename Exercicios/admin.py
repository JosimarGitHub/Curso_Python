# Importando a Classe Pai
from user import User

# Classe que será um atributo da Classe Filha
class Privileges():

    """Modelando privilégios de um admin"""
    # Iniciando Atributos da Classe
    def __init__(self, privileges):
        self.privileges = privileges

    """Modulo para mostrar os privilegios"""
    #Modulo (Uma função dentro da classe)
    def show_privileges(self):

        print('Um administrador tem os seguintes privilégios:')
        for privilege in self.privileges:
            print(privilege)

#-----------------------------------------------------#
# Classe Filha
class Admin(User):

    """Modelando Admin"""
    def __init__(self, first_name, last_name, full_name, address,
                 age, phone, email, job_sector, id_number,lista_privileges):
        
        """Herdando atributos da Classe Pai"""
        super().__init__(first_name, last_name, full_name, address,
                 age, phone, email, job_sector, id_number)
        
        """Definindo novos atributos de Admin"""
        self.lista_privileges = lista_privileges
        self.privileges = Privileges(self.lista_privileges)

#-----------------------------------------------------#