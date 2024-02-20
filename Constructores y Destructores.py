class Ejemplo:
    def __init__(self):
        print("Se ha creado un objeto")

    def __del__(self):
        print("Se ha eliminado un objeto")

# Crear objetos de la clase Ejemplo
objeto1 = Ejemplo()
objeto2 = Ejemplo()

del objeto1
# Output: Se ha eliminado un objeto
