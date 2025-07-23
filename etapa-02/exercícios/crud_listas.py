frutas = []

def adicionar(fruta):
    frutas.append(fruta)
    
def listar():
    print("Lista Atual:")
    for fruta in frutas:
       print(fruta)
       
def atualizar(antigo, indice_antigo, novo):
    indice_antigo = frutas.index(antigo)
    frutas[indice_antigo] = novo

def remover(fruta):
    frutas.remove(fruta)
    
continuar = "sim"

print("Lista de Frutas")
while continuar == "sim":
    print("Digite 1 para Adicionar uma nova fruta.\nDigite 2 para Listar as frutas.\nDigite 3 para Atualizar uma fruta.\nDigite 4 para Remover uma fruta")
    acao = input()
    
    if acao == "1":
        fruta_adicionar = input("Qual fruta você deseja adicionar? ")
        adicionar(fruta_adicionar)
    
    elif acao == "2":
        listar()
    
    elif acao == "3":
        fruta_alterar_antiga = input("Qual fruta você deseja alterar? ")
        indice_fruta_alterar_antiga = frutas.index(fruta_alterar_antiga)
        fruta_alterar_nova = input("Qual a nova fruta?")
        
        atualizar(fruta_alterar_antiga, indice_fruta_alterar_antiga, fruta_alterar_nova)
    
    elif acao == "4":
        fruta_remover = input("Qual fruta você deseja remover?" )
        frutas.remove(fruta_remover)
    
    else:
        print("Resposta inválida, selecione uma opção correta.")
        
    continuar = input("Você deseja fazer mais alguma coisa? ")