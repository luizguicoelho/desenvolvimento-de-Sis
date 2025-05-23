from conta import Conta

conta1 = Conta(123, "10500-10", "Luiz", 7500.0, 1234)
print(f'Saldo disponivel: {conta1.extrato()}')


conta1.saque(-2000.0)
print(f'Saldo disponivel: {conta1.extrato()}')

conta1.deposito(99.0)
print(f'Saldo disponivel: {conta1.extrato()}')
