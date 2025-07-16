# Enunciado: Peça um número e exiba a tabuada dele de 1 a 10 usando `while`.

a = int(input("Informe um número: "))
contador = 1

print(f"Tabuada do {a}")

while contador <= 10:
    print(f"{a} x {contador} = {a * contador}")
    contador = contador + 1