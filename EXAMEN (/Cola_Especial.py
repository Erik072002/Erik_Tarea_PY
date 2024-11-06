class Cola (object):
    def __init__(self, initialSize):  # Constructor
            self.__a = [None] * initialSize  # El array almacenado como lista
            self.__nItems = 0  # Inicialmente no hay elementos en el array
    
    def __len__(self):  # Definición especial para usar len()
        return self.__nItems  # Devuelve el número de elementos
    
    def insert(self, item):  
        self.__a[self.__nItems] = item  
        self.__nItems += 1  
    
    def push(self, item):  # Inserta un elemento al final
        if not self.isFull:
            self.__a[self.__nItems] = item  # El elemento va al final actual
            self.__nItems += 1  # Incrementa el número de elementos
        else:
            izquierda = 0
            derecha = 0
            while izquierda < derecha:
            # Mover el elemento más grande hacia la derecha
                for i in range(izquierda, derecha):
                    if self.__a[i] is self.isFull:
                        self.__a[self.__nItems] = item  # El elemento va al final actual
                        self.__nItems += 1  # Incrementa el número de elementos
            # Reducir el límite derecho
                derecha -= 1

            # Mover el elemento más pequeño hacia la izquierda
                for i in range(derecha, izquierda, -1):
                    if self.__a[i] is self.isFull:
                        self.__a[self.__nItems] = item  # El elemento va al final actual
                        self.__nItems += 1  # Incrementa el número de elementos
            # Aumentar el límite izquierdo
                izquierda += 1
        
    def pop(self):
        if self.__nItems == 0:
            return None  # Retorna None si no hay elementos en la lista

        # Accede correctamente al último elemento
        item = self.__a[self.__nItems - 1]

        # Elimina la referencia al elemento
        self.__a[self.__nItems - 1] = None

        # Decrementa el contador de elementos
        self.__nItems -= 1

        return item
    
    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__nItems): # and apply a function
            function(self.__a[j])
    
    def isEmpty(self):
        # Comprobar si la pila está vacía
        return self.__nItems - 1 < 0

    def isFull(self):
        # Comprobar si la pila está llena
        return self.__nItems >= len(self.__nItems) - 1
    
    