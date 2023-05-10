import random
###################################################################################################
def play_game():
    print_welcome()

    secret_word = load_secret_word()

    right_letters = hide_secret_word(secret_word)
    
    player_is_hanged = False
    player_is_right = False
    attempts_left = 6

    print_gallow(attempts_left)
    print(' '.join(right_letters))
   
    while (not player_is_hanged and not player_is_right):
        player_guess = input("Qual a letra? ").strip().upper()

        if player_guess in secret_word:
            reveal_right_letters(secret_word, right_letters, player_guess)
        else:
            attempts_left -= 1

        player_is_hanged = attempts_left <= 0
        player_is_right = '_' not in right_letters

        print_gallow(attempts_left)
        print(' '.join(right_letters))
    
    if player_is_right:
        print_victory()
    else:
        print_defeat(secret_word)
    print('Fim de Jogo')
###################################################################################################
def print_welcome():
    print('***************************')
    print('Bem-vindo ao jogo da forca!')
    print('***************************')
###################################################################################################
def print_gallow(attempts_left):
    print("  _______     ")
    print(" |/      |    ")
    if (attempts_left == 0):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")
    if(attempts_left == 1):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")
    if(attempts_left == 2):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")
    if(attempts_left == 3):
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |       |    ")
        print(" |            ")
    if(attempts_left == 4):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")
    if(attempts_left == 5):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if(attempts_left >= 6):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    print(" |            ")
    print("_|___         ")
###################################################################################################
def print_defeat(secret_word):
    print('Você se enforcou!')
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \\       ")
    print("  /                 \\      ")
    print("//                   \\/\\  ")
    print("\\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \\__      XXX      __/     ")
    print("   |\\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \\_             _/       ")
    print("     \\_         _/         ")
    print("       \\_______/           ")
###################################################################################################
def print_victory():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
###################################################################################################
def load_secret_word(archive="words.txt"):
    words = []
    with open(archive, 'r', encoding='UTF-8') as archive_words:
        for linha in archive_words:
            words.append(linha.strip())

    return words[random.randint(0, len(words))].upper()
###################################################################################################
def hide_secret_word(secret_word):
    return ['_' for letter in secret_word]
###################################################################################################
def reveal_right_letters(secret_word, right_letters, player_guess):
    index = 0
    for letter in secret_word:
        if (player_guess == letter):
            right_letters[index] = letter
        index += 1
###################################################################################################
if (__name__ == '__main__'):
    play_game()