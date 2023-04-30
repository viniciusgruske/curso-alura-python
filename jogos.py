import adivinhacao
import forca

def escolher_jogo():
    print('*******************')
    print('Escolha o seu jogo!')
    print('*******************')

    print('[1] Adivinhação')
    print('[2] Forca')

    jogo = int(input('Qual jogo você quer jogar? '))

    if (jogo == 1):
        print('Iniciando o jogo da Adivinhação...')
        adivinhacao.play_game()
    elif (jogo == 2):
        print('Iniciando o jogo da Forca...')
        forca.play_game()

if (__name__ == '__main__'):
    escolher_jogo()