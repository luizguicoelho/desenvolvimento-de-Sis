nam = "Luiz Coelho"
num = 21
a = 175
mf = ""
ff = "a"
IMD = 0



print("## Bem vindo ao sistema ##")
print("O sistema feito por", nam, ", n°", num)
"""
print("Digite a sua altura('em centimetro= 160'):")
alt1 = int(input())
if a <= alt1:
    print("Você é maior que eu")
elif a >= alt1:
    print("Você é menor que eu")
else:
    print("Temos o mesmo tamanho")


5
c = 0
m_p = []

while c < 3:
    m = input("Digite uma música que você gosta: ")
    m_p.append(m)
    c += 1

if mf in m_p:
    print("Você gosta da minha muica favorita")
else:
    print("Você nâo gosta da minha muica favorita")
"""


f_p = []
IMb_p = []
i = 0

for i in range(3):
    print(i)
    f = input("Digite um do seus filmes favoritos: ")
    IMDb = int(input("Digite a nota do IMDb dele:"))
    f_p.append(f)
    IMb_p.append(IMDb)

c = 0
while c < 3:
    f = f_p[c]
    I = IMb_p[c]


    print("O seu filme", f, "tem")
    if I >= IMD:
        print("uma nota menor que o meu")
    else:
        print("uma nota maior que o meu")

    c += 1