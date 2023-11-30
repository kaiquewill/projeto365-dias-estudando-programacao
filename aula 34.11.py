from datetime import datetime
from random import randint

class ContaCorrente():
    """
    Cria um objeto contacorrente para gerenciar a conta do cliente

    atributos:
        nome:nome do cliente
        cpf:(str) CPF do cliente. deve ser adicionado com pontos e tracos 
        saldo; Qual é o saldo do cliente
        limite:limite do cheque especial do cliente
        agencia: agencia responsavel pela conta do cliente
        trnasacoes: hidtorico de transacoes do cliente

    """



    @staticmethod
    def _data_hora():
        horario_BR = datetime.now()
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
        pass

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []


    def consultar_saldo(self):
        print("Seu saldo atual é de R${:,.2f}".format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite


    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('eu saldo nao é suficiente para completar a transacao ')
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print('seu cheque especial e de {:,.2f}'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('historico de transacoes')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:


    @staticmethod
    def _data_hora():
        horario_BR = datetime.now()
        return horario_BR
        pass

    def __init__(self, titular , conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        #self.cod_seguranca = '{}{}{}'. format(randint(0, 9). randint(0,9), randint(0, 9))
        self.limite = 1000
        self._senha= '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha invalida")



# programa
conta_lira = ContaCorrente("lira", "453.222.333.22", '101', '234234')

cartao_lira = CartaoCredito('Lira', conta_lira)

conta_lira._senha = 4423
print(cartao_lira._senha)


print(conta_lira.__dict__)

#34.25