import divination
import gallow

def select_game():
    print('*******************')
    print('Escolha o seu jogo!')
    print('*******************')

    print('[1] Adivinhação')
    print('[2] Forca')

    game = int(input('Qual jogo você quer jogar? '))

    if (game == 1):
        print('Iniciando o jogo da Adivinhação...')
        divination.play_game()
    elif (game == 2):
        print('Iniciando o jogo da Forca...')
        gallow.play_game()

if (__name__ == '__main__'):
    select_game()