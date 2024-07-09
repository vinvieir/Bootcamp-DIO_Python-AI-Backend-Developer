arquivo = open(r"C:\Users\pblvv\OneDrive\Documentos\Bootcamp DIO - Python AI Backend Developer\06 - Manipulação de Arquivos\teste.txt", "w")


arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "Python"])
arquivo.close()