class cola (object):

    def __init__(self, inicializar):
        self.__v= [None] * inicializar
        self.__Nitems = 0
        self.__enfrente = 0
        self.__final = 0

    def vacia (self):
        self.__Nitems == 0

    def llena (self):
        self.__Nitems == self.__v

    def enqueue (self, item):
        if self.llena():
            print("La cola esta llena")
            return None
        else:
            self.__v[self.__final]= item
            self.__final = (self.__final + 1) % len(self.__v)
            self.__Nitems +=1

    def dequeue (self):
        if self.vacia():
            print("La cola esta vacia")
            return None
        item = self.__v[self.__enfrente]
        self.__v[self.__enfrente]= None
        self.__enfrente = (self.__enfrente + 1) % len(self.__v)
        return item
    def peek (self):
        print(self.__v[self.__enfrente])




    def traverse(self):
        for j in range(self.__Nitems):
            print(self.__v[j])
