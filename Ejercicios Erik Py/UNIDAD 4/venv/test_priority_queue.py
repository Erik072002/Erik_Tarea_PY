from PriorityQueue import PriorityQueue


def test_priority_queue():
    # Crear una cola de prioridad con capacidad para 5 elementos
    pq = PriorityQueue(5)

    # Insertar elementos sin orden específico de prioridad
    pq.insert(10)
    pq.insert(30)
    pq.insert(20)
    pq.insert(40)
    pq.insert(15)

    print("Contenido de la cola después de las inserciones (sin ordenar por prioridad):")
    print(pq)

    # Ver el elemento de mayor prioridad
    print("Elemento de mayor prioridad (peek):", pq.peek())

    # Remover el elemento de mayor prioridad
    removed = pq.remove()
    print(f"Elemento removido de mayor prioridad: {removed}")
    print("Contenido de la cola después de remover el elemento de mayor prioridad:")
    print(pq)

    # Probar el método `remove` hasta vaciar la cola
    while not pq.isEmpty():
        print("Elemento removido:", pq.remove())
        print("Contenido de la cola:", pq)

    # Intentar remover de una cola vacía para verificar el manejo de errores
    try:
        pq.remove()
    except Exception as e:
        print("Error al remover de una cola vacía:", e)


# Ejecutar la prueba
test_priority_queue()
