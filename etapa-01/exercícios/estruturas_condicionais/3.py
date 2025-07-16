# Enunciado: Peça a idade e informe se a pessoa é criança (até 12), adolescente (13–17), adulto (18–59) ou idoso (60+).

idade = int(input("Qual sua idade? "))

if idade <= 12:
    print("Você é criança")
elif (12 < idade <= 17):
    print("Você é adolescente")
elif (18 <= idade <= 59):
    print("Você é adulto")
else:
    print("Você é idoso")