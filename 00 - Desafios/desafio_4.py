# CONTEXTO: Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. 
# Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. 
# Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, 
# sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

#: Crie uma classe UsuarioTelefone.  
#: Defina um método especial `__init__`, que é o construtor da classe.
#O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano        
    #: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.      
    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = input()  
numero = input()  
plano = input()  
#: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)

print(usuario)