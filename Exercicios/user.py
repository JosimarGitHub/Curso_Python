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

#-----------------------------------------------------#
