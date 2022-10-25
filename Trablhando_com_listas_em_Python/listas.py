### CURSO: TRABALHANDO COM LISTAS EM PYTHON
# Link: https://web.dio.me/course/trabalhando-com-listas-em-python/learning/14a6cc51-c672-451e-9522-ff90c9c83c64?back=/track/geracao-tech-unimed-bh-ciencia-de-dados&tab=undefined&moduleId=undefined
# Projeto GitHub: https://github.com/digitalinnovationone/trilha-python-dio/tree/01_estrutura_de_dados/01%20-%20Estrutura%20de%20dados/01%20-%20Listas
# Instrutor: Guilherme Arthur de Carvalho

""" Objetivo geral: Entender o funcionamento da estrutura de dados lista."""

""" Criando listas: Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto.
Podemos criar listas utilizando o construtor list, a função range ou colocando valores separados por 
vírgula dentro de colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após
a criação. """

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0] ) 

frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas_1 = []
print(frutas_1)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

#--------------
# ACESSO DIRETO
frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[0])  # maçã
print(frutas[2])  # uva


#--------------
#INDICES NEGATIVOS
frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[-1])  # pera
print(frutas[-3])  # laranja

#--------------
#MATRIZ
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

#--------------
"""FATIAMENTO: Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma 
sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda 
informar quantas posições o cursor deve "pular" no acesso."""

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

#--------------
"""ITERAR LISTAS: A forma mais comum para percorrer os dados de uma lista é utilizando o 
comando for. """

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# Função enumerate: Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para 
# isso podemos usar essa função.
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


#--------------
"""COMPREENSÃO DE LISTAS: A compreensão de lista oferece uma sintaxe mais curta quando você deseja: 
criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista 
aplicando alguma modificação nos elementos de uma lista existente. """

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# MÉTODOS DA CLASSE LIST

# APPEND 
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]

# -----------------
# CLEAR 
lista = [1, "Python", [40, 30, 20]]

print(lista)  # [1, "Python", [40, 30, 20]]

lista.clear()

print(lista)  # []

# -----------------
# COPY 
lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

# -----------------
#COUNT
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

# -----------------
#EXTEND
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

# -----------------
#INDEX: Se limita a trazer apenas o índice da primeira ocorrência
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0


# -----------------
# POP: Tira o ultimo elemento da lista, ou se passado o índice ele remove apenas esse.
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]


# -----------------
# REMOVE: Remove o objeto em si, no exemplo abaixo ele remove o "c".
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]

# -----------------
# REVERSE: Reverte a lista, de tras pra frente
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "js", "python"]

# -----------------
# SORT: Ordena a lista
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)


# -----------------
# LEN
linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5

# -----------------
# SORTED
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
