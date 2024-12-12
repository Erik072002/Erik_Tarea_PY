class colacir (object):

    def __init__(self, Inicializar):
        self.__v = [None] * Inicializar
        self.__frente = 0
        self.__atras = 0
        self.__Nitems = 0
        self.maxsize = Inicializar

    def vacio (self):
        self.__Nitems == 0

    def lleno (self):
        self.__Nitems == self.__v

    def enqueue(self, item): #EJERCICIO 13
        if self.lleno():
            print("La cola circular esta llena")
        else:
            self.__v[self.__atras]=item
            self.__atras = (self.__atras +1) % self.maxsize
            self.__Nitems +=1

    def dequeue (self): #EJERCICIO 13
        if self.lleno():
            print("La cola circular esta llena")
        item= self.__v[self.__frente]
        self.__v[self.__frente]= None
        self.__frente = (self.__frente + 1) % self.maxsize
        return item

    def traverse (self):
        for j in range(self.__Nitems):
            print(self.__v[j])

    def ordenamiento (self): #EJERCICIO 14
        par = []
        impar = []
        for j in range(self.__Nitems):
            index = (self.__frente + j) % len(self.__v)
            elemento = self.__v[index]
            if elemento is not None:
                if elemento % 2 == 0:
                    par.append(elemento)
                else:
                    impar.append(elemento)

        reorganizado = par + impar

        for k in range(len(reorganizado)):
            self.__v[(self.__frente + k) % len(self.__v)] = reorganizado[k]


        self.__atras = (self.__frente + len(reorganizado)) % len(self.__v)



