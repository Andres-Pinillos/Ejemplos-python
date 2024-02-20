# Usando las mismas clases del ejemplo anterior

def hacer_sonido_animal(animal):
    return animal.hacer_sonido()

# Crear objetos de las subclases
perro = Perro("Bobby")
gato = Gato("Whiskers")

print(hacer_sonido_animal(perro))  # Output: Guau!
print(hacer_sonido_animal(gato))   # Output: Miau!
