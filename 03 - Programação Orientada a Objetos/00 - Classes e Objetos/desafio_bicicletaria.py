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

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

athena = Bicicleta("vermelha", "caloi", 2024, 500)

athena.buzinar()
athena.correr()
athena.parar()

print(athena.cor, athena.modelo, athena.ano, athena.valor)

artemis = Bicicleta("verde", "monark", 2000, 340)
Bicicleta.buzinar(artemis)