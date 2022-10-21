### CURSO: TIPOS DE OPERADORES COM PYTHON 
# Instrutor: Guilherme Carvalho

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# OPERADORES DE ARITMÉTICOS
""" Objetivo Geral: O que são operadores de aritméticos e como utilizá-los.
    O que são? São operadores aritméticos executam operações matemáticas, como 
    adição, subtração com operandos.""" 

""" PRECEDÊNCIA DOS OPERADORES: Na matemática existe uma regra que indica quais operações 
    devem ser executadas primeiro. Isso é útil pois ao analisar uma expressão, a depender da 
    ordem das operações o valor pode ser diferente: 
    x = 10 - 5 * 2 
    x é igual a 10 ou 0?  

    A definição indica a seguinte ordem como a correta:
    - Parêntesis
    - Expoêntes
    - Multiplicações e divisões (da esquerda para a direita)
    - Somas e subtrações (da esquerda para a direita)
     """

print(10 - 5 * 2) #0
print((10 - 5) * 2) #10
print(10 ** (2 * 2)) #1000
print(10 / 2 * 4) #20     



produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)  #ADIÇÃO
print(produto_1 - produto_2)  #SUBTRAÇÃO
print(produto_1 / produto_2)  #DIVISÃO
print(produto_1 // produto_2) #DIVISÃO INTEIRA: Retorna o resultado da divisão com n. inteiro
print(produto_1 * produto_2)  #MULTIPLICAÇÃO
print(produto_1 % produto_2)  #MÓDULO: resto da divisão
print(produto_1 ** produto_2) #EXPONENCIAÇÃO


x = (10 + 5) * 4
y = (10 / 2) * (25 * 2) - (2 ** 2)
print(x)
print(y)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# OPERADORES DE COMPARAÇÃO
""" Objetivo Geral: O que são operadores de comparação e como utilizá-los.
    O que são? São operadores utilizados para comparar dois valores. """ 

saldo = 450
saque = 200

print(saldo == saque)  #False
print(saldo != saque)  #True
print(saldo > saque)  #True
print(saldo >= saque)  #True
print(saldo < saque)  #False
print(saldo <= saque)  #False


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# OPERADORES DE ATRIBUIÇÃO
""" Objetivo Geral: O que são operadores de atribuição e como utilizá-los.
    O que são? São operadores utilizados para definir o valor inicial ou sobrescrever 
    o valor de uma variável. """ 

saldo = 500

saldo += 200 #Uma forma reduzida de somar o valor da atribuição com o valor da variável.   
print(saldo)

saldo -= 100 #Uma forma reduzida de subtrair o valor da atribuição com o valor da variável. 
print(saldo)

saldo *= 2   #Uma forma reduzida de multiplicar o valor da atribuição com o valor da variável.
print(saldo)

saldo /= 5   #Uma forma reduzida de dividir o valor da atribuição com o valor da variável.
print(saldo)

saldo //= 5  #divisão inteira 
print(saldo)

saldo %= 480 #Modolo, que no caso seria o valor entre os 500 e 480
print(saldo)

saldo **= 2  #Exponenciação. 80 elevado ao quadrado 
print(saldo)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# OPERADORES DE LÓGICOS
""" Objetivo Geral: O que são operadores de lógicos e como utilizá-los.
    O que são? São operadores utilizados em conjunto com os operadores de comparação, para montar
    uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é 
    um boleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos,
    exemplo: op_comparacao + op_logico + op_comparacao...N... """ 

#saldo = 1000
#saque = 200
#limite = 100

#saldo >= saque and saque <= limite #Para retornar True, todos tem que ser vdd 
#saldo >= saque or saque <= limite  #Para retornar False, todos tem que ser falsos 


#Operador de Negação
# comparando uma situação, se ela for falsa o resultado é vdd
# not 1000 > 1500 #True
# not contatos_emergencia #True
# not "sAque 1500;" #True
# not " " #True

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# OPERADORES DE IDENTIDADE (is)
""" Objetivo Geral: O que são operadores de identidade e como utilizá-los.
    O que são? São operadores utilizados para comparar se os dois objetos 
    testados ocupam a mesma posição na memória.""" 

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso #True
curso is not nome_curso #False
saldo is limite # True

# ---------
saldo = 1000
limite = 1000

print(saldo is limite) #saldo ocupa a mesma posição de memoria que limite? False
print(saldo is not limite) # Saldo não ocupa a mesma posição de memoria que limite! True

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# OPERADORES DE ASSOCIAÇÃO
""" Objetivo Geral: O que são operadores de associação e como utilizá-los.
    O que são? São operadores utilizados para verificar se um objeto está 
    presente em uma sequência.""" 

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso #True
"maçã" not in frutas #True
200 in saques #False

# ------------------
frutas = ["limao", "uva", "laranja"]
curso = "Curso de Python"

print("laranja" in frutas) #True
print("limao" not in frutas) #False
print("Python" in curso) #True

