from conta import Conta
import json
import re

def criar_conta():
    agencia = int(input("Digite o número da agência: "))
    num = validar_numero_conta()
    titular = input("Digite o nome do titular: ")
    saldo = 0
    senha = int(input("Crie a senha da conta: "))

    nova_conta = Conta(agencia, num, titular, saldo, senha)

    salvar_conta_em_arquivo(nova_conta)

    print("Conta criada com sucesso!")


def validar_numero_conta():
    while True:
        num = input("Digite o número da conta (*****-**): ")

        if re.match(r"^\d{5}-\d{2}$", num):
            return num
        else:
            print("Número de conta inválido! O formato deve ser *****-**.")


def carregar_contas_do_arquivo():
    try:
        with open("contas.json", "r") as arquivo:
            return json.load(arquivo) 
    except (FileNotFoundError, json.JSONDecodeError):
        return []  


def salvar_conta_em_arquivo(conta):
    try:
        with open("contas.json", "r") as arquivo:
            dados_contas = json.load(arquivo) 
    except (FileNotFoundError, json.JSONDecodeError):
        dados_contas = []  


    for i, conta_existente in enumerate(dados_contas):
        if conta_existente["num"] == conta._Conta__num:  
            dados_contas[i]["saldo"] = conta._Conta__saldo
            dados_contas[i]["senha"] = conta._Conta__senha
            dados_contas[i]["titular"] = conta._Conta__titular
            dados_contas[i]["agencia"] = conta._Conta__agencia
            break
    else:
        dados_contas.append({
            "agencia": conta._Conta__agencia,
            "num": conta._Conta__num,
            "titular": conta._Conta__titular,
            "saldo": conta._Conta__saldo,
            "senha": conta._Conta__senha
        })



def entrar_conta():
    num_conta = input("Digite O seu número da conta")
    senha = int(input("Digite a sua senha"))

    contas = carregar_contas_do_arquivo()

    for conta in contas:
        if conta["num"] == num_conta and conta["senha"] == senha:
            print(f"Bem-vindo, {conta['titular']}!")
            conta_obj = Conta(conta["agencia"], conta["num"], conta["titular"], conta["saldo"], conta["senha"])
            menu_operacoes(conta_obj) 
            return

    print("Número da conta ou senha incorretos. Tente novamente.")

def carregar_contas_do_arquivo():
    try:
        with open("contas.json", "r") as arquivo:
            return json.load(arquivo)  
    except (FileNotFoundError, json.JSONDecodeError):
        return []  


def menu_operacoes(conta):
    while True:
        print("\n1. Consultar saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Alterar senha")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print(f"Saldo atual: R${conta.extrato()}")
        elif escolha == "2":
            try:
                valor = float(input("Digite o valor para depósito: R$"))
                conta.depositar(valor)
                salvar_conta_em_arquivo(conta)  
                print("Depósito realizado com sucesso!")
            except ValueError:
                print("Valor inválido! Por favor, insira um número válido.")
        elif escolha == "3":
            try:
                valor = float(input("Digite o valor para saque: R$"))
                senha = input("Digite a senha para saque: ")
                conta.sacar(valor, senha)
                salvar_conta_em_arquivo(conta)  
            except ValueError:
                print("Valor inválido! Por favor, insira um número válido.")
        elif escolha == "4":
            senha_antiga = input("Digite a senha antiga: ")
            senha_nova = input("Digite a nova senha: ")
            conta.alterar_senha(senha_antiga, senha_nova)
            salvar_conta_em_arquivo(conta)  
        elif escolha == "5":
            print("Saindo...")
            break  
        else:
            print("Opção inválida. Tente novamente.")   


def main():
    while True:
        print("\n1. Criar nova conta")
        print("2. Entrar na conta")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_conta()
        elif escolha == "2":
            entrar_conta()
        
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()        
