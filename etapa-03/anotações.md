# Etapa 3 - Funções

## Conteúdo da Etapa:

- Declaração e chamada de funções
- Parâmetros e argumentos
- Return
- Escopo de variáveis
- Parâmetros padrões e nomeados
- Funções como objeto

## Declaração e chamada de funções

### O que são funções?

Funções são blocos de código reutilizáveis, que executam tarefas específicas. Em Python, são declaradas com a palavra def. Veja o exemplo abaixo da sintaxe padrão:

```python
def funcao():
    # Inserir as instruções
```

Parece um pouco confuso, né? Vamos tratar um exemplo simples:

```python
def bom_dia():
    print("Olá, bom dia!")

bom_dia() #Saída: Olá, bom dia!
```

## Parâmetros e argumentos

Parâmetros são utilizados em funções quando esperamos que a função se comporte de uma determinada forma com base em algo informado no código (Agora pareceu confuso mesmo). Vamos seguir na lógica do bom dia:

```python
def bom_dia(nome):
    print(f"Olá, bom dia ${nome}")

bom_dia("Márcio") # Saída: Olá, bom dia Márcio!
```

Os parâmetros podem ser posicionais ou nominais, vejamos abaixo:

```python
def bom_dia(nome, hora):
    print(f"Olá, bom dia ${nome}, agora são {hora}.")

bom_dia("Thiago", "08:15") # Saída: Olá, bom dia Thiago, agora são 08:15.

def boa_noite(nome, hora):
    print(f"Olá, boa noite {nome}, agora são {hora}.")

boa_noite(hora="20:30", nome="João") # Saída: Olá, boa noite João, agora são 20:30.
```
Perceba que se adoto o método posicional, preciso seguir a ordem que declarei, agora se utilizo o método nominal a ordem não importa.

## Return

Return serve para devolver um valor ao finalizar a execução da função.

```python

def multiplicar_por_dez(numero):
    return numero * 10

resultado = multiplicar_por_dez(10)
print(resultado) # Saída 100
```

É possível retornar:
- Strings
- Múltiplos valores (retorna como tupla)
- Condicionais (se x = x retorna "x", se x = y retorna "y")

## Escopo de variáveis

Escopo representa onde uma variável por ser acessada. Uma variável declarada dentro de uma função não pode ser acessada fora dela. Exemplo:

```python
def saudacao():
    nome = "Lucas"
    print(f"Olá, {nome}!")

saudacao()
# print(nome)  # Erro: nome não está definido fora da função
```
Já variáveis usadas fora da função podem ser acessadas dentro dela.\
\
Caso deseje usar uma variável da função fora dela, você deve usar a palavra `global` antes de declarar a variável.\
\
Caso esteja com uma função dentro da outra e precise usar a variável use a palavra `nonlocal` antes da declaração.

