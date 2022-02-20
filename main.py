import pickle
import os
from os import remove

print("AGENDA TELEFONICA")
contactos = []

if os.path.exists('datos.pickle'):
    archivo = open('datos.pickle', 'rb')
    while True:
        try:
            contactos.append(pickle.load(archivo))
        except EOFError:
            break

    archivo.close()

while True:
    print("\nEscoge una opcion:")
    print("1) Agregar contacto")
    print("2) Mostrar contactos")
    print("3) Buscar contacto")
    print("4) Borrar todo")
    print("5) Salir")
    opcion = input("> ")

    if opcion == "1":
        contacto = dict()
        nombre = input("Introduce el nombre del contacto: ")
        while True:
            telefono = (input("Introduce su telefono: "))
            try:
                n = int(telefono)
                break 
            except ValueError:
                print("Solo debe contener numeros.\n")

        while True:
            correo = input("Introduce su correo: ")
            if '@' in correo and correo.rfind('@') != 0:
                break
            else:
                print("Correo no valido.\n")

        contacto['Nombre'] = nombre
        contacto['Telefono'] = telefono
        contacto['Correo'] = correo
        contactos.append(contacto)

        archivo = open('datos.pickle', 'ab')
        pickle.dump(contacto, archivo)
        archivo.close()

    elif opcion == "2":
        if len(contactos) == 0:
            print("No hay contactos.")
        else:
            for contacto in contactos:
                print('\n'.join("{}: {}".format(k, v) for k, v in contacto.items()) + '\n')
        
    elif opcion == "3":
        busqueda = input("Introduce el nombre del contacto: ")
        encontrado = False
        for contacto in contactos:
            if contacto['Nombre'] == busqueda:
                encontrado = True
                print('\n'.join("{}: {}".format(k, v) for k, v in contacto.items()))
                break
        
        if encontrado == False:
            print("No se encuentra este contacto.")

    elif opcion == "4":
        if len(contactos) != 0:
            contactos.clear()
            remove("datos.pickle")
            print("Contactos eliminados con exito.")
        else:
            print("No hay contactos.")

    elif opcion == "5":
        print("Hasta luego.\n")
        break

    else:
        print("Opcion no valida.")