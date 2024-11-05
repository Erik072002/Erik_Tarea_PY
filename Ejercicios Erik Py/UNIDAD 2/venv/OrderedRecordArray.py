class OrderedRecordArray(object):
    def __init__(self, initialSize, key=identity):  # Constructor
        self.__a = [None] * initialSize  # Arreglo almacenado como lista
        self.__nItems = 0  # Inicialmente no hay elementos
        self.__key = key  # Función clave
        self.__resize_factor = resize_factor  # Factor de expansión multiplicativa
        self.__fixed_increment = fixed_increment  # Incremento fijo de tamaño

    def __len__(self):
        return self.__nItems  # Definición especial para len(), devuelve el número de elementos

    def get(self, n):  # Retorna el valor en el índice n
        if n >= 0 and n < self.__nItems:  # Verifica si n está dentro de los límites
            return self.__a[n]  # Solo retorna el elemento si está en los límites
        raise IndexError("Index " + str(n) + " is out of range")

    def traverse(self, function=print):  # Recorre todos los elementos y aplica una función
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        ans = "["  # Rodea con corchetes
        for i in range(self.__nItems):
            if len(ans) > 1:  # Excepto junto al corchete izquierdo,
                ans += ", "  # separa los elementos con una coma
            ans += str(self.__a[i])  # Añade la representación en cadena del elemento
        ans += "]"  # Cierra con el corchete derecho
        return ans

    def find(self, key):  # Encuentra el índice en o justo debajo de la clave en la lista ordenada
        lo = 0
        hi = self.__nItems - 1
        while lo <= hi:
            mid = (lo + hi) // 2  # Selecciona el punto medio
            if self.__key(self.__a[mid]) == key:  # ¿Encontramos el elemento?
                return mid  # Retorna la ubicación del elemento
            elif self.__key(self.__a[mid]) < key:  # ¿La clave está en la mitad superior?
                lo = mid + 1  # Sí, sube el límite inferior
            else:
                hi = mid - 1  # No, pero podría estar en la mitad inferior
        return lo  # Elemento no encontrado, retorna el punto de inserción en su lugar

    def search(self, key):  # Busca un registro por su clave
        idx = self.find(key)
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx]  # y retorna el elemento si se encontró
        return None

    #EJERCICIO 2.7
    def __resize(self):  # Expande el tamaño del arreglo
        if self.__fixed_increment:  # Si se define un incremento fijo
            new_size = len(self.__a) + self.__fixed_increment
        else:  # Si no se define, usa el factor multiplicativo
            new_size = len(self.__a) * self.__resize_factor

        new_array = [None] * new_size  # Crea un nuevo arreglo más grande
        for i in range(self.__nItems):  # Copia los elementos al nuevo arreglo
            new_array[i] = self.__a[i]
        self.__a = new_array  # Reemplaza el arreglo original con el nuevo

    def insert(self, item):  # Inserta el elemento en la posición correcta
        if self.__nItems >= len(self.__a):  # Si el arreglo está lleno,
            raise Exception("Array overflow")  # lanza una excepción
        j = self.find(self.__key(item))  # Encuentra dónde debería ir el elemento
        for k in range(self.__nItems, j, -1):  # Mueve los elementos mayores hacia la derecha
            self.__a[k] = self.__a[k - 1]
        self.__a[j] = item  # Inserta el elemento
        self.__nItems += 1  # Incrementa el número de elementos

    #EJERCICIO 2.6
    def delete_all(self, key):  # Elimina todos los elementos que coincidan con la clave
        j = self.find(key)  # Encuentra el índice de la clave dada
        if j >= self.__nItems or self.__key(self.__a[j]) != key:
            return False  # Si no se encuentra la clave, retorna False

        # Inicia desde la posición de la primera coincidencia
        start = j
        end = start

        # Encuentra el rango de elementos con la clave duplicada
        while end < self.__nItems and self.__key(self.__a[end]) == key:
            end += 1

        # Calcula cuántos elementos se eliminarán
        num_deleted = end - start
        self.__nItems -= num_deleted  # Actualiza el número de elementos

        # Mueve los elementos restantes hacia la izquierda para llenar los espacios
        for k in range(start, self.__nItems):
            self.__a[k] = self.__a[k + num_deleted]

        # Borra las referencias sobrantes
        for k in range(self.__nItems, self.__nItems + num_deleted):
            self.__a[k] = None

        return True  # Retorna True indicando que se eliminaron elementos

    def merge(self, other): #EJERCICIO 2.5
        if self.__key != other.__key:
            raise ValueError("Cannot merge arrays with different key functions")

        # Crea un nuevo arreglo lo suficientemente grande para contener ambos arreglos
        merged_array = OrderedRecordArray(self.__nItems + other.__nItems, self.__key)

        i, j = 0, 0
        while i < self.__nItems and j < other.__nItems:
            # Compara los elementos por su clave y añade el menor
            if self.__key(self.__a[i]) <= self.__key(other.__a[j]):
                merged_array.insert(self.__a[i])
                i += 1
            else:
                merged_array.insert(other.__a[j])
                j += 1

        # Si quedan elementos en cualquiera de los dos arreglos, añádelos al arreglo fusionado
        while i < self.__nItems:
            merged_array.insert(self.__a[i])
            i += 1
        while j < other.__nItems:
            merged_array.insert(other.__a[j])
            j += 1

        # Actualiza el arreglo original con los resultados fusionados
        self.__a = merged_array.__a
        self.__nItems = merged_array.__nItems

