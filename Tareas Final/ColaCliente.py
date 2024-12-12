from Cola import cola

maxsize = 10
mi_cola = cola(maxsize)  # Cambiamos el nombre de la instancia para evitar conflictos

lista = [1, 2, 3, 4, 5, 7, 8, 9, 10]

for j in lista:
    mi_cola.enqueue(j)
mi_cola.traverse()
print("El primer elemeto de la cola es:")
mi_cola.peek()

mi_cola.dequeue()
print("La cola sin el primer elemento es:")
mi_cola.traverse()
print("El primer elemeto de la cola es:")
mi_cola.peek()
