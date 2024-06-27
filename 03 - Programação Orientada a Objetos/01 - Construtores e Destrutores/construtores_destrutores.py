class Gato:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("miau")

def criar_gato():
    hefesto = Gato("Festo", "Laranja com listras", False)
    print(hefesto.nome)

hefesto = Gato("Hefesto", "laranja")
hefesto.falar()

print("Ola mundo")

del hefesto

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")