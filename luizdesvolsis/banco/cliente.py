from conta import Conta 
import getpass
import csv

contas = []
with open('contas.csv', newline = "", encoding = 'utf-8', errors = 'ignore') as lerCont:
    leitor = csv.reader(lerCont, delimiter = ',')
    for l in leitor:
        conta = Conta(l[0], l[1], l[2], l[3], l[4])
        contas.append(conta)
print(contas)

agencia = int(input(f'Digite o número da sua agencia: '))
numCon = input(f'Digite o número da conta: ')
senha = getpass.getpass(f'Digite sua senha: ')

