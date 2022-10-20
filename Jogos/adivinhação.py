import random


def jogar():

    print("*********************************")
    print('Bem vindo ao jogo de adivinhação!')
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil, (2) Médio, (3) Difícil')

    nivel = int(input("Defina o nível: "))
    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print(f"Tentativa {rodada} de {total_tentativas}")

        chute = int(input('Digite o seu número entre 1 e 100: '))
        print(f'Você digitou {chute}')

        if chute < 1 or chute > 100:
            print("Você deve digitar um numero entre 1 e 100!")
            continue
        if numero_secreto == chute:
            print(f'Voce acertou e fez {pontos}')
            break
        else:
            if chute > numero_secreto:
                print('Você errou! O seu chute foi maior do que o número secreto')
            if chute < numero_secreto:
                print('Você errou! O seu chute foi menor do que o número secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print(f"O número secreto era {numero_secreto}")
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()





