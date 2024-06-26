texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()

#Exemplo 2
for numero in range(0, 51, 5):
    print(numero, end=" ")