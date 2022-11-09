### CURSO: DOMINANDO FUNÇÕES PYTHON
# Link: https://web.dio.me/course/dominando-funcoes-python/learning/065ecbd9-7623-486d-b10f-28efc150d00f?back=/track/geracao-tech-unimed-bh-ciencia-de-dados&tab=undefined&moduleId=undefined
#GitHub: https://github.com/digitalinnovationone/trilha-python-dio/tree/01_estrutura_de_dados/01%20-%20Estrutura%20de%20dados/05%20-%20Fun%C3%A7%C3%B5es
# Instrutor: Guilherme Arthur de Carvalho


""" Objetivo Geral: Entender como funcionam as funções em Python."""

""" O que são funções: Função é um bloco de código identificado por um nome e pode receber uma lista
de parâmetros, esses parâmetros podem não ter valores padrões. Usar funções torna o código mais 
legível e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer
que esta,ps ŕpgramando de maneira estruturada.  """


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# 

# -------------
# Primeira função
def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

print("--------------")

# -------------
""" Retornando valores: Para retornar um valor, utilizamos a palavra reservada return. 
Toda função Python retorna None por padrão. Diferente de outras linguagens de programação, em 
Python uma função pode retornar mais de um valor. """

#Retornano da função
def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
print("--------------")

# -------------
""" Argumentos nomeados: Funções também podem ser chamadas usando argumentos nomeados da forma 
chave=valor. """

#Argumentos nomeados
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
print("--------------")

# -------------
""" Args e Kwargs: Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são 
definidos (*args e **kwargs), o método recebe os valores como tuplas e dicionário respectivamente.
    args = vem como tuplas
    kwargs = vem como dicionário """

# args_kwargs
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Quinta-feira, 27 de Outubro de 2022",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)

print("--------------")

# -------------
""" Parâmetros especiais: Por padrão, argumentos podem ser passados para uma função Python tanto 
por posição quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido
restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas
olhar para a definição da função para dererminar se os itens são passados por posição, 
por posição e nome, ou por nome. """

#Parametros somente por posição copy.py
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

print("--------------")

# -------------
#Parametros somente por nome
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

print("--------------")

# -------------
""" Objetos de primeira classe: Em Python tudo é objeto, desa forma funções também são objetos o que as 
também são objetos o que as tornam objetos de primeira classe. Com isso podemos atribuir funções a 
variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados (listas, 
tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures). """

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20

print("--------------")

# -------------
""" Escopo Local e Global: Python trabalha com escopo local e global, dentro do bloco da função o escopo
é local. Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de 
ser executado. Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador
que a variável que está sendo manipulada no escopo local é global. Essa NÃO é uma boa prática e deve ser 
evitada. """

salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500
