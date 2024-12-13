class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, valor): #EJERCICIO 16
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def eliminar(self, valor): #EJERCICIO 16
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return
        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
            if nodo_actual.siguiente.valor == valor:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return
            nodo_actual = nodo_actual.siguiente

        print(f"Valor {valor} no encontrado en la lista.")

    def buscar(self, valor): #EJERCICIO 16
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor == valor:
                return nodo_actual  # Devolvemos el nodo si lo encontramos
            nodo_actual = nodo_actual.siguiente
        return None

    def traverse(self): #EJERCICIO 16
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def invertir(self): #EJERCICIO 17
        anterior = None
        actual = self.cabeza

        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

    def eliminar_duplicados(self): #EJERCICIO 18
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        nodo_actual = self.cabeza
        while nodo_actual:
            nodo_comparar = nodo_actual
            while nodo_comparar.siguiente: #EJERCICIO 18
                if nodo_actual.valor == nodo_comparar.siguiente.valor:
                    nodo_comparar.siguiente = nodo_comparar.siguiente.siguiente
                else:
                    nodo_comparar = nodo_comparar.siguiente
            nodo_actual = nodo_actual.siguiente #EJERCICIO 18