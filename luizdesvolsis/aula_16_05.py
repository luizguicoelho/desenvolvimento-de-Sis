def criar_conta(age, num, tit, sal, lim, sen):
    conta = {
        "age": age,
        "num": num,
        "tit": tit,
        "sal": sal,
        "lim": lim,
        "sen": sen
    }
    return conta 

conta2 = criar_conta(123, "2000-2", "Ciclano", 200.0, 500.0, 1234)
print(f"Agencia: {conta2['age']}, Conta: {conta2['num']} - Saldo {conta2['sal']}")    

nome = "luiz"
print(f"olá mundo! meu nome é {conta2['tit']}")