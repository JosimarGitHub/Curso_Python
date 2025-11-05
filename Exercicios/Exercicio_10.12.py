import json

def get_stored_username(path, filename):

    """Obtém o nome do usuário já armazenado se estiver disponível."""

    try:
        with open(path + filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(path, filename):

    """Pede um novo nome de usuário."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(path + filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user(path, filename):

    """Saúda o usuário pelo nome."""
    username = get_stored_username(path, filename)
    if username:
        while True:
            confirm_username = input("Seu nome é " + username + " ?\nResponda Sim ou Não: ")
            if confirm_username.lower() == "sim":
                print("Welcome back, " + username + "!")
                break
            elif confirm_username.lower() == "não":
                username = get_new_username(path, filename)
                print("We'll remember you when you come back, " + username +
                    "!")
                break
            else:
                print("Resposta inválida, responda sim ou não")
    else:
        username = get_new_username(path, filename)
        print("We'll remember you when you come back, " + username +
              "!")

#################################################################
                        # MAIN PROGRAM #
#################################################################

path = "/home/dev_net/Desktop/Curso_Python/files/"
filename = 'username.json'

greet_user(path, filename)