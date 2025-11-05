class user():
    
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
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user01 = user('josimar', 'simões', 'josimar pereira simões', 
              'rua goricia onisto morbidelli', 39,
              '35-98428-9199', 'jpsimoes85@hotmail.com', 
              'manutenção', '1000000768')

user01.describe_user()
user01.greet_user()

for i in range(15):
    user01.increment_login_attempts()

print('Tentativas de login ' + str(user01.login_attempts))

user01.reset_login_attempts()
print('Tentativas de login ' + str(user01.login_attempts))





