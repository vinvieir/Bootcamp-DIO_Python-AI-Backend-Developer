# CONTEXTO: Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet 
# ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. 
# Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, 
# além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

# Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
  
  plano1 = "Plano Essencial Fibra - 50Mbps"
  plano2 = "Plano Prata Fibra - 100Mbps"
  plano3 = "Plano Premium Fibra - 300Mbps"

  if consumo <= 10:
    return plano1
  
  elif consumo > 10 and consumo <= 20:
    return plano2
    
  elif consumo > 20:
    return plano3
  
  else:
    print("Operação Inválida!")
    
#: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
#: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))