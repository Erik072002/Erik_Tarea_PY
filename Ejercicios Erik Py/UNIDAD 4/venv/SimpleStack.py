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

class Deque: #EJERCICIO 4.3
    def __init__(self, max):
        # La pila se almacena como una lista de tamaño fijo
        self.__stackList = [None] * max  # Inicialmente vacío
        self.__top = -1  # Puntero a la parte superior de la pila
        self.__max = max  # Tamaño máximo del deque

    def insertLeft(self, item):
        # Insertar elemento en la parte izquierda (inicio)
        if not self.isFull():  # Comprobar si la pila no está llena
            self.__stackList[1:self.__top + 2] = self.__stackList[0:self.__top + 1]  # Desplaza elementos a la derecha
            self.__stackList[0] = item  # Inserta el nuevo elemento al inicio
            self.__top += 1  # Incrementa el puntero
        else:
            raise Exception("La pila está llena")  # Lanza una excepción si la pila está llena

    def insertRight(self, item):
        # Insertar elemento en la parte derecha (final)
        if not self.isFull():  # Comprobar si la pila no está llena
            self.__top += 1  # Avanzar el puntero
            self.__stackList[self.__top] = item  # Almacenar el elemento al final
        else:
            raise Exception("La pila está llena")  # Lanza una excepción si la pila está llena

    def removeLeft(self):
        # Eliminar y devolver el primer elemento de la pila
        if not self.isEmpty():  # Comprobar si la pila no está vacía
            first = self.__stackList[0]  # Obtener el primer elemento
            self.__stackList[0:self.__top] = self.__stackList[1:self.__top + 1]  # Desplazar elementos a la izquierda
            self.__stackList[self.__top] = None  # Limpiar la posición final
            self.__top -= 1  # Disminuir el puntero
            return first  # Devolver el primer elemento
        else:
            raise Exception("La pila está vacía")  # Lanza una excepción si la pila está vacía

    def removeRight(self):
        # Eliminar y devolver el último elemento de la pila
        if not self.isEmpty():  # Comprobar si la pila no está vacía
            last = self.__stackList[self.__top]  # Obtener el último elemento
            self.__stackList[self.__top] = None  # Eliminar la referencia al elemento
            self.__top -= 1  # Disminuir el puntero
            return last  # Devolver el último elemento
        else:
            raise Exception("La pila está vacía")  # Lanza una excepción si la pila está vacía

    def peekLeft(self):
        # Devolver el primer elemento sin eliminarlo
        if not self.isEmpty():  # Comprobar si la pila no está vacía
            return self.__stackList[0]  # Devolver el primer elemento
        else:
            raise Exception("La pila está vacía")  # Lanza una excepción si la pila está vacía

    def peekRight(self):
        # Devolver el último elemento sin eliminarlo
        if not self.isEmpty():  # Comprobar si la pila no está vacía
            return self.__stackList[self.__top]  # Devolver el último elemento
        else:
            raise Exception("La pila está vacía")  # Lanza una excepción si la pila está vacía

    def isEmpty(self):
        # Comprobar si la pila está vacía
        return self.__top < 0

    def isFull(self):
        # Comprobar si la pila está llena
        return self.__top >= self.__max - 1

