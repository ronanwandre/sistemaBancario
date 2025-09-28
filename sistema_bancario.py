import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Usuario:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def executar_movimento(self, conta, movimento):
        movimento.registrar(conta)

    def incluir_conta(self, conta):
        self.contas.append(conta)


class Pessoa(Usuario):
    def __init__(self, nome, nascimento, documento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.nascimento = nascimento
        self.documento = documento


class ContaBancaria:
    def __init__(self, numero, usuario):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._usuario = usuario
        self._historico = Historico()

    @classmethod
    def criar_conta(cls, usuario, numero):
        return cls(numero, usuario)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def usuario(self):
        return self._usuario

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Operação não concluída! Saldo insuficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque efetuado com êxito! ===")
            return True

        else:
            print("\n@@@ Operação não concluída! Valor inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito efetuado com êxito! ===")
        else:
            print("\n@@@ Operação não concluída! Valor inválido. @@@")
            return False

        return True


class ContaComum(ContaBancaria):
    def __init__(self, numero, usuario, limite=500, max_saques=3):
        super().__init__(numero, usuario)
        self._limite = limite
        self._max_saques = max_saques

    def sacar(self, valor):
        total_saques = len(
            [mov for mov in self.historico.transacoes if mov["tipo"] == Saque.__name__]
        )

        passou_limite = valor > self._limite
        passou_saques = total_saques >= self._max_saques

        if passou_limite:
            print("\n@@@ Operação não concluída! Valor acima do limite permitido. @@@")

        elif passou_saques:
            print("\n@@@ Operação não concluída! Limite de saques atingido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            Conta:\t\t{self.numero}
            Titular:\t{self.usuario.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def registrar_movimento(self, movimento):
        self._transacoes.append(
            {
                "tipo": movimento.__class__.__name__,
                "valor": movimento.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Movimento(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Movimento):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        ok = conta.sacar(self.valor)

        if ok:
            conta.historico.registrar_movimento(self)


class Deposito(Movimento):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        ok = conta.depositar(self.valor)

        if ok:
            conta.historico.registrar_movimento(self)


def mostrar_menu():
    menu = """\n
    ============ OPÇÕES ============
    [d]\tDepósito
    [s]\tSaque
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def localizar_usuario(documento, usuarios):
    filtrados = [usr for usr in usuarios if usr.documento == documento]
    return filtrados[0] if filtrados else None


def obter_conta_usuario(usuario):
    if not usuario.contas:
        print("\n@@@ Usuário ainda não possui conta! @@@")
        return
    return usuario.contas[0]  # simplificação


def realizar_deposito(usuarios):
    doc = input("CPF do usuário: ")
    usuario = localizar_usuario(doc, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado! @@@")
        return

    valor = float(input("Valor do depósito: "))
    mov = Deposito(valor)

    conta = obter_conta_usuario(usuario)
    if not conta:
        return

    usuario.executar_movimento(conta, mov)


def realizar_saque(usuarios):
    doc = input("CPF do usuário: ")
    usuario = localizar_usuario(doc, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado! @@@")
        return

    valor = float(input("Valor do saque: "))
    mov = Saque(valor)

    conta = obter_conta_usuario(usuario)
    if not conta:
        return

    usuario.executar_movimento(conta, mov)


def exibir_extrato(usuarios):
    doc = input("CPF do usuário: ")
    usuario = localizar_usuario(doc, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado! @@@")
        return

    conta = obter_conta_usuario(usuario)
    if not conta:
        return

    print("\n============= EXTRATO =============")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Nenhuma movimentação realizada."
    else:
        for mov in transacoes:
            extrato += f"\n{mov['tipo']}:\n\tR$ {mov['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("===================================")


def criar_usuario(usuarios):
    doc = input("CPF (apenas números): ")
    usuario = localizar_usuario(doc, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Nome completo: ")
    nasc = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (rua, nº - bairro - cidade/UF): ")

    usuario = Pessoa(nome=nome, nascimento=nasc, documento=doc, endereco=endereco)

    usuarios.append(usuario)

    print("\n=== Usuário criado com sucesso! ===")


def criar_conta(numero_conta, usuarios, contas):
    doc = input("CPF do usuário: ")
    usuario = localizar_usuario(doc, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado, cancelando criação de conta! @@@")
        return

    conta = ContaComum.criar_conta(usuario=usuario, numero=numero_conta)
    contas.append(conta)
    usuario.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    usuarios = []
    contas = []

    while True:
        opcao = mostrar_menu()

        if opcao == "d":
            realizar_deposito(usuarios)

        elif opcao == "s":
            realizar_saque(usuarios)

        elif opcao == "e":
            exibir_extrato(usuarios)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Opção inválida, escolha novamente. @@@")


main()