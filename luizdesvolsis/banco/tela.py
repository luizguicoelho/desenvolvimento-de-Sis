from conta import Conta

#import getpass
#import pwinput
#import maskpass







conta1 = Conta(123, "10500-10", "Luiz", 7500.0, 1234)
conta2 = Conta(123, "10500-11", "Guilerme", 1000.0, 1234)

con = input('Digite o seu número da conta: ')

#sen = int(getpass.getpass('Digite a sua senha: '))
#sen = int(pwinput.pwinput('Digite a sua senha: '))
#sen = int(maskpass.askpass(prompt="Digite sua senha: ", mask="*"))

print(f'Saldo disponivel: {conta1.extrato()}')

if conta1.entrar(con,sen):
    print("Bem Vindo Luiz")
else:
    print("Senha incorreta")   

valor = float(input("Digite o valor que quer depositar:"))

if conta1.transferir(valor, conta2):
    print(f'Valor de {valor} transferido')
else:
    print(f'Tranferencia negada')   

print(f'Saldo disponivel: {conta3.extrato()}')
print(f'Saldo disponivel: {conta2.extrato()}')

conta1.sacar(2000.0)
print(f'Saldo disponivel: {conta1.extrato()}')

conta1.depositar(99.0)
print(f'Saldo disponivel: {conta1.extrato()}')

