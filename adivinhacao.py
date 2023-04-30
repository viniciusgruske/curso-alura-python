import random

def jogar():
    print('*********************************')
    print('Bem-vindo ao jogo de adivinhação!')
    print('*********************************')

    secret_number = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print('Dificuldade:')
    print('[1] Fácil')
    print('[2] Médio')
    print('[3] Difícil')
    nivel = int(input('Defina o nível de dificuldade: '))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print(f'Tentativa {rodada} de {total_tentativas}')
        palpite = int(input('Digite número entre 1 e 100: '))

        if (palpite < 1 or palpite > 100):
            print('Você deve digitar um número inteiro entre 1 e 100!')
            print('Você perdeu uma tentativa')
            continue

        acertou = palpite == secret_number
        is_maior = palpite > secret_number
        is_menor = palpite < secret_number

        print('Você digitou', palpite)

        if (acertou):
            print('Você acertou!')
            print(f'Sua pontuação foi {pontos}')
            break
        else:
            if (is_maior):
                print('Você errou! O seu palpite é maior que o número.')
            elif (is_menor):
                print('Você errou! O seu palpite é menor que o número.')
            pontos -= abs(secret_number - palpite)
    else:
        print(f'Suas tentativas acabaram. O número secreto era {secret_number}!')
    print('Fim de Jogo')

if (__name__ == '__main__'):
    jogar()