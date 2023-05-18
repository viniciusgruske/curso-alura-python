# Objetivo é mostrar indice e valor de uma lista
# Inicia uma lista com idades
idades = [15, 87, 32, 65, 56, 32, 49, 37]

lazy = range(len(idades)) # No 'Lazy Mode', o range não cria uma lista, mas deixa pronto para criar
forced = list(range(len(idades))) # Ao usar o list(), você então força a criação da lista
print(lazy)
print(forced)

for i in range(len(idades)):
    print(i, idades[i])
# 0 15
# 1 87
# 2 32
# 3 65
# 4 56
# 5 32
# 6 49
# 7 37

# Usando o enumerate(), para gerar o resultado acima
lazy = enumerate(idades) 
forced = list(enumerate(idades))
print(lazy)
print(forced)

for indice_e_idade in enumerate(idades):
    print(indice_e_idade)
# (0, 15)
# (1, 87)
# (2, 32)
# (3, 65)
# (4, 56)
# (5, 32)
# (6, 49)
# (7, 37)

# Desempacotando um iterável
for indice, idade in enumerate(idades):
    print(indice, idade)

# Desempacotando um iterável e ignorando alguns valores:
pessoas = [
    ('Vinícius', 'Gruske Dorneles', 27, 2, 1996),
    ('Dilaine', 'Gruske Dorneles', 8, 3, 1967),
    ('Luis Carlos', 'Pereira Dorneles', 27, 10, 1958),
    ('Rafael', 'Gruske Dorneles', 9, 11, 2000)
]
for nome, _, _, _, ano_nascimento in pessoas:
    print(f'{nome} nasceu em {ano_nascimento}.')
