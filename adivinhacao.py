import random

def jogar():

    print("**********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("**********************************")


    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade? ")
    print("[1] Fácil  [2] Médio  [3] Difícil")
    nivel = int(input("Define o nível: "))

    while True:
        if nivel == 1:
            total_de_tentativas = 20
            break
        elif nivel == 2:
            total_de_tentativas = 10
            break
        elif nivel == 3:
            total_de_tentativas = 5
            break
        else:
            nivel = int(input("Por Favor, Digite um nível de 1 a 3: "))
            continue



    for rodada in range(1, total_de_tentativas + 1) :
        print(f"Tentativa {rodada} de {total_de_tentativas}")

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou" , chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue


        maior   = chute > numero_secreto
        menor   = chute < numero_secreto
        acertou = chute == numero_secreto

        if (acertou):
            print(f"Você acertou! Você fez {pontos} pontos.")
            break
        else:
            if(maior):
                print("Você errou! o seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! o seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print(f"O numero era {numero_secreto}")
    print("Fim do Jogo.")
if(__name__ == "__main__"):
    jogar()