class Stack(object):
    def __init__(self, max):
        # La pila se almacena como una lista
        self.__stackList = [None] * max  # Sin elementos inicialmente
        self.__top = -1  # Puntero a la parte superior de la pila

    def push(self, item):
        # Insertar elemento en la parte superior de la pila
        if not self.isFull():  # Comprobar si la pila no está llena
            self.__top += 1  # Avanzar el puntero
            self.__stackList[self.__top] = item  # Almacenar el elemento
        else:
            raise Exception("La pila está llena")  # Lanzar un error si la pila está llena

    def pop(self):
        # Eliminar y devolver el elemento superior de la pila
        if not self.isEmpty():  # Comprobar si la pila no está vacía
            top = self.__stackList[self.__top]  # Elemento superior
            self.__stackList[self.__top] = None  # Eliminar la referencia al elemento
            self.__top -= 1  # Disminuir el puntero
            return top  # Devolver el elemento superior
        else:
            raise Exception("La pila está vacía")  # Lanzar un error si la pila está vacía

    def peek(self):
        # Devolver el elemento superior sin eliminarlo
        if not self.isEmpty():  # Si la pila no está vacía
            return self.__stackList[self.__top]  # Devolver el elemento superior
        else:
            raise Exception("La pila está vacía")  # Lanzar un error si la pila está vacía

    def isEmpty(self):
        # Comprobar si la pila está vacía
        return self.__top < 0

    def isFull(self):
        # Comprobar si la pila está llena
        return self.__top >= len(self.__stackList) - 1

    def __len__(self):
        # Devolver el número de elementos en la pila
        return self.__top + 1

    def __str__(self):
        # Convertir la pila a una cadena
        ans = "["  # Comenzar con un corchete izquierdo
        for i in range(self.__top + 1):  # Recorrer los elementos actuales
            if len(ans) > 1:  # Excepto el siguiente al corchete izquierdo,
                ans += ", "  # separar los elementos con una coma
            ans += str(self.__stackList[i])  # Agregar el elemento a la cadena
        ans += "]"  # Terminar con un corchete derecho
        return ans
