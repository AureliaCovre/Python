""" A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo 
com a tabela abaixo:

Salário             | Percentual de Reajuste
0 - 600.00          | 17%   
600.01 - 900.00     | 13%
900.01 - 1500.00    | 12%
1500.01 - 2000.00   | 10%
Acima de 2000.00    | 5%
	
Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o
índice reajustado, em percentual.
A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas
decimais, conforme exemplos abaixo.

Exemplo 1
Entrada 	Saída
1000     	Novo salario: 1120,00 
            Reajuste ganho: 120,00                                                                                     
            Em percentual: 12 %

Exemplo 2
Entrada 	Saída
2000 	    Novo salario: 2200,00                                                                                                   
            Reajuste ganho: 200,00                                                                                                  
            Em percentual: 10 %          """

# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e 
# o índice reajustado (em porcentagem)

salario = int(input("Qual o seu salário? ")) 
#aumento = salario * percentual
#novo_salario = salario + aumento

if salario <= 600:
    percentual = 0.17
    novo_salario = salario + (salario * percentual)
    aumento = salario * percentual
    percentual_1 = percentual * 100
    print("{:.2f} \n{:.2f} \n{:.0f} %".format(novo_salario, aumento, percentual_1)) 
elif salario >= 600.01 <= 900:
    percentual = 0.13
    novo_salario = salario + (salario * percentual)
    aumento = salario * percentual
    percentual_1 = percentual * 100
    print("{:.2f} \n{:.2f} \n{:.0f} %".format(novo_salario, aumento, percentual_1)) 
elif salario > 900 <= 1500:
    percentual = 0.12
    novo_salario = salario + (salario * percentual)
    aumento = salario * percentual
    percentual_1 = percentual * 100
    print("{:.2f} \n{:.2f} \n{:.0f} %".format(novo_salario, aumento, percentual_1)) 
elif salario > 1500 <= 2000:
    percentual = 0.10
    novo_salario = salario + (salario * percentual)
    aumento = salario * percentual
    percentual_1 = percentual * 100
    print("{:.2f} \n{:.2f} \n{:.0f} %".format(novo_salario, aumento, percentual_1))     
else:
    percentual = 0.10
    novo_salario = salario + (salario * percentual)
    aumento = salario * percentual
    percentual_1 = percentual * 100
    print("{:.2f} \n{:.2f} \n{:.0f} %".format(novo_salario, aumento, percentual_1))    
    

"""if salario <= 600:
    percentual = 0.17
elif salario >= 600.01 < 900:
    percentual = 0.13
elif salario > 900 <= 1500:
    percentual = 0.12
elif salario > 1500 <= 2000:
    percentual = 0.10
else:
    percentual = 0.05"""

"""
if salario <= 600:
    percentual = 0.17
    print("Novo salario: {:.2f}, \nReajuste ganho: {:.2f}, \nEm percentual: {:.0f} %".format(novo_salario, aumento, (percentual *100)) )
elif salario >= 600.01 <= 900:
    print("Novo salario: ", (salario + (salario * 0.13)), "Reajuste ganho: ", salario * 0.13, "Em percentual: 13%")
elif salario > 900 <= 1500:
    print("Novo salario: ", (salario + (salario * 0.12)), "Reajuste ganho: ", salario * 0.12, "Em percentual: 12%")
elif salario > 1500 <= 2000:
    print("Novo salario: ", (salario + (salario * 0.10)), "Reajuste ganho: ", salario * 0.10, "Em percentual: 10%")
else:
    print("Novo salario: ", (salario + (salario * 0.05)), "Reajuste ganho: ", salario * 0.05, "Em percentual: 5%")
"""