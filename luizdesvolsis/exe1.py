cuM = [900, 350, 300, 400,]
gaM = [1400, 700, 500, 200]

def s(Lis):
    s = Lis[0] + Lis[1] + Lis[2] + Lis[3]
    return s 

salP = s(gaM)
salN = s(cuM)

sal = salP - salN

print("O seu ganho esse mês foi de:" , salP )
print("O seus gastos esse mês foi de:", salN )
print("O seu saldo no mês é de:", sal)