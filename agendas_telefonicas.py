
def consultar():
    global guia
    nombre = str(input("Ingrese el nombre del usuario: "))
    if nombre in guia:
        print(f'El numero de telefono de {nombre} es {guia[nombre]}')
    else :
        print("El usuario no existe")
    eleccion = (int(input("¿Desea realizar otra accion? \n1=Si \n2=no \nRespuesta: ")))
    re_eleccion(eleccion)

def añadir():
    global guia
    nombre_ad = str(input("Ingrese un nombre de usuario: "))
    if nombre_ad in guia:
        print(f'{nombre_ad} ya existe')

    else  :
        telefono = int(input("Ingrese el número de teléfono: "))
        guia[nombre_ad] = telefono
        print(f"Usuario {nombre_ad} añadido exitosamente")


    eleccion = (int(input("¿Desea realizar otra accion? \n1=Si \n2=no \nRespuesta: ")))
    re_eleccion(eleccion)



def modificar():
    nombre= str(input("Ingrese un nombre: "))
    if nombre in guia:
        telefono=(int(input("ingrese el nuevo numero de telefono: ")))
        guia[nombre] = telefono
    else:
        print(f'{nombre} no existe en la agenda')

    eleccion = (int(input("¿Desea realizar otra accion? \n1=Si \n2=no \nRespuesta: ")))
    re_eleccion(eleccion)

def borrar():
    nombre=  (str(input("Ingrese un nombre: ")))
    if nombre in guia:
        guia[nombre] = None
        print(guia.items())
    else:
        print(f'{nombre} no existe en la agenda')

    eleccion = (int(input("¿Desea realizar otra accion? \n1=Si \n2=no \nRespuesta: ")))
    re_eleccion(eleccion)


def repetir():
    global opcion
    opcion = int(input(f'Escoja que la opcion que desea elegir '
                       f'\n1= Consultar'
                       f'\n2= Añadir'
                       f'\n3= Modificar'
                       f'\n4= Borrar'
                       f'\n5= Salir'
                       f'\nRespuesta: '))
    if opcion == 1:
        consultar()
    elif opcion == 2:
        añadir()
    elif opcion ==3:
        modificar()
    elif opcion ==4:
        borrar()
    else:
        salir()

def re_eleccion(eleccion):
    if eleccion == 1:
        repetir()
    else:
        global opcion
        opcion = 5
        salir()

def salir():
    print("Gracias por usar nuestro sistema")


print("!!!Bienvenido a la guia telefonica¡¡¡")
opcion = int(input(f'Escoja que la opcion que desea elegir '
                       f'\n1= Consultar'
                       f'\n2= Añadir'
                       f'\n3= Modificar'
                       f'\n4= Borrar'
                       f'\n5= Salir'
                       f'\nRespuesta: '))

guia = {"Jose": 302944, "Mario": 829433, "Angel": 822433, "Luis": 934334}

while opcion != 5 :

    if opcion==1:
        consultar()
    elif opcion==2:
        añadir()
    elif opcion== 3:
        modificar()
    elif opcion==4:
        borrar()
    else:
        opcion=5
        salir()





