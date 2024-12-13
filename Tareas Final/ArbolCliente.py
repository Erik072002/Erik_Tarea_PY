from ArbolBin import ArbolBinario
arbol = ArbolBinario()

# Insertar elementos
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

# Recorrer el árbol en orden
print("Recorrido inorder:")
arbol.recorrer_inorder()
print("None")  # Final del recorrido

# Buscar elementos
print("\nBúsqueda de elementos:")
print("¿Existe 40?:", arbol.buscar(40))
print("¿Existe 90?:", arbol.buscar(90))