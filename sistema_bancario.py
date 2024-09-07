menu = """
###########Bem-vindo ao Seu Banco###########
          Escolha a opção desejada:
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
        print("Depósito")
        s = float(input("Insira o valor desejado para depósito: "))
        saldo += s
        print(f"Valor de {s:.2f} depositado com sucesso")
        extrato += f"Depósito de R$ {s:.2f} \n"

    elif opcao == "s":

        s = float(input("Informe o valor a ser sacado: "))

        if numero_saques == LIMITE_SAQUES:
            print("Limite de saques atingido, somente amanhã poderá realizar outro saque.")
      

        if s > saldo:
            print(f"Saldo insulficiente para saque, seu saldo é de: R$ {saldo:.2f}")

        elif s > limite:
            print(f"Valor informado acima do permitido, seu limite atual é de R$ {limite:.2f},00")
        
        elif numero_saques < LIMITE_SAQUES and s <= saldo and s <= limite:
            saldo -= s
            print(f"Valor sacado de RS {s:.2f}")
            extrato += f"Saque de R$ {s:.2f} \n"
            numero_saques += 1


    elif opcao == "e":
        if extrato == "":
            print("Você ainda não realizou movimentações de sua conta.")
        
        else:
            print("Extrato")
            print(f"Essas foram suas movimentações: \n {extrato}")
            print(f"O seu saldo é R$ {saldo:.2f}")

    elif opcao == "q":
        print("Saindo do sistema, obrigado por fazer parte do Seu Banco.....")
        break

    else:
        print("Operação inválida.Por favor selecione a operação desejada!")
