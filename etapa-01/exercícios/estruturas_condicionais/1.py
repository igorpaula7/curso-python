# Enunciado: Peça um número e diga se ele é positivo, negativo ou zero.

a = float(input("Digite um número: "))

if a > 0:
    print("Seu número é positivo.")
elif a < 0:
    print("Seu número é negativo.")
else:
    print("Seu número é zero")