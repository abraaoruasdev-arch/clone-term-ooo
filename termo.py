import random
from functions import banner, acertouLetraAmarelo, acertouLetraVerde


# Variavel para pegar as palavras na lista
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    palavras = [linha.strip() for linha in arquivo]

banner() # Interface no terminal

# Escolhendo palavra para o jogo
palavraSecreta1 = random.choice(palavras)
tentativas = 6

for numeroTentativa in range(1, tentativas + 1):
    # Mostra qual a tentativa e pede a adivinhação
    print("Tentativa:", numeroTentativa)
    chute = input("").strip().lower()

    # Verificando se tentativa é valida
    if len(chute) != len(palavraSecreta1):
        print("Tentativa invalida, digite uma palavra com 5 letras!")
        continue

    resultado = ""
    letrasRestantes = {}

    for i in range(len(palavraSecreta1)):
        if palavraSecreta1[i] != chute[i]:
            letrasRestantes[palavraSecreta1[i]] = letrasRestantes.get(palavraSecreta1[i], 0) + 1

    # Verificando cada letra por letra e comparando com a palavra secreta
    for i in range(len(palavraSecreta1)):

        # LETRA CORRETA NA POSICAO CORRETA = VERDE
        if chute[i] == palavraSecreta1[i]:
            resultado += acertouLetraVerde(chute[i])
        # LETRA ESTA NA PALAVRA (FORA DA POSICAO CORRETA) = AMARELA
        elif chute[i] in letrasRestantes and letrasRestantes[chute[i]] > 0:
            resultado += acertouLetraAmarelo(chute[i])
            letrasRestantes[chute[i]] -= 1
        else:
            resultado += chute[i]

    print(resultado)

    if chute == palavraSecreta1:
        print("Parabens, voce acertou!!!")
        break
else:
    print("Voce perdeu, muitas tentativas! A palavra certa era:\n", palavraSecreta1)