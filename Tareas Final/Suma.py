class suma (object):

    def __init__(self, initialSize):
        self.__v = [None] * initialSize
        self.__nItems = 0

    def insertar (self, item):
        self.__v[self.__nItems] = item
        self.__nItems += 1

    def delete (self, item):
        for j in range (self.__nItems):
            if self.__v[j] == item:
                self.__nItems -= 1
                for k in range (j, self.__nItems):
                     self.__v[k] = self.__v[k+1]
                return True
        return False

    def __len__(self):
        return self.__nItems

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__v[j])

    def find(self, item):
        for j in range(self.__nItems):
            if self.__v[j] == item:
                return j
        return -1

    def suma(self): #PRIMER EJERCICIO
        suma = 0
        for j in range (0, self.__nItems):
             suma = self.__v[j] + suma
        return suma

    def getmax(self):
        maxnumero= 0
        for j in range (0, self.__nItems):
            if maxnumero is None or self.__v[j] > maxnumero:
                maxnumero = self.__v[j]
        return maxnumero

    def getmin(self):
        minnumero = self.__v[0]
        for j in range (0, self.__nItems):
            if self.__v[j] < minnumero:
                minnumero = self.__v[j]
        return minnumero

    def getinver(self): #TERCER EJERCICIO
        cadena = []
        for j in range (self.__nItems - 1 , -1, -1):
            cadena.append(self.__v[j])
        return cadena

    def buscar(self): #CUARTO EJERCICIO
        num= int(input("Ingrese el numero a buscar"))
        for j in range (0, self.__nItems - 1):
            if num == self.__v[j]:
                return print("Tu numero si se encuentra en el arreglo")
        else:
            return print("Tu numero no se encuentra")

    def getduplicados(self): #QUINTO EJERCICIO
        for j in range (0, self.__nItems - 1):
            numero = self.__v[j]
            for i in range (j+1, self.__nItems - 1):
                if numero == self.__v[i]:
                    self.delete(self.__v[i])


