path = "/home/dev_net/Desktop/Curso_Python/files/"
filename = path + "learning_python.txt"

with open(filename) as file_object:
    file = file_object.read()
    print(file.rstrip())
    print("-------------------------------")

with open(filename) as file_object:  
    for line in file_object:
        print(line.rstrip())
    print("-------------------------------")

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

    
