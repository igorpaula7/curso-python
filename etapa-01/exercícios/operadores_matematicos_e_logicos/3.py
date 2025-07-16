# Enunciado: Solicite a idade de uma pessoa e verifique se ela tem entre 18 e 30 anos e se tem carteira de motorista (pergunte com `input` se `sim` ou `não`).

idade = int(input("Qual sua idade?"))
carteira = input("Você tem carteira de motorista? Responda com sim ou não")

if ((idade >= 18 and idade <= 30) and carteira == "sim"):
    print("parabéns, você atende ao que foi definido.")
else:
    print("infelizmente você não atende aos critérios")

if idade < 18:
    print("- você é menor de 18 anos.")
elif idade > 30:
    print("- você tem mais de 30 anos.")
    
if carteira != "sim":
    print("- você não possui carteira de motorista.")