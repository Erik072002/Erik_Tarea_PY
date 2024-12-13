from Ordenar_Cola import ordenar

MaxSize = 10

cola = ordenar(MaxSize)

m_cola = [3,2,5,6,8,9,10,13,16,29]

for j in m_cola:
    cola.enqueue(j)

cola.traverse()

cola.ordenar_cola()
print("La cola ordenada es: ")
cola.traverse()