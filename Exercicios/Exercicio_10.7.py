path = "/home/dev_net/Desktop/Curso_Python/files/"
filenames = ["cats.txt", "dogs.txt"]
names2 = ""

for file in filenames:
    filename = path + file

    try:
        with open(filename) as file_object:
            names = file_object.readlines()
    except FileNotFoundError:
        pass
    else:
        for name in names:
            name = name.replace("\n","")
            print(name.title())

