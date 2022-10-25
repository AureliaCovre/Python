### CURSO: EXPLORANDO CONJUNTOS EM PYTHON 
# Link: https://web.dio.me/course/explorando-conjuntos-em-python/learning/09c6ccff-aec7-4506-96b7-b90307851402?back=/track/geracao-tech-unimed-bh-ciencia-de-dados&tab=undefined&moduleId=undefined
# Projeto GitHub: https://github.com/digitalinnovationone/trilha-python-dio/tree/01_estrutura_de_dados/01%20-%20Estrutura%20de%20dados/03%20-%20Conjuntos
# Instrutor: Guilherme Arthur de Carvalho

""" Objetivo geral: Entender o funcionamento da estrutura de dados set."""

""" Criando sets: Um set é uma coleção que não possui o objetos repetidos, usamos sets para 
representar conjuntos matemáticos ou eliminar itens duplicados de um iterável. """

print("Exemplo de criação de Sets: ")
print()
print("--------------")
numeros = ([1, 2, 3, 1, 3, 4])
print("Resultado numeros antes: ",numeros)  # {1, 2, 3, 4}
numeros = set([1, 2, 3, 1, 3, 4])
print("Resultado numeros depois: ",numeros)  # {1, 2, 3, 4}

print("--------------")
letras = ("abacaxi")
print("Resultado letras antes: ",letras)  
letras = set("abacaxi")
print("Resultado letras depois: ",letras)  # {"b", "a", "c", "x", "i"}

print("--------------")
carros = ("palio", "gol", "celta", "palio")
print("Resultado carros antes: ",carros)
carros = set(("palio", "gol", "celta", "palio"))
print("Resultado carros depois: ",carros)  # {"gol", "celta", "palio"}

print("--------------")
linguagem = {"python", "java", "python"}
print(linguagem)

print("--------------")
# -------------
# Acessando dados: Conjuntos em Python não suportam indexação e nem fatiamento, caso queira 
# acessar os seus valores é necessário converter o conjunto para lista.
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print("Resultado da conversão em lista: ", numeros[0])
print("--------------")
# -------------
# Iterar Conjuntos: A forma mais comim para percorrer os dados de um conjunto é utilizando o for.
print("Resultado para iteração do set: ")
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
print("--------------")
# -------------
# Union: 
print("Resultado do union: ")

conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print("Resultado union: ", resultado)
print("--------------")
# -------------
# Intersection: Verifica o que ha de comum nos conjuntos
print("Resultado do intersection (O que ha de igual em ambos os conjuntos)...")

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print("Resultado intersection: ", resultado)
print("--------------")
# -------------
# Difference: Verifica o que ha em um conjunto e não consta no outro
print("Resultado do método difference (O que tem de único em cada conjunto...) ")

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)
print("--------------")
# -------------
# symmetricc_difference: Verifica o que de unico em cada conjunto de uma so vez. 
print("Resultado do método symmetricc_ difference (O que tem de único em cada conjunto... )")

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)
print("--------------")
# -------------
#  issubset: Verifica se um conjunto é sub-conjunto de outro, ou seja se todos os conjuntos de A estão B.
print("Resultado do método issubset: ")

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print("Todos os elemento do conjunto A estão em B? ",resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print("Todos os elemento do conjunto B estão em A? ",resultado)
print("--------------")
# -------------
# issuperset: erifica se um conjunto é sub-conjunto de outro, ou seja se todos os conjuntos 
# de A estão B. Mas ele inverte a ordem na hora de fazer a pergunta.
print("Resultado do método issuperset: ")
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print("Todos os elemento do conjunto B estão em A? ",resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print("Todos os elemento do conjunto A estão em B? ",resultado)
print("--------------")
# -------------
# isdisjoint: Verifica se todos os elementos de um conjunto não constam no outro.
print("Resultado do método isdisjoint (Se os conjuntos possuem elementos diferentes....) ")

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print("Todos os elementos do conjunto A são diferentes do conjunto B? ",resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print("Todos os elementos do conjunto A são diferentes do conjunto C? ",resultado)
print("--------------")
# -------------
# add: adicionar valores em um conjunto
print("Resultado do método add (Adiciona elementos a um conjunto....) ")
sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print("Adicionando o 25", sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print("Adicionando o 42", sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print("Adicionando o 25 novamente...", sorteio)
print("--------------")
# -------------
# clear: limpa o conjunto
print("Resultado do método clear (Limpa o conjunto....) ")
sorteio = {1, 23}

print(sorteio)  # {1,23}

sorteio.clear()

print(sorteio)  # {}
print("--------------")
# -------------
# copy: Gera uma copia do conjunto
print("Resultado do método copy (Gera uma cópia do conjunto....) ")
sorteio = {1, 23}

print(sorteio)  # {1, 23}

sorteio.copy()

print(sorteio)  # {1, 23}
print("--------------")
# -------------
# discard: Descartar um valor | Se colocar valor que não existe não da erro
print("Resultado do método discart (Descarta valores....) ")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print("Resultado após discart(1)", numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
print("--------------")
# -------------
# pop: Vai removendo valores da lista
print("Resultado do método pop (Vai removendo valores da lista....) ")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}
print("--------------")
# -------------
# remove: Remove um valor | Se colocar valor que não existe DA ERRO
print("Resultado do método remove (Remove valores....) ")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("--------------")
# -------------
# len: Conta quantos elementos constam no conjunto
print("Resultado do método len (Conta quantos elementos constam no conjunto...)")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  # 10
print("--------------")
# -------------
# in: Verifica se um elemento consta no conjunto.
print("Resultado do método in (Verifica se um elemento consta no conjunto...) ")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False
