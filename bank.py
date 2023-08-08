import random
import textwrap

user_accounts = [{
    "userId": "1",
    "nome": "admin",
    "senha": "123",
    "numero_conta": "123456",
    "data_nascimento": "17/05/1992",
    "cpf": "12345678946",
    "endereco": "teste 123",
    "contato": "teste@email.com",
    "tipo": "Admin",
}]

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 60)
        print(textwrap.dedent(linha))

def transferencia(saldo, valor, extrato, conta_destino, user_accounts):
    usuario_destino = encontrar_usuario_por_conta(conta_destino, user_accounts)

    if usuario_destino is not None:
        if valor > 0 and valor <= saldo:
            saldo -= valor
            extrato += f"Transferência para a conta {conta_destino}: R$ {valor:.2f}\n"
            usuario_destino_saldo = usuario_destino.get("saldo", 0)  # Recuperar saldo do usuário destino
            usuario_destino["saldo"] = usuario_destino_saldo + valor  # Atualizar saldo do usuário destino
            print("\n Transferência realizada com sucesso! ")
            # Atualizar extrato do usuário remetente (se necessário)
            user_accounts[0]["extrato"] = extrato

            return saldo, extrato
        else:
            print("Operação falhou! O valor informado é inválido ou o saldo é insuficiente.")
    else:
        print("Conta de destino não encontrada.")
    
    return saldo, extrato

def encontrar_usuario_por_conta(numero_conta, user_accounts):
    for usuario in user_accounts:
        if usuario["numero_conta"] == numero_conta:
            return usuario
    return None

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Operação concluída! Depósito realizado com sucesso!")
        # Atualizar o histórico de saldo
        historico_saldo.append(saldo)
        user_accounts[0]["historico_saldo"] = historico_saldo
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > 0:
        if valor <= saldo and valor <= limite and numero_saques < limite_saques:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação concluída! Saque realizado.")
            # Atualizar o histórico de saldo
            historico_saldo.append(saldo)
            user_accounts[0]["historico_saldo"] = historico_saldo
        else:
            if saldo < valor:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif numero_saques >= limite_saques:
                print("Operação falhou! Número máximo de saques excedidos.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *,extrato):
    print("\n================ Extrato ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(user_accounts):
    # Gerar um novo ID para o usuário.
    user_id = len(user_accounts) + 1
    numero_conta = random.randint(1, 1000000)

    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, user_accounts)

    if usuario:
        print("\n Já existe usuário com esse CPF! ")
        return
    nome = input("Informe o nome completo: ")
    senha = input("Informe uma senha para Login: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço(logradouro, nro - bairro - cidade/sigla estado): ")
    contato = input("Informe seu telefone email para Contato: ")
    
    user_accounts.append({
        "userId": user_id,
        "nome": nome,
        "senha": senha,
        "numero_conta": numero_conta,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "contato": contato,
        "historico_saldo": [],
        "tipo": "Freemium",
    })
    print(" Usuario criado com sucesso! ")
    return user_accounts

def filtrar_usuario(cpf, user_accounts):
    usuarios_filtrados = [usuario for usuario in user_accounts if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, user_accounts):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, user_accounts)
    if usuario:
        print("\n Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n Usuário não encontrado, fluxo de craição de conta encerrado! ")

def menu():
    menu = """\n
    =============== MENU ===============
    \t[t] Transferir
    \t[b] Informações da conta
    \t[d] Depositar
    \t[s] Sacar
    \t[e] Extrato
    \t[h] Histórico de saldo
    \t[u] Atualizar informações pessoais
    \t[n] Nova conta
    \t[l] Listar contas
    \t[q] Sair

    => """
    return input(menu)

def sign():
    sign = """\n
    ============= SIGN PAGE =============
    \t[i] Sign In
    \t[c] Sign Up
    \t[q] Sair
    => """
    return input(sign)

def authenticate():
    while True:
        value = sign()
        if value == "i":
            password_attempt = input("Digite sua senha: ")
            if password_attempt == user_accounts[0]['senha']:
                return password_attempt
            else:
                print("Senha incorreta. Tente novamente.")
        elif value == "c":
            criar_usuario(user_accounts)
            password_attempt = input("Digite sua senha: ")
            if password_attempt == user_accounts[0]['senha']:
                return password_attempt
            else:
                print("Senha incorreta. Tente novamente.")
        elif value == "q":
            exit()
        else:
            print("Opção inválida. Por favor, selecione 'i' para SignIn ou 'c' para SignUp.")

authenticated = False
while not authenticated:
    password_attempt = authenticate()
    if password_attempt == user_accounts[0]['senha']:
        authenticated = True
    else:
        print("Senha incorreta. Tente novamente.")

    LIMITE_SAQUES = 3
    AGENCIA="0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    historico_saldo = []
    tipo = user_accounts[0]['tipo']
    contas = []

    while True:
        opcao = menu()

        if opcao == "t":
            # Transfer funds implementation
            valor = float(input("Informe o valor da transferência: "))
            conta_destino = input("Informe o número da conta de destino: ")
            saldo, extrato = transferencia(saldo, valor, extrato, conta_destino, user_accounts)
            pass
        elif opcao == "b":
            # Account information implementation
            print("\n========= Informações da Conta =========")
            print("Nome do titular: ", user_accounts[0]['nome'])
            print("Número da conta: ", user_accounts[0]['numero_conta'])
            print("Contato: ", user_accounts[0]['contato'])
            print("Tipo de conta: ", user_accounts[0]['tipo'])
            print("Saldo: R$ {:.2f}".format(saldo))
            print("========================================")
            pass
        elif opcao == "d":
            # Deposit implementation
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
            pass
        elif opcao == "s":
            # Withdraw implementation
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                numero_saques = numero_saques,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
            )
            pass
        elif opcao == "e":
            # Account statement implementation
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "h":
            # Exibe o histórico de Saldo
            print("\n=========== Histórico de Saldo ===========")
            for i, saldo_historico in enumerate(historico_saldo):
                print(f"Transação {i+1}: R$ {saldo_historico:.2f}")
            print("=========================================")
            pass
        elif opcao == "u":
            if tipo == "Admin":
                admin_password = authenticate()
                if admin_password == user_accounts[0]["senha"]:
                    print("\n========= Atualizar informações pessoais =========")
                    new_nome = input("Digite o novo nome: ")
                    if input("Deseja alterar o número da conta? (S/N): ").lower() == "s":
                        new_numero_conta = input("Digite o novo número da conta: ")
                        user_accounts[0]["numero_conta"] = new_numero_conta
                        numero_conta = new_numero_conta  # Update local variable
                    new_contato = input("Digite o novo contato: ")
                    user_accounts[0]["nome"] = new_nome
                    user_accounts[0]["contato"] = new_contato
                    nome = new_nome  # Update local variable
                    contato = new_contato  # Update local variable
                    print("Informações pessoais atualizadas com sucesso.")
                    print("=================================================")
                else:
                    print("Senha incorreta. Apenas o administrador pode atualizar as informações pessoais.")
            else:
                print("Apenas o administrador pode atualizar as informações pessoais.")
        elif opcao == "n":
            numero_conta = random.randint(1, 1000000)
            conta = criar_conta(AGENCIA, numero_conta, user_accounts)
            if conta:
                contas.append(conta)
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")
