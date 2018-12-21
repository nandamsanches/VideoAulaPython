import random


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    # enquanto (True)
    while (not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            #print("Tentativa {} de {}".format(erros, len(palavra_secreta)))
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r", encoding="utf-8")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    #entre 0 e o tamanho da lista, da um numero aleatorio
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def pede_chute():
    chute = input("Qual letra?")
    # tira os espaços se usuário digitar palavra com espaços
    # por exemplo tirando o \n também
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra

        index += 1

def imprime_mensagem_perdedor():
     print("Você perdeu!")

def imprime_mensagem_vencedor():
    print("Você ganhou!!")


if(__name__ == "__main__"):
    jogar()