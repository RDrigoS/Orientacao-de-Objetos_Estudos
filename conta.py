

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('{} possui um saldo de R${:.2f}'.format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_dacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if(self.__pode_dacar(valor)):
            self.__saldo -= valor
        else:
            print('O valor de R${:.2f} exedeu o limite da conta, o limite disponivel de Saque é R${:.2f}'.format(valor, (self.__saldo + self.__limite)))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def __codigo_banco():
        return "001"