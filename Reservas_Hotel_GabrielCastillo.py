import random

habitaciones = {
    "SI123": {
        "codigo": "SI123",
        "numero": 101,
        "tipo": "Simple",
        "estado": "Disponible"
    },
    "DO456": {
        "codigo": "DO456",
        "numero": 202,
        "tipo": "Doble",
        "estado": "Ocupada"
    }
}

TIPOS_VALIDOS = ["Simple", "Doble", "Suite"]


def generar_codigo(tipo):
    letras = tipo[:2].upper()
    numero = random.randint(100, 999)
    return letras + str(numero)


def registrar_habitacion():
    try:
        numero = int(input("Ingrese numero de habitacion: "))

        print("Tipos disponibles: Simple, Doble, Suite")
        tipo = input("Ingrese tipo de habitacion: ").capitalize()

        if tipo not in TIPOS_VALIDOS:
            print("Tipo de habitacion no valido")
            return

        codigo = generar_codigo(tipo)

        while codigo in habitaciones:
            codigo = generar_codigo(tipo)

        habitaciones[codigo] = {
            "codigo": codigo,
            "numero": numero,
            "tipo": tipo,
            "estado": "Disponible"
        }

        print("\nHabitacion registrada correctamente")
        print("Codigo generado:", codigo)

    except:
        print("Error al ingresar los datos")


def mostrar_habitaciones():
    if len(habitaciones) == 0:
        print("No existen habitaciones registradas")
        return

    print("\n===== LISTA DE HABITACIONES =====")

    for codigo in habitaciones:
        print("Codigo :", habitaciones[codigo]["codigo"])
        print("Numero :", habitaciones[codigo]["numero"])
        print("Tipo   :", habitaciones[codigo]["tipo"])
        print("Estado :", habitaciones[codigo]["estado"])
        print("-" * 40)


def buscar_habitacion():
    codigo = input("Ingrese codigo de habitacion a buscar: ").upper()

    if codigo in habitaciones:
        print("\nHabitacion encontrada")
        print("Codigo :", habitaciones[codigo]["codigo"])
        print("Numero :", habitaciones[codigo]["numero"])
        print("Tipo   :", habitaciones[codigo]["tipo"])
        print("Estado :", habitaciones[codigo]["estado"])
    else:
        print("Habitacion no encontrada")


def reservar_habitacion():
    codigo = input("Ingrese codigo de habitacion a reservar: ").upper()

    if codigo in habitaciones:
        if habitaciones[codigo]["estado"] == "Ocupada":
            print("La habitacion ya se encuentra ocupada")
        else:
            habitaciones[codigo]["estado"] = "Ocupada"
            print("Habitacion reservada correctamente")
    else:
        print("Habitacion no existe")


def liberar_habitacion():
    codigo = input("Ingrese codigo de habitacion a liberar: ").upper()

    if codigo in habitaciones:
        if habitaciones[codigo]["estado"] == "Disponible":
            print("La habitacion ya se encuentra disponible")
        else:
            habitaciones[codigo]["estado"] = "Disponible"
            print("Habitacion liberada correctamente")
    else:
        print("Habitacion no existe")


def modificar_habitacion():
    codigo = input("Ingrese codigo de habitacion a modificar: ").upper()

    if codigo in habitaciones:
        try:
            nuevo_numero = int(input("Nuevo numero de habitacion: "))

            print("Tipos disponibles: Simple, Doble, Suite")
            nuevo_tipo = input("Nuevo tipo de habitacion: ").capitalize()

            if nuevo_tipo not in TIPOS_VALIDOS:
                print("Tipo de habitacion no valido")
                return

            habitaciones[codigo]["numero"] = nuevo_numero
            habitaciones[codigo]["tipo"] = nuevo_tipo

            print("Habitacion modificada correctamente")

        except:
            print("Error en los datos ingresados")
    else:
        print("Habitacion no existe")


def eliminar_habitacion():
    codigo = input("Ingrese codigo de habitacion a eliminar: ").upper()

    if codigo in habitaciones:
        del habitaciones[codigo]
        print("Habitacion eliminada correctamente")
    else:
        print("Habitacion no existe")


def menu():
    opcion = 0

    while opcion != 8:

        print("\n===== SISTEMA DE RESERVAS DE HOTEL =====")
        print("1. Registrar habitacion")
        print("2. Mostrar habitaciones")
        print("3. Buscar habitacion")
        print("4. Reservar habitacion")
        print("5. Liberar habitacion")
        print("6. Modificar habitacion")
        print("7. Eliminar habitacion")
        print("8. Salir")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                registrar_habitacion()

            elif opcion == 2:
                mostrar_habitaciones()

            elif opcion == 3:
                buscar_habitacion()

            elif opcion == 4:
                reservar_habitacion()

            elif opcion == 5:
                liberar_habitacion()

            elif opcion == 6:
                modificar_habitacion()

            elif opcion == 7:
                eliminar_habitacion()

            elif opcion == 8:
                print("Saliendo del sistema")

            else:
                print("Opcion invalida")

        except:
            print("Debe ingresar un numero")

menu()
