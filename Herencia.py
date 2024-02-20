class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Crear objetos de las subclases
perro = Perro("Bobby")
gato = Gato("Whiskers")

print(perro.hacer_sonido())  # Output: Guau!
print(gato.hacer_sonido())   # Output: Miau!
