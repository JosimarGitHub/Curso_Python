from Funções.word_count import count_words

#path = "/home/dev_net/Desktop/Curso_Python/files/"
path = ""
file_names = ["Alice's Adventures in Wonderland.txt",
              "Siddhartha.txt",
              "Moby Dick.txt",
              "Little Women.txt"]

for filename in file_names:
    count_words(path, filename)

