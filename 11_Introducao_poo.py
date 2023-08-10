### CURSO: INTRODUÇÃO À PROGRAMAÇÃO ORIENTADA A OBJETOS(POO) COM PYTHON
# Link: https://web.dio.me/course/introducao-poo/learning/9aaf0076-a2e6-4d6e-b106-889460797859?back=/track/geracao-tech-unimed-bh-ciencia-de-dados&tab=undefined&moduleId=undefined
# GitHub: https://github.com/digitalinnovationone/trilha-python-dio/tree/02_programacao_orientada_objetos/02%20-%20Programa%C3%A7%C3%A3o%20Orientada%20a%20Objetos
# Instrutor: Guilherme Carvalho

""" Uma clase define as características e comportamentos de um objeto, porém não conseguimos usá-las 
diretamente. Já os objetos podemos usá-los e eles possuem as características e comportamentos que 
foram definidos nas classes. """

""" Desafio: João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um 
programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, 
parar e correr. Adicione esses compartamentos! """

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        #pass #Palavra que encerra o método
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmm....")   

    #def __str__(self):
    #    return f"Bicicleta: cor={self.cor}, modelo={self.modelo}. ano={self.ano}, valor={self.valor}"      

    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


#b1 = Bicicleta("vermelha", "caloi", 2022,600) 
#b1.buzinar()
#b1.correr()
#b1.parar()
#print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
b2.buzinar() #Bicicleta.buzinar(b2)

""" CONSTRUTORES E DESTRUTORES """

""" O método construtor(inicializador) sempre é executado quando uma nova instância da classe é criada. Nesse método
inicializamos o estado do nosso objeto. Para declarar o método construtor da classe, criamos um método
com nome __init__. """

""" Método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em
Python não são tão necessários quanto em C++ porque o Python tem um coletor de lixo que lida com o 
gerenciamento de  memória automaticamente. Para declarar o método destrutor da classe, criamos um 
método com o nome __del__. """  

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")    

    def falar(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

c = Cachorro("Chappie", "Amarelo")
c.falar()     

print("Ola mundo!")

del c 

print("Ola mundo!")
print("Ola mundo!")
print("Ola mundo!")

#criar_cachorro()
