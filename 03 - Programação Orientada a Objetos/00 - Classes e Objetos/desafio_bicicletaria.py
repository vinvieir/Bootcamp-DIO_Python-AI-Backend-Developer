class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim...")

    def parar(self):
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmm...")

athena = Bicicleta("vermelha", "caloi", 2024, 500)

athena.buzinar()
athena.correr()
athena.parar()