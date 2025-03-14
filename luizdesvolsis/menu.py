import random

print("Digite o número do Nível digitado")
print("Fácil=1 , Médio=2 , Díficil=3")
n_d = int(input("digite o número de dificuldade:"))
 
if (n_d == 1):
    print("Você escolheu o nível fácil")
    n_m = 10
    lt = 3
elif (n_d == 2):
    n_m = 50
    lt = 5
    print("você escolheu a dificuldade Média")

elif (n_d == 3):
    n_m = 100
    lt = 7
    print("você escolheu a dificuldade Díficil")
elif (n_d >= 4):
    print("você escolheu uma dificuldade inválida")
    exit()

s = random.randint(1, n_m)
print("#### BEM VINDO AO JOGO ####")
print("Adivinhe o número de 1 a", n_m)

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
print("o seu número é", s)

    