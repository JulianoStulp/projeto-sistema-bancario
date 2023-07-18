import textwrap

def saque(*, saldo, extrato, limite, valor_saque, numero_saques):
    
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
    extrato += f" - SAQUE:\tR$ {valor_saque:.2f}\n"
    numero_saques += 1

    print("\nValor sacado com sucesso!")

    return saldo, extrato, numero_saques

def depositar(valor_deposito, saldo, extrato, /):
    
    if int(valor_deposito) <= 0:
        while valor_deposito <= 0:
            valor_deposito = float(input("Valor inválido, digite um valor maior que zero para deposito:"))

    saldo += valor_deposito
    extrato += f" + DEPOSITO:\tR$ {valor_deposito:.2f}\n"

    print("\nValor depositado com sucesso!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    print("\n--------------------- Extrato ---------------------")
    print(extrato)
    print(f" = Saldo:\t{saldo:.2f}")
    print("---------------------------------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com esse CPF")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro, cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criaca com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    
    menu = """\n
    ========== MENU ==========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [lc]\tListar Conta
    [q]\tSair

    => """

    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:

        opcao = input(textwrap.dedent(menu))

        if opcao == "d":

            valor_deposito = float(input("Digite o valor para depósito:"))
            
            saldo, extrato = depositar(valor_deposito,
                                       saldo,
                                       extrato)
            
        elif opcao == "s":
            
            if numero_saques == LIMITE_SAQUES:
                print("\nNão é possível realizar mais saques, limite diário extendido")
                continue
            
            valor_saque = float(input("\nDigite o valor para depósito:"))

            saldo, extrato, numero_saques = saque(saldo=saldo, 
                                                  extrato=extrato, 
                                                  limite=limite,
                                                  valor_saque=valor_saque, 
                                                  numero_saques=numero_saques)

        elif opcao == "e":

            exibir_extrato(saldo, 
                        extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1

            conta = criar_conta(AGENCIA, 
                                numero_conta, 
                                usuarios)
            
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()