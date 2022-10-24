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

print(curso.upper())
print(curso.lower())
print(curso.title())

#Eliminando espaços em branco:
curso_1 = " Python "

print(curso_1.strip())   # "Python"
print(curso_1.lstrip())  # "Python "
print(curso_1.rstrip())  #" Python"

#Junções e centralização:
curso_2 = "Python"
print(curso.center(10, "#")) #"##Python##"
print(".".join(curso_2))  #"P.y.t.h.o.n"
