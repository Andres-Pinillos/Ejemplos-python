class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # El atributo saldo está encapsulado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")

# Acceso al saldo encapsulado
cuenta = CuentaBancaria(1000)
cuenta.__saldo  # Esto generaría un error, ya que el atributo es privado
