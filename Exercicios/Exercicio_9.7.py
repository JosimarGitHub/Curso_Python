class User():
    
    """Modelando um usuário"""

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

    def greet_user(self):
        print('Olá Sr(Sra)' + self.first_name.title() + ', seja bem vindo a Pandurata Alimentos')

class Admin(User):

    """Modelo Pai"""
    def __init__(self, first_name, last_name, full_name, address,
                 age, phone, email, job_sector, id_number):
        
        super().__init__(first_name, last_name, full_name, address,
                 age, phone, email, job_sector, id_number)
        self.privileges = ["can add post", "can delete post", "can ban user", "can change settings", "can install programs"]
    
    def show_privileges(self):

        print('Um administrador tem os seguintes privilégios:')
        for privilege in self.privileges:
            print(privilege)




user01 = Admin('josimar', 'simões', 'josimar pereira simões', 
              'rua goricia onisto morbidelli', 39,
              '35-98428-9199', 'jpsimoes85@hotmail.com', 
              'manutenção', '1000000768')

user01.describe_user()
user01.greet_user()
user01.show_privileges()



