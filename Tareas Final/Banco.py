class banco (object):

    def __init__(self, inicializar):
        self.__v = [None] * inicializar
        self.__frente = 0
        self.__atras = 0
        self.__Nitems = 0

    def vacio (self):
        self.__Nitems == 0

    def llena (self):
        self.__Nitems == self.__v

    def traverse (self):
        for j in range(self.__Nitems):
            print(self.__v[j])

    def enqueue (self, item):
        if self.llena():
            print("El banco esta lleno")
            return
        else:
            self.__v[self.__atras] = item
            self.__atras = (self.__atras + 1) % len(self.__v)
            self.__Nitems += 1

    def dequeue (self):
        if self.vacio():
            print("El listado del banco se encuentra vacio")
        item = self.__v[self.__frente]
        self.__v[self.__frente] = None
        self.__frente = (self.__frente + 1) % len(self.__v)
        return item

    def fila(self):
        while not self.vacio():
            tecla = input("Presione la n para pasar al siguiente cliente")
            if tecla == "n":
                cliente = self.dequeue()
                if cliente is not None:
                    print("El cliente que sigue es el:", cliente)
            else:
                print("Tecla incorrecta")
                return

