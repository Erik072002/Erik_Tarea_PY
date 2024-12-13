class ordenar(object):

    def __init__(self, inicializar):
        self.__v = [None] * inicializar
        self.__Nitems = 0
        self.__final = 0
        self.__enfrente = 0

    def vacia(self):
        return self.__Nitems == 0

    def llena(self):
        return self.__Nitems == len(self.__v)

    def traverse(self):
        if self.vacia():
            print("La cola está vacía.")
            return
        index = self.__enfrente
        count = 0
        while count < self.__Nitems:
            print(self.__v[index], end=" ")
            index = (index + 1) % len(self.__v)
            count += 1
        print()

    def dequeue(self):
        if self.vacia():
            print("La cola está vacía.")
            return None
        item = self.__v[self.__enfrente]
        self.__v[self.__enfrente] = None
        self.__enfrente = (self.__enfrente + 1) % len(self.__v)
        self.__Nitems -= 1
        return item

    def enqueue(self, item):
        if self.llena():
            print("La cola está llena.")
            return None
        else:
            self.__v[self.__final] = item
            self.__final = (self.__final + 1) % len(self.__v)
            self.__Nitems += 1

    def ordenar_cola(self):
        if self.vacia():
            print("No hay elementos para ordenar.")
            return
        for i in range(self.__Nitems):
            temp_list = []
            for _ in range(self.__Nitems):
                temp_list.append(self.dequeue())
            temp_list.sort()
            for item in temp_list:
                self.enqueue(item)