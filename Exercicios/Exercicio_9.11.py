from admin import Admin

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
