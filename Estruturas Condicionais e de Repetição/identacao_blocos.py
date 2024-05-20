def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa!")


def depositar(valor):
    saldo = 500
    saldo += valor
    print(saldo)

sacar(100)

depositar(200)