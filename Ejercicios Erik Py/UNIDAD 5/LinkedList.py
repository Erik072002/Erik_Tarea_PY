# Implementación de la lista enlazada simple y el deque basado en un arreglo

def identity(x): return x  # Función identidad

class Link(object):  # Nodo para una lista enlazada
    def __init__(self, datum, next=None):
        self.__data = datum
        self.__next = next

    def getData(self):
        return self.__data

    def setData(self, datum):
        self.__data = datum

    def getNext(self):
        return self.__next

    def setNext(self, link):
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception("El siguiente nodo debe ser un objeto Link o None")

    def isLast(self):
        return self.getNext() is None

    def __str__(self):
        return str(self.getData())

class LinkedList(object):  # EJERCICIO 5.4 Y 5.5
    def __init__(self):
        self.__first = None

    def getFirst(self):
        return self.__first

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
        else:
            raise Exception("El primer nodo debe ser un objeto Link o None")

    def isEmpty(self):
        return self.getFirst() is None

    def first(self):
        if self.isEmpty():
            raise Exception("No hay elementos en la lista")
        return self.getFirst().getData()

    def traverse(self, func=print):
        enlace = self.getFirst()
        while enlace is not None:
            yield enlace.getData()
            enlace = enlace.getNext()

    def __len__(self):
        return sum(1 for _ in self.traverse())

    def __str__(self):
        elementos = (str(dato) for dato in self.traverse())
        return "[" + " > ".join(elementos) + "]"

    def insert(self, datum):
        link = Link(datum, self.getFirst())
        self.setFirst(link)

    def find(self, goal, key=identity):
        link = self.getFirst()
        while link is not None:
            if key(link.getData()) == goal:
                return link
            link = link.getNext()

    def search(self, goal, key=identity):
        link = self.find(goal, key)
        if link is not None:
            return link.getData()

    def insertAfter(self, goal, newDatum, key=identity):
        link = self.find(goal, key)
        if link is None:
            return False
        newLink = Link(newDatum, link.getNext())
        link.setNext(newLink)
        return True

    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("No se puede eliminar de una lista vacía")
        first = self.getFirst()
        self.setFirst(first.getNext())
        return first.getData()

    def delete(self, goal, key=identity):
        if self.isEmpty():
            raise Exception("No se puede eliminar de una lista vacía")
        previous = self
        while previous.getFirst() is not None:
            link = previous.getFirst()
            if key(link.getData()) == goal:
                previous.setFirst(link.getNext())
                return link.getData()
            previous = link
        raise Exception("Elemento no encontrado")

class Deque:  # EJERCICIO 5.4 Y 5.5
    def __init__(self, max):
        self.__stackList = [None] * max
        self.__top = -1
        self.__max = max

    def insertLeft(self, item):
        if not self.isFull():
            self.__stackList[1:self.__top + 2] = self.__stackList[0:self.__top + 1]
            self.__stackList[0] = item
            self.__top += 1
        else:
            raise Exception("El deque está lleno")

    def insertRight(self, item):
        if not self.isFull():
            self.__top += 1
            self.__stackList[self.__top] = item
        else:
            raise Exception("El deque está lleno")

    def removeLeft(self):
        if not self.isEmpty():
            first = self.__stackList[0]
            self.__stackList[0:self.__top] = self.__stackList[1:self.__top + 1]
            self.__stackList[self.__top] = None
            self.__top -= 1
            return first
        else:
            raise Exception("El deque está vacío")

    def removeRight(self):
        if not self.isEmpty():
            last = self.__stackList[self.__top]
            self.__stackList[self.__top] = None
            self.__top -= 1
            return last
        else:
            raise Exception("El deque está vacío")

    def peekLeft(self):
        if not self.isEmpty():
            return self.__stackList[0]
        else:
            raise Exception("El deque está vacío")

    def peekRight(self):
        if not self.isEmpty():
            return self.__stackList[self.__top]
        else:
            raise Exception("El deque está vacío")

    def isEmpty(self):
        return self.__top < 0

    def isFull(self):
        return self.__top >= self.__max - 1
