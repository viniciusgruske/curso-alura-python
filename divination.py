import random

def play_game():
    print('*********************************')
    print('Bem-vindo ao jogo de adivinhação!')
    print('*********************************')

    secret_number = random.randrange(1,101)
    total_attempts = 0
    points = 1000

    print('Dificuldade:')
    print('[1] Fácil')
    print('[2] Médio')
    print('[3] Difícil')
    level = int(input('Defina o nível de dificuldade: '))

    if (level == 1):
        total_attempts = 20
    elif (level == 2):
        total_attempts = 10
    else:
        total_attempts = 5

    for round in range(1, total_attempts + 1):
        print(f'Tentativa {round} de {total_attempts}')
        player_guess = int(input('Digite número entre 1 e 100: '))

        if (player_guess < 1 or player_guess > 100):
            print('Você deve digitar um número inteiro entre 1 e 100!')
            print('Você perdeu uma tentativa')
            continue

        player_is_rigth = player_guess == secret_number
        attempt_is_bigger = player_guess > secret_number
        attempt_is_smaller = player_guess < secret_number

        print('Você digitou', player_guess)

        if player_is_rigth:
            print('Você acertou!')
            print(f'Sua pontuação foi {points}')
            break
        else:
            if attempt_is_bigger:
                print('Você errou! O seu palpite é maior que o número.')
            elif attempt_is_smaller:
                print('Você errou! O seu palpite é menor que o número.')
            points -= abs(secret_number - player_guess)
    else:
        print(f'Suas tentativas acabaram. O número secreto era {secret_number}!')
    print('Fim de Jogo')

if (__name__ == '__main__'):
    play_game()