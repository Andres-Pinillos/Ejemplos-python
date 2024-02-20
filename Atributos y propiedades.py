class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulado

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

# Crear un objeto de la clase Persona
persona = Persona("Juan")
print(persona.nombre)  # Output: Juan

persona.nombre = "Pedro"
print(persona.nombre)  # Output: Pedro
