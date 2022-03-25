
# 1 - A classe e a chave da Orientação dos Objetos,
# 2 - Quando usamos o "from conta import Conta" = "Importe do arquivo conta a classe conta" nos retorna um
# um codigo "caminho", onde o objeto foi criado na memoria
# 3 - Nesse caso para criar uma conta, criamos uma class "conta = Conta(dados a ser guardado)"

class Conta: # e criada uma classe para encapsular o mudulos
    def __init__(self, numero, titular, saldo, limite): # __init__ e uma classe construtora, e usamos juntamente com o
        # self, que seria caminho onde os dados são armazenados na memoria
        print("Contruindo...{}".format(self)) # nos apresenta um feedback com o codigo da memoria
        self.__numero = numero # gera um objeto na memoria numero quando usamos o "conta = Conta(dados a ser guardado)"
        self.__titular = titular # e um codigo privado, para isso e usado o "__"
        self.__saldo = saldo # self "é" o caminho onde foi guardado o objeto"dados"
        self.__limite = limite


    # funções dentro das classes ou orientação de objetos são chamados de "Modulos"
    def extrato(self): # quando usamos o conta.extrato() = "busca conta e me mostra o extrato "
        print('{} possui um saldo de R${:.2f}'.format(self.__titular, self.__saldo))
        # interpolação de string tambem e possivel usar a rientação dos Objetos atravel do self.__"modulo" busca os
        # dados do "modulo"

    def depositar(self, valor): # quando usamos conta.depositar(valor) = em conta, busca o objeto __saldo e adiciona valor
        self.__saldo += valor

    def __pode_dacar(self, valor_a_sacar): # modulo de verificação de limite do saque
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor): # modulo de saque da conta
        if(self.__pode_dacar(valor)): # se "conta" tiver limite, pode sacar
            self.__saldo -= valor # # quando usamos conta.depositar(valor) = em conta, busca o objeto __saldo e retira valor
        else: # se conta não tiver limite, exiba a mensagem:
            print('O valor de R${:.2f} exedeu o limite da conta, o limite disponivel de Saque é R${:.2f}'.format(valor, (self.__saldo + self.__limite)))
            # interpolação de string que faz a soma do saldo e limite e exibe na tela o limite total da conta

    def transferir(self, valor, destino):  # conta.transferir(valor, conta desejada)
        self.sacar(valor) # realize o modulo sacar e retire o "valor" da conta
        destino.depositar(valor) # e deposite dessa "conta" o valor

    def get_saldo(self):# o "get_" e um padrão de devolve / retorna o modulo que foi aplicado
        return self.__saldo # retorna o conteudo do objeto privado "__saldo"

    def get_titular(self): # o "get_" e um padrão de devolve / retorna o modulo que foi aplicado
        return self.__titular # retorna o conteudo do objeto privado "__titular"

    @property # outra forma de criar um _get, sem a necessidade de colocar o _get antes do modulo
    def limite(self):
        return self.__limite # retorna o conteudo do objeto privado "__limite"

    @limite.setter # criando um set_limite sem a necessidade do set_
    def limite(self, limite): # busca conta.limite e muda e altera o limite
        self.__limite = limite

    @staticmethod # um objeto estatico, que nao muda. E aplicado em todas as contas criadas
    def __codigo_banco():
        return "001" # quando solicitado o modulo, retorna o "001"