import random

print("********************************")
print("BEM VINDE AO JOGO DA ADIVINHACAO")
print("********************************")

numero_secreto = random.randrange(0,101)
total_de_tentativas = 0
pontos = 1000

print("Qual nivel de dificuldade?")
print("(1) Facil (2) Medio (3) Dificil")

nivel = int(input("Defina o nivel: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print("Voce acertou! e fez {} pontos".format(pontos))
        break
    else:
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        if maior:
            print("O seu chute foi maior que o numero secreto.")
            if(rodada == total_de_tentativas):
                print("O numero secreto era {}. Voce fez {}".format(numero_secreto, pontos))
        elif menor:
            print("Voce errou! O seu chute foi menor que o numero correto.")
            if(rodada == total_de_tentativas):
                print("O numero secreto era {}. Voce fez {}".format(numero_secreto, pontos))

print("Fim do jogo")