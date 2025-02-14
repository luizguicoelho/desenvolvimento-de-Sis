import random

s = random.randint(1,10)

print("#### BEM VINDO AO JOGO ####")
print("Adivinhe o número de 1 a 10")
c = int(input("Qual é o número?:" ))

if c == s:
    print("Você acertou")
else:
    print("Você errou")

print("O seu número é:", s,)    

