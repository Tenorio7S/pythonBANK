menu = """
==========================================
Bem-vindo ao PythonBANK! 
Escolha uma das opções abaixo para realizar suas operações bancárias:
[d] Depositar
[s] Sacar
[t] Transferir
[e] Extrato
[q] Sair
==========================================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

contas = {"1234-5": 1000}  # Exemplo de conta de terceiros para transferir

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "t":
        conta_destino = input("Informe o número da conta de destino (exemplo: 1234-5): ")
        valor = float(input("Informe o valor da transferência: "))

        if conta_destino in contas and valor > 0:
            if valor <= saldo:
                saldo -= valor
                contas[conta_destino] += valor
                extrato += f"Transferência para {conta_destino}: R$ {valor:.2f}\n"
                print(f"Transferência de R$ {valor:.2f} realizada com sucesso para a conta {conta_destino}.")
            else:
                print("Operação falhou! Saldo insuficiente.")
        else:
            print("Operação falhou! Conta de destino inválida ou valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por usar o PythonBANK!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
