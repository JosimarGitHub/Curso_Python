# Classe Pai
class User():
    
    """Modelando um usuário"""

    # Iniciando Atributos da Classe
    def __init__(self, first_name, last_name, full_name, address,
                 age, phone, email, job_sector, id_number):
        
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.address = address
        self.age = age
        self.phone = phone
        self.email = email
        self.job_sector = job_sector
        self.id_number = id_number

    # Modulo (Uma função dentro da classe)
    def describe_user(self):

        print('Informações do Usuário: ')
        print('Nome - ' + self.first_name.title())
        print('Sobrenome - ' + self.last_name.title())
        print('Nome completo - ' + self.full_name.title())
        print('Endereço - ' + self.address)
        print('Idade - ' + str(self.age))
        print('Telefone - ' + self.phone)
        print('e-mail - ' + self.email)
        print('Setor de Trabalho - ' + self.job_sector)
        print('Chapa - ' + self.id_number)

    #Modulo (Uma função dentro da classe)
    def greet_user(self):
        print('Olá Sr(Sra)' + self.first_name.title() + ', seja bem vindo a Pandurata Alimentos')

#---------------------------------------------------------------------------------------------------------------------------------#
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

#-----------------------------------------------------------------------------------------------------------------------------------#
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

#---------------------------------------------------------------------------------------------------------------------------------#
    
#####################################################################################################################################
                                                        # Main Program #
#####################################################################################################################################

lista_privileges = ["can add post", "can delete post", "can ban user", "can change settings", "can install programs"]

user01 = Admin('josimar', 'simões', 'josimar pereira simões', 
              'rua goricia onisto morbidelli', 39,
              '35-98428-9199', 'jpsimoes85@hotmail.com', 
              'manutenção', '1000000768',lista_privileges)

user01.describe_user()
user01.greet_user()
user01.privileges.show_privileges()

