from Lista_Enlazada import ListaEnlazada

lista = ListaEnlazada()
lista.agregar_al_final(10) #EJERCICIO 16
lista.agregar_al_final(20) #EJERCICIO 16
lista.agregar_al_final(30) #EJERCICIO 16
lista.agregar_al_final(30) #EJERCICIO 16
lista.agregar_al_final(50) #EJERCICIO 16

print("Lista después de agregar elementos:")
lista.traverse()

nodo = lista.buscar(20) #EJERCICIO 16
if nodo:
    print(f"Elemento encontrado: {nodo.valor}")
else:
    print("Elemento no encontrado.") #EJERCICIO 16

lista.invertir() #EJERCICIO 17
print("La lista invertida es:")
lista.traverse() #EJERCICIO 17

lista.eliminar_duplicados() #EJERCICIO 18
print("La lista sin duplicados es: ")
lista.traverse() #EJERCICIO 18