import forca
import adivinhacao

def escolha_jogos():
    print("**********************************")
    print("Escolha o seu jogo!")
    print("**********************************")


    print("(1) Forca  (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolha_jogos()