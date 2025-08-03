# Enunciado: Crie uma função usando args que receba números e retorne uma tupla contendo mínimo, máximo e média, nessa ordem. Deve ser possivel passar numeros infinitos.

def retornar_tupla(numeros):

    lista_strings = numeros.split(",")  
    lista_numeros = []  

    for num_str in lista_strings:
        numero = float(num_str.strip())
        lista_numeros.append(numero)
    
    return max(lista_numeros), min(lista_numeros), sum(lista_numeros)/len(lista_numeros)

numeros = input("Digite a lista de números que deseja verificar o mínimo, média e máximo no seguinte formato: 1,2,3,4: ")

tupla = retornar_tupla(numeros)

print("Após verificar o conjunto que você inseriu, obtivemos os seguintes dados:")
print(f"Máximo: {tupla[0]}")
print(f"Mínimo: {tupla[1]}")
print(f"Média: {tupla[2]}")
