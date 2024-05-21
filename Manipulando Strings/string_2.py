nome = "Pablo"
idade = 21
profissao = "Programador"
linguagem = "Python"
saldo = 45.367

dados = {"nome": "Pablo", "idade": 21}

print("Nome: {} Idade: {}".format(nome,idade))
print("Nome: {1} Idade: {0}".format(idade,nome))

print("Nome: {nome} Idade: {idade}".format(idade=idade ,nome=nome))
print("Nome: {name} Idade: {age}".format(age=idade ,name=nome))

print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:0.2f}")