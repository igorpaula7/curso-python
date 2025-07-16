# Enunciado: Solicite a nota de um aluno e diga se ele foi aprovado (nota ≥ 7), em recuperação (nota entre 5 e 6.9) ou reprovado (abaixo de 5).

nota = float(input("Qual foi sua nota? "))

if nota >= 7: 
    print("Você foi aprovado.")
elif nota >=5: 
    print("Você está de recuperação.")
else: 
    print("Você foi reprovado.")
