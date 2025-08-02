# A mesma calculadora agora deve poder fazer operaçoes de raiz e potencia, porém devemos passar qual fator será usado Exemplo: (fator, numero) = 4³ Dica: numero ** fator (exponencial) numero ** (1/fator) (raiz).

def instrucoes():
    instrucao = input("Digite a operação que deseja realizar. (soma, subtração, multiplicação, divisão, potência, raiz): ")
    return instrucao

def somar(x, y):
    resultado = x + y
    print(f"Seu resultado é: {resultado}")

def subtrair(x, y):
    resultado = x - y
    print(f"Seu resultado é: {resultado}")

def multiplicar(x, y):
    resultado = x * y
    print(f"Seu resultado é: {resultado}")

def dividir(x, y):
    resultado = x / y
    print(f"Seu resultado é: {resultado}")

def potencia(x, y):
    resultado = x ** y
    print(f"Seu resultado é {resultado}")

def raiz(x,y):
    resultado = x ** (1/y)
    print(f"Seu resultado é: {resultado}")

continuar = "sim"

print("Seja bem-vindo à calculadora.py!")
print("/"*10)

while continuar == "sim":
    instrucao = instrucoes()

    numero_um = float(input("Digite o primeiro número: "))
    numero_dois = float(input("Digite o segundo número: "))

    if instrucao == "soma":
        somar(numero_um, numero_dois)

    if instrucao == "subtração":
        subtrair(numero_um, numero_dois)

    if instrucao == "multiplicação":
        multiplicar(numero_um, numero_dois)

    if instrucao == "divisão":
        dividir(numero_um, numero_dois)

    if instrucao == "potência":
        potencia(numero_um, numero_dois)

    if instrucao == "raiz":
        raiz(numero_um, numero_dois)

    continuar = input("Deseja continuar? (sim / não): ")