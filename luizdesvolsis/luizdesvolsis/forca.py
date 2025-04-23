#importa a biblioteca random
import random


print("Digite o número correspondente do tema escolhido")
print("##### 1 = Comidas, 2 = nomes, 3 = Dia a Dia#####")
n_t = int(input("Digite o número escolhiado:"))

if(n_t == 1):
    print("Você escolheu o tema comidas")
    ps = []
    arq = open("ccomida.txt", "r")
    for lin in arq:
        ps.append(lin.strip())
elif(n_t == 2):
    print("Você escolheu o tema 'Nomes' ")
    ps = []
    arq = open("nome.txt", "r")
    for lin in arq:
        ps.append(lin.strip()) 
elif(n_t == 3):
    print("Você escolheu o tema 'Dia a Dia' ")
    ps = []
    arq = open("diaAdia.txt", "r")
    for lin in arq:
        ps.append(lin.strip())
elif():
    print("Digito Errado")
    exit()         

#configurando inicial das variáveis
p = random.choice(ps)
lim_ten = len(p) * 2
a = False
e = False

#cria o esqueleto da palavra
ls_ace = []
for l in p:
    ls_ace.append("_")

#contador
cont = 1

#cri um laço de repetição 
while(not a and not e):# O jogo continua enquanto o jogador não acertar (a) ou perder (e)
    print(ls_ace)
    print("Tentativas: ", cont, "/", lim_ten)
    c = input("digite a letra: ")

    #percorre o esqueleto, e se a letra for igual,troca
    i = 0
    for l in p:
        if c == l:
            ls_ace[i] = c
        i += 1

    #Condição de derrota
    if cont == lim_ten :
        e = True   
        print("Você perdeu")
        print("A palavra era: ", p)
    
    #Condição de vitória
    if ls_ace.count("_") == 0:
        a = True
        print( "Parabéms, você encontrou a palavra secreta!")
        print(ls_ace)

    #controle de laço de repetição
    cont += 1    


