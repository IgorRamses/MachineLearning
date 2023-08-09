# Crie uma função que receba  uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa,
# e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

listaDeTuplas = [
    ("João", 25),
    ("Maria", 30),
    ("Carlos", 22),
    ("Ana", 28),
    ("Pedro", 35),
    ("Lúcia", 40),
    ("Miguel", 19),
    ("Sofia", 27),
    ("Rafael", 31),
    ("Isabela", 23),
    ("Fernando", 29),
    ("Laura", 26),
    ("Eduardo", 33),
    ("Camila", 24),
    ("Gustavo", 38),
    ("Larissa", 21),
    ("Antônio", 45),
    ("Natália", 32),
    ("Rodrigo", 36),
    ("Carolina", 34)
]

print(sorted(listaDeTuplas)) #Exibindo a lista em ordem alfabética pessoa por pessoa

print()
# Outro modo de visualizar a lista
listaDeTuplas = sorted(listaDeTuplas) # Deixando a lista em ordem alfabética.
for person in listaDeTuplas:
    print(person) # Exibindo uma pessoa por linha