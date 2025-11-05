path = "/home/dev_net/Desktop/Curso_Python/files/"
file_names = ["Alice's Adventures in Wonderland.txt",
              "Moby Dick.txt",
              "Little Women.txt"]

quantidade = 0

for filename in file_names:
    with open(path + filename) as arquivo:
        texto = arquivo.read()
        quantidade = texto.lower().count("the")
        print("A palavra 'the' em " + filename + " aparece " + 
              str(quantidade) + " vezes")

