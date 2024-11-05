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

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))

print("Setting item at index 3 to 33")
arr.set(3, 33)

print("Array after deletions has", len(arr), "items")
arr.traverse()


contador_par, contador_impar = arr.oddEvenSort()
print("Arreglo ordenado par e impar")
print("Número de intercambios en la pasada impar:", contador_par)
print("Número de intercambios en la pasada par:", contador_impar)
arr.traverse()

arr.bubbleSort()
print("Arreglo ordenado")
arr.traverse()

print("La mediana es =", arr.getmedia())

arr.dublicate()
print("La cadena sin duplicados es = ")
arr.traverse()
