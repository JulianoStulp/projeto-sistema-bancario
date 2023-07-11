
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        valor_deposito = float(input("Digite o valor para depósito:"))
        
        if int(valor_deposito) <= 0:
            while valor_deposito <= 0:
                valor_deposito = float(input("Valor inválido, digite um valor maior que zero para deposito:"))

        saldo += valor_deposito
        extrato += f" + DEPOSITO: R$ {valor_deposito:.2f}\n"
        print("\nValor depositado com sucesso!")

    elif opcao == "s":
        
        if numero_saques == LIMITE_SAQUES:
            print("\nNão é possível realizar mais saques, limite diário extendido")
            continue
        
        valor_saque = float(input("\nDigite o valor para depósito:"))

        if valor_saque <= 0:
            while valor_saque <= 0:
                valor_saque = float(input("\nValor inválido, digite um valor maior que zero para saque:"))
        
        if valor_saque > saldo:
            while valor_saque > saldo:
                valor_saque = float(input("\nValor digitado para saque maior que o valor do saldo, digite um valor para saque:"))

        if valor_saque > limite:
            while valor_saque > limite:
                valor_saque = float(input("\nValor digitado para saque maior que o limite diário, digite um valor para saque:"))

        saldo -= valor_saque
        extrato += f" - SAQUE:    R$ {valor_saque:.2f}\n"
        numero_saques += 1
        print("\nValor sacado com sucesso!")

    elif opcao == "e":
        print("\n--------------------- Extrato ---------------------")
        print(extrato)
        print(f" = Saldo: {saldo:.2f}")
        print("---------------------------------------------------")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")