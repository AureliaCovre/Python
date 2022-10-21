# Instrutor: Guilherme Carvalho


produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = (10 + 5) * 4
y = (10 / 2) * (25 * 2) - (2 ** 2)
print(x)
print(y)

# -----------------------------
# OPERADORES DE COMPARAÇÃO
""" Objetivo Geral: O que são operadores de comparação e como utilizá-los.
    O que são? São operadores utilizados para comparar dois valores. """ 


# -----------------------------
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

# -----------------------------
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

# -----------------------------
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

# ----------------------
saldo = 1000
limite = 1000

print(saldo is limite) #saldo ocupa a mesma posição de memoria que limite? False
print(saldo is not limite) # Saldo não ocupa a mesma posição de memoria que limite! True
