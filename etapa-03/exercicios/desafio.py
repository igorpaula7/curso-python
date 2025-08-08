import math

# O programa deverá pedir o tamanho (em metros quadrados) da área a ser pintada. (varíavel após definir funções)
cobertura_tinta = 6 # A tinta cobre 1 litro para cada 6 metros quadrados.
preco_lata = 80 # Lata de 18 litros = R$ 80,00
preco_galao = 25 # Galão de 3,6 litros = R$ 25,00
margem = 0.1 # Margem de segurança de 10%, sempre considerar latas / galões cheios.
litros_lata = 18 # Cobertura da lata
litros_galao = 3.6 # Cobertura do galão

# O programa deve calcular e exibir as quantidades de tinta necessárias e os respectivos custos em 3 situações:

# Comprar apenas latas de 18 litros:

def calcular_com_latas(tinta):
    latas_necessarias = math.ceil(tinta/litros_lata)
    valor = latas_necessarias * preco_lata
    print(f"Apenas Latas: Você precisa de {latas_necessarias} latas, que dará o valor de R$ {valor}.")

# Comprar apenas galões de 3,6 litros:

def calcular_com_galoes(tinta):
    galoes_necessarios = math.ceil(tinta/litros_galao)
    valor = galoes_necessarios * preco_galao
    print(f"Apenas Galões: Você precisa de {galoes_necessarios} galões, que dará o valor de R$ {valor}.")

# Misturar latas e galões de forma a minimizar o custo total:

def calcular_melhor_custo(tinta):
    
    menor_custo = float('inf')
    menos_latas = 0
    menos_galoes = 0
    
    max_latas = math.ceil(tinta/ litros_lata) + 1 # Latas que faz sentido testar, ex: 17 = 1 + 2
    
    for qtd_latas in range(max_latas + 1): # itera sobre o máximo de latas
        tinta_restante = tinta - (qtd_latas * litros_lata)  # Calcular quanta tinta ainda precisa cobrir com galões
        
        if tinta_restante <= 0: # importante verificar vai que já atingiu o necessário
            qtd_galoes = 0
        else:
            qtd_galoes = math.ceil(tinta_restante / litros_galao)
        
        custo_total = qtd_latas * preco_lata + qtd_galoes * preco_galao
        
        if custo_total < menor_custo:
            menor_custo = custo_total
            menos_latas = qtd_latas
            menos_galoes = qtd_galoes
    
    print(f"Menor custo: Você precisa de {menos_latas} latas e {menos_galoes} galões, com um custo total de R$ {menor_custo}.")

metragem = float(input("Qual a metragem da área a ser pintada? "))
tinta_necessaria = metragem/6
tinta_necessaria_com_margem = tinta_necessaria + (tinta_necessaria * margem)

calcular_com_latas(tinta_necessaria_com_margem)
calcular_com_galoes(tinta_necessaria_com_margem)
calcular_melhor_custo(tinta_necessaria_com_margem)
