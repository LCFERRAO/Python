import random


def jogar():

    abertura()
    palavra_secreta = palavra()

    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute not in palavra_secreta:
            erros += 1
            desenha_forca(erros)
        else:
            chute_correto(palavra_secreta, chute, letras_acertadas)

        enforcou = erros == 7
        if enforcou:
            break

        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print('Parabéns você ganhou!')
    else:
        print('Você foi enforcado! :( ')
        print(f'A palavra secreta era {palavra_secreta}')


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")


def abertura():
    print("***************************")
    print('Bem vindo ao jogo de Forca!')
    print("***************************")


def palavra():
    arquivo = open("palavras.txt", 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1




if __name__ == "__main__":
    jogar()

