from bytebank import Funcionario

# vinicius = Funcionario('Vinicius Gruske', '27/02/1996', 5000)

# print(vinicius.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '27/02/1996', 2650)
    print(f'Teste = {funcionario_teste.age()}')

teste_idade()