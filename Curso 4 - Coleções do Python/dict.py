# Dicionários
####################################################################################################

# texto = "Bem vindo eu me chamo Vinícius e eu gosto muito de Python e tenho duas gatas e gosto muito delas".lower()
# contador_palavras = {}

# for palavra in texto.split():
#     contador = contador_palavras.get(palavra, 0)
#     contador_palavras[palavra] = contador + 1

# print(contador_palavras)

####################################################################################################

# from collections import defaultdict

# texto = "Bem vindo eu me chamo Vinícius e eu gosto muito de Python e tenho duas gatas e gosto muito delas".lower()
# contador_palavras = defaultdict(int)

# for palavra in texto.split():
#     contador_palavras[palavra] += 1

# print(contador_palavras)

####################################################################################################

# from collections import Counter

# texto = "Bem vindo eu me chamo Vinícius e eu gosto muito de Python e tenho duas gatas e gosto muito delas".lower()
# contador_palavras = Counter(texto.split())

# print(contador_palavras)

####################################################################################################

# from collections import defaultdict

# class Conta:
#   def __init__(self):
#     print("Criando uma conta")

# contas = defaultdict(Conta)

# contas[15] # Cria novas contas, pois a chave não existe e será criada com o o defaultdict()
# contas[20] # Cria novas contas, pois a chave não existe e será criada com o o defaultdict()
# print(contas) 
# contas[15] # Não cria novas contas, pois a chave já existe
# contas[20] # Não cria novas contas, pois a chave já existe
# print(contas)
# contas[15] = Conta() # Cria novas contas, pois é uma atribuição de um novo valor na chave
# contas[20] = Conta() # Cria novas contas, pois é uma atribuição de um novo valor na chave
# print(contas)

####################################################################################################

from collections import Counter

texto1 = """
Python também inclui um tipo de dados para conjuntos, chamado set. Um conjunto é uma coleção desordenada de elementos, sem elementos repetidos. Usos comuns para conjuntos incluem a verificação eficiente da existência de objetos e a eliminação de itens duplicados. Conjuntos também suportam operações matemáticas como união, interseção, diferença e diferença simétrica.

Chaves ou a função set() podem ser usados para criar conjuntos. Note: para criar um conjunto vazio você precisa usar set(), não {}; este último cria um dicionário vazio, uma estrutura de dados que discutiremos na próxima seção.
"""

texto2 = """
Um recomendação importante a ser feita é que antes de fazer a solicitação de servidores de CDN ou de um PNI por exemplo, é importante realizar uma avaliação detalhada do tráfego que o seu ASN troca com os ASNs desses geradores de conteúdo. Ferramentas como NetFlow e PeeringDB auxiliam bastante. Cerifique-se que você atende à TODOS os requisitos antes de fazer a solicitação, principalmente se possui a quantidade de mínima de tráfego para ser elegível. Esses servidores somente são enviados aos ISPs no caso das empresas de CDN verificarem que eles trazem benefícios para ambos CDN e ISP, caso contrário dificilmente serão enviados. Hospedar e manter um servidor de CDN é algo que demanda recursos do provedor como espaço em rack, portas de switch e principalmente um consumo razoável de energia elétrica por isso uma avaliação criteriosa é bastante importante antes de realizar a solicitação.

Outro detalhe imprescindível na hora de solicitar um servidor de CDN, Peering por Sessão Bilateral ou PNI é o IPv6. Devido à crescente importância deste protocolo algumas CDNs hoje em dia tem colocado restrições caso você não seja capaz de estabelecer uma sessão IPv6 com eles.Além disso caso você possua IPv6 em seu backbone porém ainda não está distribuindo para os usuários residencias e possui apenas CGNAT44 a maioria das grandes CDNs já possuem suporte completo à IPv6 portanto uma parte significativa do seu tráfego poderia estar fluindo preferencialmente em IPv6 ao invés de estar passando por equipamentos que fazem o GGNAT a um custo computacional maior além de ter a identificação do usuário facilitada em caso de uma solicitação baseada no Marco Civil da Internet.
"""

def imprime_top_letras_mais_comuns_no_texto(texto, ranking):
    contador_letras = Counter(texto.lower())
    total_letras = sum(contador_letras.values())
    for letra, contador in contador_letras.most_common(ranking):
        print(f'\'{letra}\':{contador / total_letras * 100:.2f}%')

def get_imprime_top_letras_mais_comuns_no_texto(texto, ranking):
    contador_letras = Counter(texto.lower())
    total_letras = sum(contador_letras.values())
    proporcao_letras = [(letra, contador / total_letras) for letra, contador in contador_letras.items()]
    return Counter(dict(proporcao_letras)).most_common(ranking)


imprime_top_letras_mais_comuns_no_texto(texto1, 3)
print(get_imprime_top_letras_mais_comuns_no_texto(texto1, 3))
imprime_top_letras_mais_comuns_no_texto(texto2, 3)
print(get_imprime_top_letras_mais_comuns_no_texto(texto2, 3))