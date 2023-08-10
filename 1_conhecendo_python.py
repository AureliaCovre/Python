#Principais converções que vamos utilizar no nosso dia a dia.

print(int(1.9))
print(int("10"))
print(float("10.10"))
print(float(100))

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print(100/2)
print(100//2)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end="... \n")
print(nome, idade, sep="#")
print(nome, idade, sep="#", end="... \n")

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Nessa aula aprendemos sobre: Como se declara variáveis | Como alterar valor da variáveis | 
# Como definir as constantes | Quais são as convenções e boas práticas para escrever código em Python

nome = "Aurélia"
idade = 35

nome = "Giovana"

print(nome, idade)

limite_sque_diario = 1000

BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"]
print(BRAZILIAN_STATES)
