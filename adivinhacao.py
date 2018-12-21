import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dficuldade?")
    print("(1) Fácil (2) Médio (3)Difícil")

    nivel = int(input("Define o nível:"))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #tem que colocar o +1 se não, ele nao vai até o último número, posição final não é inclusiva
    for rodada in range(1,total_de_tentativas+1):
        print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        #tem que passar para int, se nao ele compara uma string e mostra resultado errado, tudo que passa para input é string
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            #pula pra próxima iteração
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto")
            #escreve assim pq o else não aceita condição
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()
