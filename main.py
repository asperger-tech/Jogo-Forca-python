import random

def play():
    
    print_welcome_message()

    fruits_list = ['abacate','amora','ameixa','acerola','abacaxi','açai','banana','carambola','caju','cereja','cacau','caqui','cupuaçu','damasco','figo',
                   'guarana','jaca','kiwi','laranja','limao','lima','lixia','melancia','mamao','melao','maracuja','manga','maça','tangerina','uva']

    randomic = random.randint(0,29)
    palavra_secreta = fruits_list[randomic]
    letras_acertadas = create_space_letter(palavra_secreta)

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input("Chute uma letra: ")
        chute = chute.strip().lower()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == chute:
                    letras_acertadas[index] = chute
                    print(letras_acertadas)
                index += 1

        else:
            tentativas +=1
    
        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if acertou:
        print_win_message()
    else:
        print_lose_message()
        
    end_game_message(palavra_secreta)

def end_game_message(palavra_secreta):
    print("A palavra era: ",palavra_secreta)
    print('Fim do jogo.')

def print_win_message():
    print("********************")
    print("Você ganhou.")
    print("********************")

def create_space_letter(palavra_secreta):
    return ["_" for letter in palavra_secreta]

def print_lose_message():
    print("********************")
    print("Você perdeu.")
    print("********************")

def print_welcome_message():
    print("****************************")
    print('Bem vindo ao jogo da Forca!')
    print("****************************")


if __name__ == '__main__':
    play()


