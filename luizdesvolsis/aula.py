import random


s = random.randint(1,10)

print("#### BEM VINDO AO JOGO ####")
print("Adivinhe o número de 1 a 10")

t = 1
while (lt >= t):
    print("tentativa", t)
    c = int(input("Qual é o número?:" ))
    if (c == s):
        print("Parabéns, você acertou!")
        break #termina o jogo se o usuário acertar
    elif (c > s):
        print("Quase! tente um menor")
    elif (c < s):
        print("Quase! tente um maior")    


    t = t + 1


print("O seu número é:", s,)    
   
