menu = """
deposito = [d]
saque = [s]
extrato = [e]
sair = [0]
"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("\nQual valor você deseja depositar? Digite: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido")
        
    elif opcao == "s":
        valor = float(input("Valor do saque: "))
        excedeusaldo = valor > saldo
        excedeulimite = valor > limite
        excedeusaques = numero_saques >= LIMITE_SAQUES

        if excedeusaldo:
            print("Erro. Você não tem saldo suficiente!")
        elif excedeulimite:
            print("Erro. O valor de saque excede o limite!")
        elif excedeusaques:
            print("Erro. Número máximo de saques excedido!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Erro. O valor informado é inválido!")

    elif opcao == "e":
        print("\n============== EXTRATO ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSeu extrato é: {saldo:.2f}")
        print("=====================================")

    elif opcao == "0":
        print ("Saindo...")
    
        break
    
    else:
        print("Digite uma opção válida")