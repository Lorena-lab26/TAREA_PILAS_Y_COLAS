from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo."""

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  La pila está llena")
            return False

        if self.buscar(pasajero.numero) != -1:
            print("  Ya existe un pasajero con ese número")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (pila vacía)")
            return

        for i in range(self.cantidad - 1, -1, -1):
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]} <- TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]} <- FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    def desapilar(self):
        if self.cantidad == 0:
            return None

        pasajero = self.datos[self.cantidad - 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1

        return pasajero

    def ver_tope(self):
        if self.cantidad == 0:
            return None

        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i

        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)

        if posicion == -1:
            return False

        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento

        return True

    def eliminar_por_numero(self, numero):
        if self.cantidad == 0:
            return False

        auxiliar = MiPila(self.capacidad)
        encontrado = False

        while self.cantidad > 0:
            pasajero = self.desapilar()

            if pasajero.numero == numero:
                encontrado = True
            else:
                auxiliar.apilar(pasajero)

        while auxiliar.cantidad > 0:
            pasajero = auxiliar.desapilar()
            self.apilar(pasajero)

        return encontrado

    def copiar(self):
        nueva_pila = MiPila(self.capacidad)

        for i in range(self.cantidad):
            nueva_pila.apilar(self.datos[i])

        return nueva_pila

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
