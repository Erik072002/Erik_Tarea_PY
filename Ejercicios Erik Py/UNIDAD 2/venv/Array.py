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


    def search(self, item):# Search for item
        return self.get(self.find(item))  # and return item if found

    def delete(self, item):  # Elimina la primera aparición de un elemento
        for j in range(self.__nItems):  # Entre los elementos actuales
            if self.__a[j] == item:  # Si se encuentra el elemento
                self.__nItems -= 1  # Decrementa el número de elementos
                for k in range(j, self.__nItems):  # Mueve los elementos de la derecha hacia la izquierda
                    self.__a[k] = self.__a[k + 1]
                return True  # Devuelve True si se eliminó con éxito
        return False  # Si no se encuentra el elemento, devuelve False

# right over 1
# Return success flag
# Made it here, so couldn't find the item
    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__nItems): # and apply a function
            function(self.__a[j])

    def getMaxNumber(self): #EJERCICIO 2.1
        max_number = None
        for j in range(self.__nItems):
            if isinstance(self.__a[j], (int, float)):
                if max_number is None or self.__a[j] > max_number:
                    max_number = self.__a[j]
        return max_number

    def deleteMaxNum(self): #EJERCICIO 2.2
        max_number = self.getMaxNumber()
        if max_number is not None:
            return self.delete(max_number)
        return False

    def removeDupes(self): #EJERCICIO 2.4
        unique_items = []
        for j in range(self.__nItems):
            if self.get(j) not in unique_items:  # Check if the item is unique
                unique_items.append(self.get(j))  # Add unique item to the list
        # Update the array with unique items
        self.__nItems = len(unique_items)
        for j in range(self.__nItems):
            self.set(j, unique_items[j])  # Set unique items in the array
        # Clear the rest of the array
        for j in range(self.__nItems, len(self.__a)):
            self.set(j, None)


        