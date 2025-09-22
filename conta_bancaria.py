from pessoa import Pessoa

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular  # objeto Pessoa
        self.__saldo = saldo      # atributo privado

    # Getter e setter para titular
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nova_pessoa):
        if isinstance(nova_pessoa, Pessoa):
            self.__titular = nova_pessoa

    # Getter e setter para saldo
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor

    # Métodos de operação
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
