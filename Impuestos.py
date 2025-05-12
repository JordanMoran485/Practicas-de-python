class Persona:
    def __init__(self):
        self.nombre=input("ingresa tu nombre: ")
        self.edad = input("ingresa tu edad: ")

    def imprimir(self):
        print(f'tu nombre es {ciudadano.nombre} y tu edad es {ciudadano.edad}y su deposito es de {ciudadano.deposito} ')

class Ciudadano(Persona):

    deposito = float(input("ingresa tu deposito: "))
    def impuesto(self, deposito):
        if deposito>4000:
            print("Debe pagar impuesto")
        else:
            print("No debe pagar impuesto")



ciudadano = Ciudadano()
ciudadano.imprimir()
ciudadano.impuesto(ciudadano.deposito)


