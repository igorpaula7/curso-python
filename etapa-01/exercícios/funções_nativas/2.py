# Enunciado: Peça uma lista de 5 números (usando `input()` e `split()`) e imprima a soma com `sum()` e o maior número com `max()`.

# Consultei a internet:

# https://www.w3schools.com/python/python_lists.asp
# https://www.w3schools.com/python/ref_string_split.asp

numeros_string = input("Digite números separados por espaço: ")

numeros = []

for numero in numeros_string.split():
    numeros.append(int(numero))

print("Números digitados:", numeros)
print("Soma:", sum(numeros))
print("Maior:", max(numeros))