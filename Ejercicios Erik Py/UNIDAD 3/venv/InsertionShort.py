import Array

maxSize = 11
arr = Array.Array(maxSize)
arr.insert(77)
arr.insert(99)
arr.insert(100)
arr.insert(12)
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert(21)
arr.insert(-17)
arr.insert(21)
# Max size of the array
# Create an array object
# Insert 10 items
print("Array containing", len(arr), "items")
arr.traverse()

contador1, contador2 = arr.ordenarPorInsercion()

print("El arreglo ordenado es: ")
print("El numero de copias es = ", contador1)
print("El numero de comparaciones = ", contador2)
arr.traverse()