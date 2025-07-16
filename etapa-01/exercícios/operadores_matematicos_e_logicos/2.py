# Enunciado: Verifique se um número informado pelo usuário é par ou ímpar.

# Tive que consultar a internet, não me lembrava como funcionava restos no python:

# https://www.inf.pucrs.br/flash/progbio/aulas/seq/build/progbio/OperatorsandOperands.html

a = int(input("Informe seu número: "))

if (a % 2 == 0):
    print("O número é par.")
else:
    print("O número é impar.")