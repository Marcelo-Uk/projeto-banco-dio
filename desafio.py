def menu():
    menu = """
    Escolha uma opção para continuar:

    1 - Depositar
    2 - Sacar
    3 - Extrato
    9 - Sair

    => """
    return input(menu)

def depositar(saldo, deposito, extrato):
    print("\nVocê selecionou Depósito!")

    deposito = float(input("Digite o valor a ser depositado: R$ "))

    if(deposito > 0):
        saldo += deposito
        extrato.append((deposito, "(deposito)"))

        print(f"\nValor depositado: R$ {deposito:.2f}!")
        print(f"Saldo Atual: R$ {saldo:.2f}")
    else:
        print("Valor incorreto. Tente novamente")

    return saldo, deposito, extrato

def sacar(saldo, numero_saques, limite, extrato):
    print("\nVocê selecionou Saque!\n")
    print(f"Seu saldo no momento é de: R$ {saldo:.2f}")
    print(f"Você possui {numero_saques} saques restantes para hoje.")
    print(f"Seu limite para saque é de R$ {limite}")

    if numero_saques > 0 and numero_saques <= 3:
        saque = float(input("Digite o valor a ser sacado: R$ "))  
        if (saque <= limite):
            if(saque <= saldo):
                saldo -= saque
                numero_saques -= 1
                extrato.append((saque, "(saque)"))
                print(f"\nValor sacado: R$ {saque:.2f}")
                print(f"Quantidade de saques diários restantes: {numero_saques}")
                print(f"Saldo Atual: R$ {saldo:.2f}")
            else:
                print("\nSaldo insuficiente. Tente um valor menor para o saque.")
        else:
            print("\nValor excede o limite diário! Tente um valor menor.")
    else:
        print("\nVocê excedeu o limite de saques diários.")
    
    return (saldo, numero_saques, limite, extrato)

def exibir_extrato(saldo, extrato):
    if not extrato:
        print("Não foram realizadas movimentações!")
    else:
        extrato_formatado = ', '.join(f'R$ {valor:.2f} {tipo}' for valor, tipo in extrato)
        print(f"Extrato: {extrato_formatado}")
    
    print(f"Seu saldo no momento é de: R$ {saldo:.2f}")
    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    deposito = 0
    extrato = []
    numero_saques = LIMITE_SAQUES

    while True:
        opcao = menu()

        if opcao == "1":
            saldo, deposito, extrato = depositar(saldo, deposito, extrato)

        elif opcao == "2":
            saldo, numero_saques, limite, extrato = sacar(saldo, numero_saques, limite, extrato)

        elif opcao == "3":
           exibir_extrato(saldo, extrato)

        elif opcao == "9":
            break

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")

main()

