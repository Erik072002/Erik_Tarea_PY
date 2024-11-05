class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially

    def __len__(self):  # Special def for len() func
        return self.__nItems  # Return number of items

    def get(self, n):  # Return the value at index n
        if 0 <= n and n < self.__nItems:  # Check if n is in bounds, and
            return self.__a[n]  # only return item if in bounds

    def set(self, n, value):  # Set the value at index n
        if 0 <= n and n < self.__nItems:  # Check if n is in bounds, and
            self.__a[n] = value  # only set item if in bounds

    def insert(self, item):  # Insert item at end
        self.__a[self.__nItems] = item  # Item goes at current end
        self.__nItems += 1  # Increment number of items

    def find(self, item):  # Find index for item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # If found,
                return j  # then return index to item
        return -1  # Not found -> return -1


    def search(self, item): # Search for item
        return self.get(self.find(item))  # and return item if found

    def delete(self, item):  # Elimina la primera aparición de un elemento
        for j in range(self.__nItems):  # Entre los elementos actuales
            if self.__a[j] == item:  # Si se encuentra el elemento
                self.__nItems -= 1  # Decrementa el número de elementos
                for k in range(j, self.__nItems):  # Mueve los elementos de la derecha hacia la izquierda
                    self.__a[k] = self.__a[k + 1]
                return True  # Devuelve True si se eliminó con éxito
        return False  # Si no se encuentra el elemento, devuelve False

    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__nItems): # and apply a function
            function(self.__a[j])

    def swap(self, j, k):
        """Intercambia los valores en los índices j y k."""
        if (0 <= j < self.__nItems and  # Verifica si los índices están dentro de los límites
                0 <= k < self.__nItems):
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def bubbleSort(self): #EJERCICIO 3.1

        izquierda = 0
        derecha = self.__nItems - 1

        while izquierda < derecha:
            # Mover el elemento más grande hacia la derecha
            for i in range(izquierda, derecha):
                if self.__a[i] > self.__a[i + 1]:
                    self.swap(i, i + 1)
            # Reducir el límite derecho
            derecha -= 1

            # Mover el elemento más pequeño hacia la izquierda
            for i in range(derecha, izquierda, -1):
                if self.__a[i] < self.__a[i - 1]:
                    self.swap(i, i - 1)
            # Aumentar el límite izquierdo
            izquierda += 1


    def selectionSort(self):
        for outer in range(self.__nItems - 1):
            min = outer
            # Assume min is leftmost
            for inner in range(outer + 1, self.__nItems):
                if self.__a[inner] < self.__a[min]:  # If we find new
                    min = inner
                self.swap(outer, min)

    def getmedia(self): #EJERCICIO 3.2
        contador = (self.__nItems // 2)
        if self.__nItems % 2 != 0:
            return self.__a[contador]

        else:
            mediana1 = self.__a [contador]
            mediana2 = self.__a [contador - 1]
            return (mediana1 + mediana2) / 2

    def dublicate(self): #EJERCICIO 3.3
        # Eliminamos duplicados en un arreglo ordenado
        if self.__nItems < 2:
            return

        posicion_unica = 1
        for i in range(1, self.__nItems):
            if self.__a[i] != self.__a[i - 1]:
                self.__a[posicion_unica] = self.__a[i]
                posicion_unica += 1

        self.__nItems = posicion_unica

    def oddEvenSort(self): #EJERCICIO 3.4
        contador_par = 0
        contador_impar = 0
        ordenar = False

        while not ordenar:
             ordenar = True

             for j in range (1, self.__nItems -1, 2):
                 if self.__a [j] > self.__a [j + 1]:
                     self.swap(j, j + 1)
                     contador_par += 1
                     ordenar = False

             for j in range (0, self.__nItems - 1, 2):
                 if self.__a [j] > self.__a [j + 1]:
                     self.swap(j, j + 1)
                     contador_impar += 1
                     ordenar = False

        return contador_par, contador_impar

    def ordenarPorInsercion(self): #EJERCICIO 3.5
        contador1 = 0
        contador2 = 0
        # Ordenar mediante inserciones repetidas
        for externo in range(1, self.__nItems):  # Marca un elemento
            temp = self.__a[externo]  # Almacena el elemento marcado en temp
            contador1 += 1
            interno = externo  # El bucle interno comienza en el elemento marcado


            # Desplaza elementos a la derecha hasta encontrar la posición correcta para temp
            while interno > 0 and temp < self.__a[interno - 1]:  # Si el elemento marcado es menor,
                contador2 +=1
                self.__a[interno] = self.__a[interno - 1]  # desplaza el elemento a la derecha
                interno -= 1  # Mueve hacia la posición siguiente a la izquierda


            self.__a[interno] = temp  # Inserta el elemento marcado en su posición correcta
            contador1 +=1
        return contador1, contador2

    def insertionSortAndDedupe(self): #EJERCICIO 3.6
        """Ordena el arreglo por inserción y elimina elementos duplicados."""
        special_value = float('-inf')  # Valor especial para indicar duplicados

        # Ordenamiento por inserción modificado para manejar duplicados
        for externo in range(1, self.__nItems):
            temp = self.__a[externo]
            interno = externo

            # Busca la posición correcta para temp y desplaza elementos hacia la derecha
            while interno > 0 and temp < self.__a[interno - 1]:
                self.__a[interno] = self.__a[interno - 1]
                interno -= 1

            # Inserta el valor temporal en su posición
            self.__a[interno] = temp

        # Segunda pasada para eliminar duplicados
        write_index = 0
        last_value = None  # Variable para almacenar el último valor escrito
        for i in range(self.__nItems):
            if self.__a[i] != last_value:  # Mantiene sólo los valores únicos
                self.__a[write_index] = self.__a[i]
                write_index += 1
                last_value = self.__a[i]  # Actualiza el último valor escrito

        self.__nItems = write_index  # Actualiza el número de elementos tras eliminar duplicados