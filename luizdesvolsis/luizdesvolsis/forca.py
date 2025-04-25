import random

print("Digite o número correspondente do tema escolhido")
print("##### 1 = Comidas, 2 = esportes, 3 = Roupas #####")
numero_tema = int(input("Digite o número escolhido: "))

lista_palavras = []
if numero_tema == 1:
    print("Você escolheu o tema 'Comidas'")
    arquivo = open("comida.txt", "r")
elif numero_tema == 2:
    print("Você escolheu o tema 'Nomes'")
    arquivo = open("esporte.tt", "r")
elif numero_tema == 3:
    print("Você escolheu o tema 'Dia a Dia'")
    arquivo = open("roupa.txt", "r")
else:
    print("TU É BURRO POR ACASO?!!!!!")
    exit()

for linha in arquivo:
        lista_palavras.append(linha.strip())    

palavra_secreta = random.choice(lista_palavras)

limite_tentativas = len(palavra_secreta) * 2

acertou = False
errou = False

letras_adivinhadas = []
for letra in palavra_secreta:
    letras_adivinhadas.append("_")


tentativa = 1
while not acertou and not errou:
    print(letras_adivinhadas)
    print("Tentativas:", tentativa, "/", limite_tentativas)
    letra_digitada = input("Digite uma letra: ")

    indice = 0
    for letra in palavra_secreta:
        if letra_digitada == letra:
            letras_adivinhadas[indice] = letra
        indice += 1


    if tentativa == limite_tentativas:
        errou = True
        print("Você perdeu!")
        print("A palavra era:", palavra_secreta)


    if "_" not in letras_adivinhadas:
        acertou = True
        print("Parabéns, você encontrou a palavra secreta!")
        print(letras_adivinhadas)

    tentativa += 1