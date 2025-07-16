# Etapa 01 - Fundamentos da Programação

## Conteúdo da Etapa:
- Tipos de Dados
- Variáveis
- Entrada e Saída de Dados
- Operadores Matemáticos e Lógicos
- Estruturas condicionais
- Estruturas de repetição
- Funções nativas
- Exercícios

## Breve introdução ao Clean Code:

Antes de iniciar o código em Python, dei uma breve lida sobre as melhores práticas ao se codar nessa linguagem nesse artigo da [TestDriven](https://testdriven.io/blog/clean-code-python/).
Resumidamente:
- os nomes das classes devem ser CamelCase (MyClass)
- os nomes das variáveis devem ser snake_case e todos em letras minúsculas (first_name)
- os nomes das funções devem ser snake_case e todos em letras minúsculas (quick_sort())
- as constantes devem ser snake_case e todas em maiúsculas ( PI = 3.14159)
- aspas simples e duplas são tratadas da mesma forma (basta escolher uma e ser consistente)
- recuar usando 4 espaços (espaços são preferíveis a tabulações)
- as linhas não devem ter mais de 79 caracteres

## Tipos de Dados:

### O que são Dados?
Dados são informações que podem ser processadas, armazenadas e manipuladas por um programa de computador. É a matéria-prima fundamental da programação!

### Principais tipos:

- int - número inteiro
- float - número com casas decimais
- boolean - verdadeiro ou falso
- string - cadeia de caracteres (nome, cidade, etc..)
- list - lista de elementos que pode mudar
- tuple - lista de elementos que não pode mudar
- dict - dicionário

## Variáveis

Uma variável nada mais é que um nome que recebe e armazena um valor na memória do computador. Em python, não há a necessidade de declarar seu tipo, embora isso possa ser convertido futuramente. Veja o exemplo abaixo:

```python
nome = "João" # Variável do tipo string
idade = 25 # Variável do tipo int
altura = 1.75 # Variável do tipo float
```

Um adendo importante: Variáveis podem ter seu valor alterado ao longo do tempo, conforme o caso abaixo:
```python
nome = "João" # Meu nome é João!

nome = "Pedro" # Meu nome é Pedro!

print(nome) # O resultado seria simplesmente "Pedro"
```

## Entrada e Saída de Dados

Em Python, podemos receber e imprimir dados para o usuário, através dos seguintes comandos respectivamente:
- input (recebe dados do usuário, **sempre em string**)
- print (exibe dados para o usuário)

Veja o exemplo abaixo:

```python
nome = input("Qual seu nome?")
print("Seu nome é: ", nome)
```
É possível imprimir variáveis, textos, e até a soma de números inteiros. Lembram-se que eu falei da conversão anteriormente, vejamos um exemplo no código abaixo:
```python
numero_um = int(input("Qual o primeiro número?")) # Conversão de string para inteiro
numero_dois = int(input("Qual o segundo número?")) # Conversão de string para inteiro

print("A soma de ", numero_um, "e ", numero_dois, " é: ", (numero_um + numero_dois)) # Caso eu responda 2 e 5, retornaria: "A soma de 2 e 5 é: 7"
```
## Operadores matemáticos e lógicos

Podemos fazer operações com as quatro operações básicas em Python de forma nativa, e existem também operadores lógicos que retornam valores true ou falso:
```python
# Operadores matemáticos:

numero_um = 2
numero_dois = 7

print(numero_um + numero_dois) # Retorna 9
print(numero_um - numero_dois) # Retorna -5
print(numero_um * numero_dois) # Retorna 14
print(numero_um / numero_dois) # Retorna 0.2857142857142857

# Percebam que eu nunca declarei que as variáveis eram do tipo float (que aceitam casas decimais), mas o próprio código subentende quando realizo uma operação que daria um resultado dessa forma.

# Operadores lógicos:

print(numero_um > numero_dois) # Retorna False
print(numero_um < numero_dois) # Retorna True
```

## Estruturas Condicionais:

- if (condição número 1)
- elif (condição número 2)
- else (caso não atenda nenhuma condição)\
Veja o exemplo abaixo:
```python
idade = int(input("Qual sua idade?"))

if idade < 13:
    print("Você é criança")
elif (idade >= 13 and idade < 18):
    print("Você é adolescente")
else:
    print("Você é adulto")
```

## Estruturas de repetição:

Executam código múltiplas vezes automaticamente.

### for - Para sequências
- Percorre listas, strings, range()
- Uso: quando você sabe quantas vezes vai repetir

```python
for i in range(3):
    print(i)  # 0, 1, 2
```

### while - Por condição
- Repete enquanto condição for verdadeira
- Uso: quando não sabe quantas repetições

```python
contador = 0
while contador < 3:
    print(contador)
    contador += 1  # 0, 1, 2
```

## Funções Nativas

O que são: Funções já disponíveis no Python, sem precisar importar.

Principais funções:

**Entrada/Saída:**
- `print()` → exibe dados
- `input()` → recebe dados do usuário

**Informações:**
- `len()` → tamanho/quantidade
- `type()` → tipo da variável

**Conversão:**
- `int()`, `float()`, `str()` → muda tipo de dado

**Sequências:**
- `range()` → gera números em sequência

**Matemáticas:**
- `max()` → maior valor
- `min()` → menor valor  
- `sum()` → soma elementos
- `sorted()` → ordena lista