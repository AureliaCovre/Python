### CURSO: APRENDENDO A UTILIZAR DICIONÁRIOS EM PYTHON 
# Link: https://web.dio.me/course/aprendendo-a-utilizar-dicionarios-em-python/learning/d60c0324-9369-4e88-9354-abc1dfc876a7?back=/track/geracao-tech-unimed-bh-ciencia-de-dados&tab=undefined&moduleId=undefined
#GitHub: https://github.com/digitalinnovationone/trilha-python-dio/tree/01_estrutura_de_dados/01%20-%20Estrutura%20de%20dados/04%20-%20Dicion%C3%A1rios
# Instrutor: Guilherme Arthur de Carvalho

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=
# DICIONÁRIOS
"""Objetivo geral: Entender o funcionamento da estrutura de dados dicionário """

""" Um dicionário é um conjunto não ordenado de pares chave:valor, onde as chaves são únicas
em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, 
e contém uma lista de pares chave: valor separada por vírgulas."""

# -------------
print("Declarando Dicionários...")
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

#Adicionando uma chave ao dicionário já existente:
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
print("--------------")

# -------------
print("Acessando Dados...")
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
print("--------------")

# -------------
print("""Dicionários Aninhados: Dicionários podem armazenar qualquer tipo de objeto em Python como 
valor, desde que a CHAVE para esse valor seja um objeto imutável como (strings e números)""")

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

#Para acessar o valor telefone, passamos a chave unica e a chave telefone:
telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print("Telefone: ",telefone)
print("--------------")

# -------------
print("Iterando Dicionários...")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("-" * 10)

for chave, valor in contatos.items():
    print(chave, valor)
print("--------------")

# -------------
print("Método Clear: Apaga todos os valore sdo dicionário....")

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.clear()
print(contatos)  # {}
print("--------------")

# -------------
print("Método Copy: Gera uma cópia do dicionário...")

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}
print("--------------")

# -------------
print("""Método Fromkeys: Cria a chave sem vincular valores ou cria um conjunto de chaves com 
mesmo valor...""")

resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
print("--------------")

# -------------
print(""" Método GET: Utilizado quando não temos certeza se a chave existe no dicionário. Aceita
tambem um valor default, se le não encontra o 1 argumento ele retorna o 2 ...""")

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError #Simulando um erro

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
print("--------------")

# -------------
print(""" Método ITEMS: Retorna uma lista de tuplas...""")
# Items
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
print(resultado)
print("--------------")

# -------------
print(""" Método Keys: Retorna apenas as chaves do dicionário ...""")
# Keys

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)
print("--------------")

# -------------
print(""" Método POP: Remove uma chave no dicionário e mostra o que esta removendo ...""")
# pop
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
#resultado = contatos.pop("guilherme@gmail.com", "não encontrado")  # é o mesmo q a linha acima
print(resultado)
print("--------------")

# -------------
print(""" Método POPITEM: Remove os itens na sequencia ...""")
# popitem
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError
print("--------------")

# -------------
print(""" Método SETDEFAULT: Se o atributo não constar no dicionário ele add, se constar 
ele respeita a que já existe não altera ...""")
# setdefault
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
print("--------------")

# -------------
print(""" Método UPDATE: Atualiza o dicionário com outro dicionário ...""")
# update
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
print("--------------")

# -------------
print(""" Método VALUES: Retorna os valores, ou seja todos os dicionários que estão amarrados 
ás chaves  ...""")
# values

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])  # noqa
print(resultado)
print("--------------")

# -------------
print(""" Método IN: Verifica se uma chave existe ou não no dicionário...""")
# in

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)
print("--------------")

# -------------
print(""" Método DEL: Remove objetos ...""")

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)
