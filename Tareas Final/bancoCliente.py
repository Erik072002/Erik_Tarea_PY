from Banco import banco

MaxSize = (10)

banc = banco(MaxSize)
Clientes = [1,2,3,4,5,6,7,8,9,10]

for j in Clientes:
    banc.enqueue(j)
banc.traverse()

banc.dequeue()
banc.traverse()

banc.fila()