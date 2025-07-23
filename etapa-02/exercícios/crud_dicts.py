contatos = {}

def adicionar_ou_alterar(nome, numero):
    contatos[nome] = numero

def listar():
    print(contatos)

def remover(nome):
    del contatos[nome]

continuar = "sim"

print("Lista de Contatos")
while continuar == "sim":
    print("Digite 1 para Adicionar ou Alterar um contato.\nDigite 2 para Listar os contatos.\nDigite 3 para Remover um contato")
    acao = input()
    
    if acao == "1":
        nome_adicionar = input("Qual nome você deseja adicionar ou alterar o telefone? ")
        telefone_adicionar = input("Qual o telefone que você deseja adicionar ou alterar? ")

        adicionar_ou_alterar(nome_adicionar, telefone_adicionar)

    elif acao == "2":
        listar()
    
    elif acao == "3":
        nome_remover = input("Qual contato você deseja remover?")
        remover(nome_remover)

    else:
        print("Resposta inválida, selecione uma opção correta.")
        
    continuar = input("Você deseja fazer mais alguma coisa? ")