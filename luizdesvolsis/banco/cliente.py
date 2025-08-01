from conta import Conta 
import maskpass
import csv

contas = []
conEnc = None
acessLiberado = False

def lerArquivo():
    with open('contas.csv', newline="", encoding='utf-8', errors='ignore') as lerCont:
        leitor = csv.reader(lerCont, delimiter=',')
        for l in leitor:
            conta = Conta(int(l[0]), l[1], l[2], float(l[3]), l[4])
            contas.append(conta)

def encontraConta(agencia, numCon):
    global conEnc
    for conta in contas:
        if conta.agencia == agencia and conta.num == numCon:
            conEnc = conta
    return None

def verificaAcess(numCon, senha):
    global acessLiberado
    if conEnc is not None:
        if conEnc.entrar(numCon, senha):
            print(f'Acesso liberado')
            acessLiberado = True
        else:
            print(f'Senha incorreta')
    else:
        print(f'Conta não encontrada')

def procurarConta(num):
    for conta in contas:
        if conta.num == num:
            return conta
    return None

def inicia():
    global acessLiberado
    global conEnc
    acessLiberado = False
    conEnc = None

    lerArquivo()
    agencia = int(input(f'Digite o número da sua agencia: '))
    numCon = input(f'Digite o número da conta: ')
    senha = maskpass.askpass(prompt="Digite sua senha: ", mask="*")

    encontraConta(agencia, numCon)
    verificaAcess(numCon, senha)

inicia()

while acessLiberado:
    print(f'\nEscolha o número da opção desejada:')
    print(f'1 - Extrato')
    print(f'2 - Saque')
    print(f'3 - Depósito')
    print(f'4 - Transferir')
    print(f'5 - Sair')
    print()
    try:
        transacao = int(input('Digite a opção: '))
    except ValueError:
        print(f'Por favor, digite um número válido.')
        continue

    if transacao == 1:
        print(f'O saldo da conta é R$:{conEnc.extrato()}')

    elif transacao == 2:
        try:
            valor = float(input('R$: '))
            sucesso = conEnc.sacar(valor)
            if sucesso:
                print(f'Saque realizado')
            else:
                print(f'Saque inválido')
        except ValueError:
            print(f'Valor invalido, digite um numero')        

    elif transacao == 3:
        try:
            valor = float(input('R$: '))
            sucesso = conEnc.depositar(valor)
            if sucesso:
                print(f'Depósito realizado')
            else:
                print(f'Depósito negado')
        except ValueError:
            print(f'Valor invalido, digite um numero')  

    elif transacao == 4:
        try:
            valor = float(input(f'R$: '))
            num = input(f'Número Conta: ')
            contaDestino = procurarConta(num)
            if contaDestino:
                sucesso = conEnc.transferir(valor, contaDestino)
                if sucesso:
                    print(f'Transferência realizada')
                else:
                    print(f'Transferência negada')
            else:
                print(f'Conta destino não encontrada')
        except ValueError:
            print(f'Valor invalido, digite um numero')  

    elif transacao == 5:
        print(f'Saindo... Obrigado!')
        break

    else:
        print(f'Opção incorreta')

    print()


'''
from conta import Conta 
import maskpass
import csv

contas = []
agencia = int(input('Digite o número da sua agencia: '))
numCon = input('Digite o número da conta: ')
senha = maskpass.askpass(prompt="Digite sua senha: ", mask="*")
conEnc = None
acessLiberado  = False


def lerArquivo():
    with open('contas.csv', newline="", encoding='utf-8', errors='ignore') as lerCont:
        leitor = csv.reader(lerCont, delimiter=',')
        for l in leitor:
            conta = Conta(int(l[0]), l[1], l[2], float(l[3]), l[4])
            contas.append(conta)

def encontraConta():
    global conEnc
    for conta in contas:
        if numCon == conta.num and agencia == conta.agencia:
            conEnc = conta
            break 
def verificaAcess():
    global conEnc
    global acessLiberado
    if conEnc is not None:
        if conEnc.entrar(numCon, senha):
            print('Acesso liberado')
            acessLiberado = True
        else:
            print('Senha incorreta')
    else:
        print('Conta não encontrada')

def inicia():
    lerArquivo()
    encontraConta()
    verificaAcess()

inicia()

if acessLiberado == True:
    while(True):
        print(f'Escolha o numero da opção desejada')
        print(f'1 - Extrato')
        print(f'2 - Saque')
        print(f'3 - Depósito')
        print(f'4 - Transferir')
        print(f'5 - Sair')
        transacao = int(input(f'Digite a opção:'))
        if transacao == 1:
            print(f'O saldo da conta é R$:{conEnc.extrato()}')
        elif transacao == 2:
            conEnc.sacar(float(input(f'R$:')))
            if conEnc.sacar == True:
                print(f'Saque realizado')
            else:
                print(f'Saque inválido')
        elif transacao == 3:
            conEnc.depositar(float(input(f'R$:')))
            if conEnc.depositar == True:
                print(f'Depósito realizado')
            else:
                print('Depósito negado')
        elif transacao == 4:
            conEnc.transferir(float(input(f'R$:')), (input(f'Numero Conta:')))
            if conEnc.transferir == True:
                print(f'Transferencia realizada')
            else:
                print(f'Transferencia negada')
        elif transacao == 5:
            inicia()
        else:
            print(f'Opção incorreta')

'''