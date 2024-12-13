from Fusionar_dos_Listas_Enlazadas import ListaEnlazada
#EJERCICIO 19
lista1 = ListaEnlazada()
lista1.agregar_al_final(1)
lista1.agregar_al_final(3)
lista1.agregar_al_final(5)
lista1.agregar_al_final(7)

#EJERCICIO 19
lista2 = ListaEnlazada()
lista2.agregar_al_final(2)
lista2.agregar_al_final(4)
lista2.agregar_al_final(6)
lista2.agregar_al_final(8)

print("Lista 1:")
lista1.traverse()

print("Lista 2:")
lista2.traverse()

# Fusionar las listas
lista_fusionada = lista1.fusionar(lista2)

print("Lista fusionada:")
lista_fusionada.traverse()