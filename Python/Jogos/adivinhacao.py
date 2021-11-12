print("*******************")
print("JOGO DA ADIVINHACAO")
print("*******************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):

    #print("Tentativa", rodada, "de", total_de_tentativas)
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu numero: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print("Voce acertou!")
    else:
        if maior:
            print("Voce errou! O seu chute foi maior que o numero correto.")
        else:
            print("Voce errou! O seu chute foi menor que o numero correto.")
    rodada = rodada + 1