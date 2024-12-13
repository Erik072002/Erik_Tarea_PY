class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        """Inserta un elemento en el árbol binario."""
        nuevo_nodo = NodoArbol(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        """Inserción recursiva."""
        if nuevo_nodo.dato < nodo_actual.dato:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, nuevo_nodo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.derecho, nuevo_nodo)

    def recorrer_inorder(self):
        """Recorrido inorder (izquierdo, raíz, derecho)."""
        self._recorrer_inorder_recursivo(self.raiz)

    def _recorrer_inorder_recursivo(self, nodo_actual):
        """Recorrido inorder recursivo."""
        if nodo_actual is not None:
            self._recorrer_inorder_recursivo(nodo_actual.izquierdo)
            print(nodo_actual.dato, end=" -> ")
            self._recorrer_inorder_recursivo(nodo_actual.derecho)

    def buscar(self, dato):
        """Busca un elemento en el árbol binario."""
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, nodo_actual, dato):
        """Búsqueda recursiva."""
        if nodo_actual is None:
            return False  # No se encontró el elemento
        if nodo_actual.dato == dato:
            return True  # Se encontró el elemento
        elif dato < nodo_actual.dato:
            return self._buscar_recursivo(nodo_actual.izquierdo, dato)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, dato)