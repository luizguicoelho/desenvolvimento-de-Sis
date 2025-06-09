from conta import Conta 
import getpass
import random
import csv
def escreveArq(agencia, num, titular,saldo, senha):
    with open('contas.csv', 'a', newline='') as cvsfile:
        escritor = csv.writer(cvsfile, delimiter=',')
        escritor.writerow([agencia, num, titular, saldo, senha])


#
#
#def __init__(self, agencia, num, titular, saldo, senha):
#conta2 = Conta(123, "10500-11", "Guilerme", 1000.0, 1234)



while(True):
    print(f'Crie as contas:')
    cinN = str(random.randint(10000, 99999))
    twoN = str(random.randint(10, 99))
    agencia = int(input("Qual o número da agência: "))
    num = f'{cinN}-{twoN}'
    titular = input("Digite o nome do titular: ")
    saldo = 0
    senha = int(getpass.getpass(f'Crie a senha:'))
    escreveArq(agencia, num, titular, saldo, senha)
    novaConta = Conta(agencia, num, titular, saldo, senha)
    print(f'Conta {novaConta.num} criado com sucesso!\n')
