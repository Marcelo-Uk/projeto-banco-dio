menu = """

Bem Vindo!
Escolha uma opção para continuar:

1 - Depositar
2 - Sacar
3 - Extrato
9 - Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 3
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Você selecionou Depósito!")
        print("Digite o valor a ser depositado: ")

        deposito = float(input())
        saldo += deposito
        extrato.append((deposito, "(deposito)"))

        print(f"\nValor depositado: R$ {deposito:.2f}!")
        print(f"Saldo Atual: R$ {saldo:.2f}")

    
    elif opcao == "2":
        print("Você selecionou Saque!")
        print(f"Seu saldo no momento é de: R$ {saldo:.2f}")
        print(f"Você possui {numero_saques} saques restantes para hoje.")
        print("Seu limite para saque é de R$ 500")

        if numero_saques > 0 and numero_saques <= 3:
            print("Digite o valor a ser sacado: ")
            
            saque = float(input())  

            if (saque <= limite):
                if(saque <= saldo):
                    saldo -= saque
                    numero_saques -= 1
                    extrato.append((saque, "(saque)"))
                    print(f"Valor sacado: R$ {saque:.2f}")
                    print(f"Quantidade de saques diários restantes: {numero_saques}")
                    print(f"Saldo Atual: R$ {saldo:.2f}")
                else:
                    print("Saldo insuficiente. Tente um valor menor para o saque.")
            else:
                print("Valor excede o limite diário! Tente um valor menor.")
        else:
            print("Você excedeu o limite de saques diários.")
    
    elif opcao == "3":        
        if not extrato:
            print("Não foram realizadas movimentações!")
        else:
            for valor in extrato:
                valor

            extrato_formatado = ', '.join(f'R$ {valor:.2f} {tipo}' for valor, tipo in extrato)
            print(f"Extrato: {extrato_formatado}")
            print(f"Seu saldo no momento é de: R$ {saldo:.2f}")
    
    elif opcao == "9":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
