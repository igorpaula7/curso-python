# Enunciado: Implemente criar_perfil(**kwargs) que recebe dados como nome, idade, email, e retorna um dicionário com essas informações. Não se limite apenas as sugestões, esse treino é importante para o futuro

usuarios_registrados = []

def criar_perfis(**kwargs):

    registro = {}

    for chave, valor in kwargs.items():
        registro[chave] = valor
    
    usuarios_registrados.append(registro)

continuar = "sim"

print("Bem vindo ao Registro de Usuários")
print("/"*20)

while continuar == "sim":

    nome = input("Insira o nome do seu usuário: ")
    idade = int(input("Insira a idade do seu usuário: "))
    email = input("Insira o e-mail do seu usuário: ")

    criar_perfis(nome = nome, idade = idade, email = email)

    continuar = input("Deseja adicionar mais algum usuário? (sim / não)")

print("Os seguintes usuários foram registrados: ")
print(usuarios_registrados)
