class ContaBancaria:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0

# Função para verificar se um CPF está cadastrado
def verificar_cadastro(cpf, clientes_cadastrados):
    for cliente in clientes_cadastrados:
        if cliente["cpf"] == cpf:
            return True
    return False

# Função para realizar um saque
def sacar(saldo):
    valor = float(input("Informe o valor do saque: "))
    if valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo

# Função para verificar o saldo
def verificar_saldo(saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")

# Função para realizar um depósito
def depositar(saldo):
    valor = float(input("Informe o valor do depósito: "))
    saldo += valor
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    return saldo

# Função para cadastrar um novo cliente
def cadastrar_cliente(clientes_cadastrados):
    nome = input("Digite o nome do novo cliente: ")
    cpf = input("Digite o CPF do novo cliente: ")
    clientes_cadastrados.append({"nome": nome, "cpf": cpf})
    print("Novo cliente cadastrado com sucesso!")

# Função para listar todas as contas bancárias cadastradas
def listar_contas(contas_bancarias):
    print("\n=== Contas Bancárias Cadastradas ===")
    for idx, conta in enumerate(contas_bancarias, start=1):
        print(f"Conta {idx}:")
        print(f"Agência: {conta.agencia}")
        print(f"Número da Conta: {conta.numero_conta}")
        print(f"Usuário: {conta.usuario['nome']}")
        print("-" * 30)

# Função principal - Menu do Banco
def menu_banco():
    clientes_cadastrados = []  # Lista de clientes cadastrados
    contas_bancarias = []  # Lista de contas bancárias

    while True:
        print("\n=== Menu Banco ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Verificar Saldo")
        print("4. Consultar CPF")
        print("5. Listar Contas")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo = depositar(saldo)
        elif opcao == "2":
            saldo = sacar(saldo)
        elif opcao == "3":
            verificar_saldo(saldo)
        elif opcao == "4":
            cpf = input("Digite o CPF para consulta: ")
            if verificar_cadastro(cpf, clientes_cadastrados):
                print("CPF cadastrado.")
            else:
                print("CPF não cadastrado. Por favor, cadastre-se.")
                nome = input("Digite o nome do cliente: ")
                novo_cliente = {"nome": nome, "cpf": cpf}
                clientes_cadastrados.append(novo_cliente)
                
                # Criação de uma nova conta bancária para o cliente
                agencia = input("Digite o número da agência: ")
                numero_conta = input("Digite o número da conta: ")
                nova_conta = ContaBancaria(agencia, numero_conta, novo_cliente)
                contas_bancarias.append(nova_conta)
                
                print("Cliente cadastrado e conta bancária criada com sucesso!")
        elif opcao == "5":
            listar_contas(contas_bancarias)
        elif opcao == "6":
            print("Obrigado por utilizar nossos serviços. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executar o menu do banco
menu_banco()
