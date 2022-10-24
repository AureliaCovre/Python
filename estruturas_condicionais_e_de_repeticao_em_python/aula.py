### CURSO: ESTRUTURAS CONDICIONAIS E DE REPETIÇÃO COM PYTHON 
# Link: https://web.dio.me/course/estruturas-condicionais-e-de-repeticao-em-python/learning/f9b78902-9c92-4a12-b411-9b78a56b15d1
# Instrutor: Guilherme Arthur de Carvalho

### CURSO: TIPOS DE OPERADORES COM PYTHON 
# Instrutor: Guilherme Carvalho

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# INDENTAÇÃO E BLOCO DE COMANDO
""" A estética: Identar código é uma forma de manter o código fonte mais legível e manutenível. 
Mas em Python ela exerce um segundo papel, através da indentação o interpretador consegue 
determinar onde o bloco de comando inicia e onde ele termina. 
    
    Bloco de comando: As linguagens de programação constumam utilizar caracteres ou palavras
reservadas para terminar o início e o fim do bloco. Em Java e C por exemplo utiliza-se chaves.
    
    Utilizando espaços: Existe uma convenção em Python, que define as boas práticas para escrita
de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de
indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco. 
"""

# ESTRUTURAS CONDICIONAIS (if/ if-else/ elif)
""" Objetivo geral: O que são as estruturas condicionais e como utilizá-las.
    O que são? A estrutura condicional permite o desvio de fluxo de controle, quando 
    determinadas expressões lógicas são atendidas. """

""" if: Para criar uma estrutura condicional simples, composta por um único desvio, podemos
utilizar a palavra reservada if. O comando irá testar a expressão lógica, e em caso de retorno 
verdadeiro as ações presentes no bloco de código do if serão executadas. """  

saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")    


""" if/else: Para criar uma estrutura condicional com dois desvios,podemos utilizar as palavras 
reservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o 
bloco de código do if será executado, CAso contrário o bloco de código do else será executado. """ 

saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")   


""" if/elif/else: Em alguns cenários queremos mais de dois descios, para isso podemos utilizar 
a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso 
retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs 
que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a 
complexidade do código. """

opcao= int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))
    # .... continua o código....
elif opcao ==2:
    print("Exibindo o extrato... ")
else:
    #sys.exit("Opção inválida!")  
    print("Opção Inválida!)

#-------------
maior_idade = 18
idade_especial = 17

idade = int(input("Informe a sua idade: "))

if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")

if idade < maior_idade:
    print("Ainda não pode tirar a CNH.")   

#Exemplo 2:
if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")     
elif idade == idade_especial:
    print("Pode fazer aulas teóricas, masnão pode fazer as aulas práticas.")    
else:
    print("Ainda não pode tirar a CNH.")    


""" if aninhado: Podemos criar estruturas condicionais aninhadas, para isso basta adicionar
estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else. """  
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else: 
        print("Saldo insuficiente!")  
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com seu gerente")        


""" if ternário: O if ternário permite escrever uma condição em uma única linha. Ele é 
composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, 
a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não 
seja atendida.  """  

saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")


# ESTRUTURAS DE REPETIÇÃO (for / while)
""" Objetivo geral: Conhecer as estruturas de reperição for e while e quando utilizá-las.
    O que são ? São utilizadas para repetir um trecho de código um determinado número de vezes.
Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.  
"""

#Receba um núro do teclado e exiba os 2 números seguintes:
a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)
a += 1
print(a)

#pegando o mesmo exemplo com estrutura de repetição...
a = int(input("Informe um número inteiro: "))
print(a)

#repita 2 vezes:
#    a += 1
#    print(a)

""" Comando for: O comando for é usado para percorrer um objeto iterável. Faz senntido 
usar for quando sabemos o número exato de vezes que o nosso bloco de código deve ser executado,
ou quando queremos percorrer um objeto iterável. """
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:        
    print() #adiciona uma quebra de linha        

#Exemplo utilizando a função built-in range
for numero in range(0, 51,5):
    print(numero, end=" ")

""" Comando while: O comando while é usado para repetir um bloco de código várias vezes. Faz sentido
usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.""" 

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!") 

#Estrutura com break
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)    

#Exemplo com for:
for numero in range(100):
    if numero == 10:
        break #Para quando atingir a execução (10)
        #continue #Pula a execução (10)

    print(numero, end=" ")   
