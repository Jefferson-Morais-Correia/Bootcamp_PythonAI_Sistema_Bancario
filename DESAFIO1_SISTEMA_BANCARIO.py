
menu = """

                    ==========DIGITE_A_OPERAÇÃO_DESEJADA==========
                                [1]-Deposito
                                [2]-Saque
                                [3]-Extrato
                                [4]-Sair
                    ==============================================
=>
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Operação falhou. O valor informado é inválido!")

    elif opcao == "2":
        valor = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente em conta.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite de saque.")

        elif excedeu_saques:
            print("Operação falhou! Número de saques doi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Operação Falhou! O valor informado é inválido.")


    elif opcao == "3":
        print ("\n=============== EXTRATO ================")
        print ("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\nSaldo:R$ {saldo: .2f}")
        print ("========================================")


    elif opcao == "4":
        
        break

    else:

        print("Operação inválida, por favor selecione a operação desejada!")