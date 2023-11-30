from random import randint

class Agencia:
    def __init__(self, telefone, cnpj, numero):
        self.telefone= telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nivel recomendado. Caixa atual :{}'.format(self.caixa))
        else:
            print('caixa esta ok. valor atual do caixa é de {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf,juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf , juros))
        else:
            print('nao podemos emprestar no momento')

    def adicionar_cliente(self, nome, cpf,patrimonio):
        self.clientes.append((nome, cpf, patrimonio))




class AgenciaVirtual(Agencia):
    def __init__(self, site ,telefone,cnpj):
        self.site= site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal= 0

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

    def depositar_paypal(self,valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor



class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001 , 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001 , 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio >1000000:
            super().adicionar_cliente(nome, cpf,patrimonio)

        else:
            print('nao tem dineiro suficiente para o premium')


agencia1= Agencia(222244444,333444444444, 4567)

agencia_virtual = AgenciaVirtual('www.kaique.com', 8994321946, 344555666777)
agencia_virtual.verificar_caixa()
print(agencia_virtual.site)

agencia_comum = AgenciaComum(2334444444, 3333234343)

agencia_premium= AgenciaPremium(122343443, 343553553)

agencia_virtual.depositar_paypal(20000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

agencia_premium.adicionar_cliente('lira', 54665535353, 10000000888)
print(agencia_premium.clientes)