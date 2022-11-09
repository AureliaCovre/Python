### CURSO: MANIPULAÇÃO DE STRINGS COM PYTHON 
# Link: https://web.dio.me/course/dominando-strings-e-fatiamento-com-python/learning/b67433a9-2fc7-41cc-8db0-c0ddd3964198?back=/track/geracao-tech-unimed-bh-ciencia-de-dados&tab=undefined&moduleId=undefined
# Instrutor: Guilherme Arthur de Carvalho

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# STRING E FATIAMENTO
"""Objetivo geral: Conhecer métodos úteis para manipular objetos do tipo string, como interpolar
valores de variáveis e entender como funciona o fatiamento. """


# Conhecendo métodos úteis da classe string

#Maiusculo, minusculo e titulo:
curso = "pYtHon"

print(curso.upper()) #PYTHON
print(curso.lower()) #python
print(curso.title()) #Python

#Eliminando espaços em branco:
curso_1 = " Python "

print(curso_1.strip())   # "Python"
print(curso_1.lstrip())  # "Python "
print(curso_1.rstrip())  #" Python"

#Junções e centralização:
curso_2 = "Python"
print(curso_2.center(10, "#")) #"##Python##"
print(".".join(curso_2))  #"P.y.t.h.o.n"
# ----------------
nome = "aUréLIa"
print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá mundo!    "
print(texto)
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# INTERPOLAÇÃO DE VARIÁVEIS
""" INTRODUÇÃO: Em Python temos 3 formas de interpolar variáveis em strings, a primeira
é usando  o sinal %, a segunda é utilizando o método format e a última é utilizando f strings.
    A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, por esse motivo 
iremos focar nas 2 últimas. """

#Old style %
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no no curso de %s."%(nome, idade, profissao, linguagem))
# >>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho com Programador e estou matriculado no no curso de Python.

#Método format
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no no curso de {}.".format(nome, idade, profissao, linguagem))
# >>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho com Programador e estou matriculado no no curso de Python.

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no no curso de {0}.".format(linguagem, profissao, idade, nome))
# >>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho com Programador e estou matriculado no no curso de Python.

#f-string
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no no curso de {linguagem}.")
# >>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho com Programador e estou matriculado no no curso de Python.

#formatar strings com f-strings
PI =3.14159
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

#------------
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

print("Nome: %s Idade: %s" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(nome, idade))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

#criando um dicionario 
dados = {"nome": "Aurélia", "idade": 35}
print("Nome {nome} Idade {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}" )

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# FATIAMENTO DE STRINGS
""" INTRODUÇÃO: Fatiamento de strings é uma técnica utilizada para retornar substrings (partes 
da string original), informando inicio (star), fim(stop) e passo(step): [start:stop[,step]] """

nome = "Aurélia Christina Bagagim Amador Covre"

print(nome[0]) #>>> A
print(nome[:9]) #>>> Aurélia C
print(nome[10:]) #>>> ristina Bagagim Amador Covre
print(nome[10:16]) #>>> ristin
print(nome[10:16:2]) #>>> rsi
print(nome[:]) #>>> Aurélia Christina Bagagim Amador Covre
print(nome[::-1]) #>>> ervoC rodamA migagaB anitsirhC ailéruA

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# STRING MÚLTIPLAS LINHAS
""" INTRODUÇÃO: Strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas
durante a atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em branco 
são incluídos na string final. """

nome = "Aurélia"

mensagem = f"""
Olá meu nome é {nome}, 
Eu estou aprendendo Python.
"""
print(mensagem)
# >>> Olá meu nome é Aurélia, 
# >>> Eu estou aprendendo Python.

print("""
    ============= MENU ===========
 
    1 - Depositar
    2 - Sacar
    0 - Sair

    ==============================
    
        Obrigado por usar nosso sistema!!!!
