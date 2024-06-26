# CONTEXTO: Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. 
# O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, 
# em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.



#: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

#: Crie um loop para solicita os itens ao usuário:

coisa = 1
while True:
    item_solicitado = input()
    itens.append(item_solicitado)
    coisa += 1
    if coisa > 3: break
#: Solicite o item e armazena na variável "item":

#: Adicione o item à lista "itens":


# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
