from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola
from datetime import datetime

pila = MiPila(10)
cola = MiCola(10)


# ---------------- FUNCIONES DE APOYO ----------------

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ingresar un número entero.")


def leer_pasajero():
    print("\n--- REGISTRAR PASAJERO ---")

    while True:
        numero = leer_entero("  N.º de pasajero: ")

        if numero > 0:
            break

        print("  El número debe ser mayor que cero.")

    nombre = input("  Nombre: ").strip()

    while nombre == "":
        print("  El nombre no puede estar vacío.")
        nombre = input("  Nombre: ").strip()

    while True:
        cedula = input("  Cédula: ").strip()

        if cedula.isdigit() and len(cedula) == 10:
            break

        print("  La cédula debe tener 10 dígitos.")

    while True:
        edad = leer_entero("  Edad: ")

        if edad > 0:
            break

        print("  La edad debe ser mayor que cero.")

    while True:
        fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()

        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            break
        except ValueError:
            print("  Fecha incorrecta.")

    destino = input("  Destino: ").strip()

    while destino == "":
        print("  El destino no puede estar vacío.")
        destino = input("  Destino: ").strip()

    asiento = input("  Asiento: ").strip().upper()

    while asiento == "":
        print("  El asiento no puede estar vacío.")
        asiento = input("  Asiento: ").strip().upper()

    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito", "12A"),
        Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C"),
        Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto", "0934567890", 16, "2026-11-20", "Quito", "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima", "01A")
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# ---------------- MENÚ 1: PILA ----------------

def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 - PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")

        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()

            if pila.apilar(pasajero):
                print("  Pasajero apilado correctamente.")

        elif op == "2":
            pila.listar()

        elif op == "3":
            pasajero = pila.desapilar()

            if pasajero is None:
                print("  La pila está vacía.")
            else:
                print("  Pasajero retirado:", pasajero)

        elif op == "4":
            pasajero = pila.ver_tope()

            if pasajero is None:
                print("  La pila está vacía.")
            else:
                print("  Tope:", pasajero)

        elif op == "5":
            numero = leer_entero("  Número del pasajero: ")
            posicion = pila.buscar(numero)

            if posicion == -1:
                print("  Pasajero no encontrado.")
            else:
                print("  Encontrado en la posición:", posicion)
                print(" ", pila.datos[posicion])

        elif op == "6":
            numero = leer_entero("  Número del pasajero: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()

            if destino == "" or asiento == "":
                print("  Los datos no pueden estar vacíos.")
            elif pila.modificar(numero, destino, asiento):
                print("  Pasajero modificado correctamente.")
            else:
                print("  Pasajero no encontrado.")

        elif op == "7":
            numero = leer_entero("  Número del pasajero: ")

            if pila.eliminar_por_numero(numero):
                print("  Pasajero eliminado correctamente.")
            else:
                print("  Pasajero no encontrado.")

        elif op == "8":
            copia = pila.copiar()
            print("  Copia de la pila:")
            copia.listar()

        elif op == "9":
            print("  Longitud:", pila.longitud())

            if pila.esta_vacia():
                print("  La pila está vacía.")
            else:
                print("  La pila tiene pasajeros.")

        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)

            print("  Datos de prueba cargados.")

        elif op == "0":
            break

        else:
            print("  Opción no válida.")


# ---------------- MENÚ 2: COLA ----------------

def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 - COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")

        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()

            if cola.encolar(pasajero):
                print("  Pasajero encolado correctamente.")

        elif op == "2":
            cola.listar()

        elif op == "3":
            pasajero = cola.desencolar()

            if pasajero is None:
                print("  La cola está vacía.")
            else:
                print("  Pasajero retirado:", pasajero)

        elif op == "4":
            pasajero = cola.ver_frente()

            if pasajero is None:
                print("  La cola está vacía.")
            else:
                print("  Frente:", pasajero)

        elif op == "5":
            numero = leer_entero("  Número del pasajero: ")
            posicion = cola.buscar(numero)

            if posicion == -1:
                print("  Pasajero no encontrado.")
            else:
                print("  Encontrado en la posición:", posicion)
                print(" ", cola.datos[posicion])

        elif op == "6":
            numero = leer_entero("  Número del pasajero: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()

            if destino == "" or asiento == "":
                print("  Los datos no pueden estar vacíos.")
            elif cola.modificar(numero, destino, asiento):
                print("  Pasajero modificado correctamente.")
            else:
                print("  Pasajero no encontrado.")

        elif op == "7":
            numero = leer_entero("  Número del pasajero: ")

            if cola.eliminar_por_numero(numero):
                print("  Pasajero eliminado correctamente.")
            else:
                print("  Pasajero no encontrado.")

        elif op == "8":
            copia = cola.copiar()
            print("  Copia de la cola:")
            copia.listar()

        elif op == "9":
            print("  Longitud:", cola.longitud())

            if cola.esta_vacia():
                print("  La cola está vacía.")
            else:
                print("  La cola tiene pasajeros.")

        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)

            print("  Datos de prueba cargados.")

        elif op == "0":
            break

        else:
            print("  Opción no válida.")


# ---------------- MENÚ PRINCIPAL ----------------

def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS - PASAJEROS =====")
        print("1. Menú 1 - Pila")
        print("2. Menú 2 - Cola")
        print("3. Salir")

        op = input("Opción: ").strip()

        if op == "1":
            menu_pila()

        elif op == "2":
            menu_cola()

        elif op == "3":
            print("¡Hasta pronto!")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
