arquivo = open(r"C:\Users\pblvv\OneDrive\Documentos\Bootcamp DIO - Python AI Backend Developer/06 - Manipulação de Arquivos\lorem.txt", "r")

print(arquivo.read())

print(arquivo.readline())

print(arquivo.readlines())

while len(linha := arquivo.readline()):
    print(linha)
    
arquivo.close()