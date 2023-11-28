menu = """

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

=> """

saldo = 0
extrato = ""
SAQUE_LIMITE = 3
limite = 500
numero_saques = 0


while True:
    opcao = int(input(menu))
    
    if opcao == 1:
        valor = float(input("Digite o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= SAQUE_LIMITE
        
        if excedeu_saldo:
            print("Operação falhou! O valor solicitado é maior que o saldo em conta...")
        elif excedeu_limite:
            print("Operação falhou! Você excedeu o limite de saque permitido...")
        elif excedeu_saque:
            print("Operação falhou! Você excedeu a quantidade de saques diários...")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido")
    elif opcao == 3:
        print("\n=============== EXTRATO ===============")
        print("Não foram realizado movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("\n=======================================")
    elif opcao == 4:
        break
    
    else:
        print("Operação inválida, por favor seleciona novamente a opção desejada!")