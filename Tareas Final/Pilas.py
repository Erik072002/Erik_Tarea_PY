class pilas (object):
    def __init__(self, Inicializace):
        self.__v = [None] * Inicializace
        self.__Nitems = 0

    def push (self, item): #SEXTO EJERCICIO
        self.__v[self.__Nitems] = item
        self.__Nitems +=1

    def traverse (self): #SEXTO EJERCICIO
        for j in range(self.__Nitems):
            print(self.__v[j])

    def pop (self): #SEXTO EJERCICIO
        if self.__Nitems == 0:
            return None
        item = self.__v[self.__Nitems - 1]
        self.__v[self.__Nitems - 1] = None
        self.__Nitems -= 1
        return item

    def peek (self): #SEXTO EJERCICIO
        print(self.__v[self.__Nitems-1])

    def getbalanceo(self): #SEPTIMO EJERCICIO
        balanceo = 0
        for j in range (self.__Nitems):
            if self.__v[j] != "()":
                balanceo -= 1
            elif self.__v[j] == "()":
                balanceo += 1
        if balanceo == self.__Nitems:
            print("Parentesis balanceados")
        else:
            print("Parentesis no balanceados")

    def getinvertir (self): #OCTAVO EJERCICIO
        cadena = []
        for j in range (self.__Nitems -1, -1,-1):
            cadena.append(self.__v[j])
        return cadena

