# Conjuntos
alunos_curso1 = {15, 23, 43, 56}
alunos_curso2 = {13, 23, 56, 42}

for aluno in alunos_curso1:
    print(aluno)

for aluno in alunos_curso2:
    print(aluno)

# OR
# Alunos no Curso 1 ou no Curso 2 ou em ambos
print(alunos_curso1 | alunos_curso2) # {42, 43, 13, 15, 23, 56}

# AND
# Alunos no Curso 1 e no Curso 2
print(alunos_curso1 & alunos_curso2) # {56, 23}

# MINUS
# Alunos no Curso 1 mas não no Curso 2
print(alunos_curso1 - alunos_curso2) # {43, 15}
# Alunos no Curso 2 mas não no Curso 1
print(alunos_curso2 - alunos_curso1) # {42, 13}

# OR EXCLUSIVE, NEGATIVE AND
# Alunos no Curso 1 ou no Curso 2, mas não em ambos
print(alunos_curso1 ^ alunos_curso2) # {42, 43, 13, 15}

# Dicionários
texto = "Bem vindo eu me chamo Vinícius e eu gosto muito de Python e tenho duas gatas e gosto muito delas".lower()
contador_palavras = {}

for palavra in texto.split():
    contador = contador_palavras.get(palavra, 0)
    contador_palavras[palavra] = contador + 1

print(contador_palavras)
