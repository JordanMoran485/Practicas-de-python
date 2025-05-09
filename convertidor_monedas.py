
print("!!!Bienvenido al convertidor de monedas¡¡¡¡")

def convertidor(moneda_convertida, nombre_moneda_actual):

    def toDolar(nombre_moneda_actual):
        if nombre_moneda_actual == 1:
            '''Pesos colomnbianos'''
            equivalente = 3750
            valor_moneda = float(input(f'Ingrese el valor en dolares a convertir '))
            total = valor_moneda * equivalente
            print(f'{valor_moneda} dolares a pesos son {total} pesos colombianos')
        elif nombre_moneda_actual == 2:
            '''Yaunes'''
            equivalente = 6.37
            valor_moneda = float(input(f'Ingrese el valor en dolares a convertir '))
            total = valor_moneda * equivalente
            print(f'{valor_moneda} dolares a yuanes son {total} yuanes')
        else :
            '''Libras esterlinas'''
            equivalente = 0.76
            valor_moneda = float(input(f'Ingrese el valor en dolares a convertir '))
            total = valor_moneda * equivalente
            print(f'{valor_moneda} dolares a libras son {total} libras esterlinas')

    def toEuro(nombre_moneda_actual):
        if nombre_moneda_actual == 1:
            '''Pesos colomnbianos'''
            equivalente  = 4000
            valor_moneda = float(input(f'Ingrese el valor en euros a convertir '))
            total = valor_moneda * equivalente
            print(f'{valor_moneda} dolares a pesos son {total} pesos colombianos')
        elif nombre_moneda_actual == 2:
            '''Yuanes'''
            equivalente = 6.93
            valor_moneda = float(input(f'Ingrese el valor en euros a convertir '))
            total = valor_moneda * equivalente
            print(f'{valor_moneda} dolares a yuanes son {total} yuanes')
        else:
            '''Libras esterlinas'''
            equivalente = 0.83
            valor_moneda = float(input(f'Ingrese el valor en euros a convertir '))
            total = valor_moneda * equivalente
            print(f'{valor_moneda} dolares a libras son {total} libras esterlinas')

    if moneda_convertida == 1:
        toDolar(nombre_moneda_actual)
    elif moneda_convertida == 2 :
        toEuro(nombre_moneda_actual)
    else:
        print("error")

print("Elija su moneda actual")
nombre_moneda_actual= int(input(f' 1= pesos colombianos\n 2= yuanes\n 3= libras esterlinas\n Respuesta: '))
print("Elija el tipo de moneda al cual quiere convertirlo ")
moneda_convertida = int(input(f' 1= dolar\n 2= euro\n Respuesta: '))

convertidor(moneda_convertida, nombre_moneda_actual)
