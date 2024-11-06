def identity(x): return x


class PriorityQueue:
    def __init__(self, size, pri=identity):  # Constructor
        self.__maxSize = size  # Tamaño máximo de la cola
        self.__que = [None] * size  # Lista de almacenamiento
        self.__pri = pri  # Función de prioridad
        self.__nItems = 0  # Contador de elementos

    def insert(self, item):
        # Insertar el elemento en la parte trasera de la lista (inserción rápida)
        if self.isFull():
            raise Exception("Queue overflow")  # Excepción si la cola está llena
        self.__que[self.__nItems] = item  # Almacenar el nuevo elemento
        self.__nItems += 1  # Aumentar el contador de elementos
        return True

    def remove(self):
        # Remover el elemento de mayor prioridad
        if self.isEmpty():
            raise Exception("Queue underflow")  # Excepción si la cola está vacía

        # Encontrar el índice del elemento con mayor prioridad
        highest_priority_index = 0
        for i in range(1, self.__nItems):
            if self.__pri(self.__que[i]) > self.__pri(self.__que[highest_priority_index]):
                highest_priority_index = i

        # Guardar el elemento de mayor prioridad
        highest_priority_item = self.__que[highest_priority_index]

        # Mover el último elemento a la posición del elemento eliminado y ajustar el contador
        self.__que[highest_priority_index] = self.__que[self.__nItems - 1]
        self.__que[self.__nItems - 1] = None
        self.__nItems -= 1
        return highest_priority_item

    def peek(self):
        # Retorna el elemento de mayor prioridad sin eliminarlo
        if self.isEmpty():
            return None

        # Encontrar el elemento de mayor prioridad
        highest_priority_index = 0
        for i in range(1, self.__nItems):
            if self.__pri(self.__que[i]) > self.__pri(self.__que[highest_priority_index]):
                highest_priority_index = i

        return self.__que[highest_priority_index]

    def isEmpty(self):
        return self.__nItems == 0

    def isFull(self):
        return self.__nItems == self.__maxSize

    def __len__(self):
        return self.__nItems

    def __str__(self):
        # Representación en cadena de la cola de prioridad
        ans = "["
        for i in range(self.__nItems):
            if i > 0:
                ans += ", "
            ans += str(self.__que[i])
        ans += "]"
        return ans