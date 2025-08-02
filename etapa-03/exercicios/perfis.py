# Enunciado: Implemente criar_perfil(**kwargs) que recebe dados como nome, idade, email, e retorna um dicionário com essas informações. Não se limite apenas as sugestões, esse treino é importante para o futuro

usuarios_registrados = []

def criar_perfis(**dados):
    
    registro = {}

    for chave, valor in dados.items():
        registro[chave] = valor
    
    usuarios_registrados.append(registro)

criar_perfis(nome = "João", idade = 20)
criar_perfis(nome = "Carolina", idade = 27)

print(usuarios_registrados)
