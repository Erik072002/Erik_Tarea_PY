class historial (object):

    def __init__(self, inicializar):
        self.__v = [None] * inicializar
        self.__Nitems = 0

    def vacio (self):
        self.__Nitems == 0

    def lleno (self):
        self.__Nitems == self.__v

    def push (self, item):
        self.__v[self.__Nitems] = item
        self.__Nitems +=1

    def pop(self):  # SEXTO EJERCICIO
        if self.__Nitems == 0:
            return None
        item = self.__v[self.__Nitems - 1]
        self.__v[self.__Nitems - 1] = None
        self.__Nitems -= 1
        return item

    def traverse (self):
        for j in range (self.__Nitems):
            print(self.__v[j])

    def peek (self): #SEXTO EJERCICIO
        print(self.__v[self.__Nitems-1])

    def atras (self):
        while not self.vacio():
            tecla = input("Presione a si desea regresar al sitio anterior   ")
            if tecla == "a":
                cliente = self.pop()
                if cliente is not None:
                    print("Se encuentra en la pagina", cliente)
            else:
                print("Tecla incorrecta")
                return
