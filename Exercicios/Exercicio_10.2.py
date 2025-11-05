path = "/home/dev_net/Desktop/Curso_Python/files/"
filename = path + "learning_python.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line_aux = line.replace('python', 'Java')
    print(line_aux.rstrip())