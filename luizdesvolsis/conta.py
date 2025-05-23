class Conta:
    def __init__(self, agencia, num, titular, saldo, senha):
        self.__agencia = agencia
        self.__num = num
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha

    def extrato(self):
        return self.__saldo

    def saque(self, valor):
        if valor < 0 or valor > self.__saldo:
            return False
        else:
            self.__saldo -= valor
            return True     

    def deposito(self, valor):
        if valor < 0:
            return False
        else:    
            self.__saldo += valor
            return True 

        
