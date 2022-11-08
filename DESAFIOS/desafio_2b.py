""" Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em
português. Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em
francês. Nico, amigo de Humberto, ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele
levanta as duas?”. Antes que Humberto pudesse responder, o papagaio gritou: “Aí eu caio, idiota!”.
Entrada: A entrada consiste de diversos casos de teste. Cada caso de teste consiste uma string 
informando qual a situação de levantamento de pernas do papagaio.
Saída: Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará.
Caso ele levante ambas as pernas, imprima “caiu”. Quebre uma linha a cada caso de teste.
 
Entrada   | Saída
esquerda  | ingles 
direita   | frances 
nenhuma   | portugues
ambas     |  caiu     """

# while True significa que, enquanto houver entradas, o código após o try continuará sendo executado
import os

try:
    while True: 
        os.system('cls')
        papagaio = input()
        if papagaio == "esquerda":
            print("ingles")
        if papagaio == "direita":
            print("frances")
        if papagaio == "nenhuma":
            print("portugues")
        if papagaio == "ambas":
           print("caiu")  
        else:
            break              
except Exception as e:
    print("ERRO no main:", str(e))

""" Dado de entrada:
esquerda

direita

nenhuma

ambas

Saída esperada:
ingles

frances

portugues

caiu
Sua Saída:
ingles
"""