import Array

maxSize = 10
arr = Array.Array(maxSize)
arr.insert(77)
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(44)
arr.insert("baz")
arr.insert(-17)
# Max size of the array
# Create an array object
# Insert 10 items
print("Array containing", len(arr), "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))

print("Setting item at index 3 to 33")
arr.set(3, 33)

print("Array after deletions has", len(arr), "items")
arr.traverse()

print("El numero mayor = ", arr.getMaxNumber())

print("La cadena eliminando el numero mayor =", arr.deleteMaxNum())
arr.traverse()
print("Array after deletions has", len(arr), "items")


print("\nOrdenando el arreglo...")

band = True #EJERCICIO 2.3
while not band:
    band = True
    for j in range(len(arr) - 1):
        # Solo comparamos si ambos son números
        if isinstance(arr.get(j), (int, float)) and isinstance(arr.get(j + 1), (int, float)):
            if arr.get(j) > arr.get(j + 1):
                # Intercambiamos los valores
                antiguo = arr.get(j)
                arr.set(j, arr.get(j + 1))
                arr.set(j + 1, antiguo)
                band = False

print("\nArray after sorting (only numbers):")
arr.traverse()

print("El arreglo sin dublicados: ")
arr.removeDupes()

print("")
arr.traverse()


