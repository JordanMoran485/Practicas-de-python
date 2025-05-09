class Persona:
    def __init__(self , nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print("Holaaaaaaa")

    def comer(self):
        print("Estoy comiendo")

persona1 = Persona("Jordan, Moran, 22")
persona2 = Persona("Jose, Flores, 23")

persona1.saludar()
persona2.comer()

print(persona1.saludar())
print(persona2.comer())