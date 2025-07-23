# Estruturas de Dados

## Conteúdo da Etapa:

- Listas
- Tuplas
- Conjuntos (set)
- Dicionários (dict)
- Iteração com for e enumerate
- Compreensões de listas
- Métodos Úteis
- Exercícios

```python
# Trata-se de conteúdo complexo e extenso, sempre checar o material original e a documentação oficial da linguagem.
```

## Listas

Listas são um objeto para armazenamento de dados, que podem conter todo os tipos de dados: números, strings, booleans.

### Principais operações com listas:

```python
lista = [1, 2, 3] # Declaração da lista

print(lista[0]) # Acessa um elemento de uma lista com base em seu índice, no caso, retornaria o valor 1.

lista[2] = 42 # Altera um elemento de uma lista com base em seu índice, caso eu desse um print(lista) iria retornar: [1, 2, 42]

lista.append(4) # Adiciona um elemento no fim da lista, em caso de print(lista) retornaria: [1, 2, 3, 4]

lista.insert(indice) # Insere um elemento no índice informado.

print(f"{lista + [5,6]}") #  Concatenação de listas, inclui os numeros 5 e 6 na lista declarada anteriormente.

lista.remove(2) # Remove por valor.

# Ver todas no arquivo original.
```

## Tuplas:

Em Python, tuplas são ""listas"" que não podem ser alteradas. São declaradas entre parênteses, conforme o caso abaixo:

```python
tupla = ("Python", "JavaScript", "C#")

print(tupla) # Retorna ('Python', 'JavaScript', 'C#')

tupla[2] = "Js"

print(tupla)

# TypeError: 'tuple' object does not support item assignment
```

## Set (Conjunto):

Coleção não ordenada e sem elementos duplicados.

```python
conjunto = {1,2,3}

print(conjunto) # Retorna {1,2,3}

conjunto_vazio = set() # Não usar {} pois cria um dicionário.

conjunto.add(4) # Adiciona o numero 4 ao conjunto

conjunto.remove(4) # Remove o número 4 do conjunto, se fosse um elemento inexistente geraria erro.

conjunto.clear() # Limpa o conjunto
```

## Dicionários:

Dicionários são estruturas no python que contêm combinações de chave-valor, conforme os moldes abaixo:

```python
dict_vazio = {} # Dicionário vazio.

pessoa = {"nome" : "joão", "idade" : 23}

print(f"{pessoa["nome"]} tem {pessoa["idade"]} anos") # Retorna joão tem 23 anos.

# Acessar conteúdo completo do curso.
```

## Iteração com for e enumerate:

Iteração significa percorrer uma determinada sequencia, conforme abaixo:

```python
linguagens = ["Python", "JavaScript", "C#"]

for linguagem in linguagens:
    print(linguagem)

for indice, linguagem in enumerate(linguagens):
    print(f"{indice}: {linguagem}")

# Enumerate é mais legível que for, pois mostra o índice do item iterado.
```

## List Comprehensions:

List comprehensions são uma forma concisa e elegante de criar listas baseadas em sequências existentes ou condições específicas.

```python
# Quadrados dos números de 0 a 4
quadrados = [x**2 for x in range(5)]
# Resultado: [0, 1, 4, 9, 16]

# Maiúsculas de uma lista de strings
nomes = ["ana", "bruno", "carla"]
maiusculas = [nome.upper() for nome in nomes]
# Resultado: ['ANA', 'BRUNO', 'CARLA']
```

Com condições (filtros):

```python
# Com if no final (filtro)
pares = [x for x in range(10) if x % 2 == 0]
# Resultado: [0, 2, 4, 6, 8]

# Com if-else (expressão condicional)
resultado = [x if x > 0 else 0 for x in [-2, -1, 0, 1, 2]]
# Resultado: [0, 0, 0, 1, 2]
```
