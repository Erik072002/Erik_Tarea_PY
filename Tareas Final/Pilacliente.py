from Pilas import pilas

TamañoMax= 10
pila = pilas(TamañoMax)

#cadena = [1,2,3,4,5,6,7,8,9,10]
cadena = ["()","()", "()", "()"]

for j in cadena:
    pila.push(j)
pila.traverse()

pila.pop()
print("La pila con el ultimo elemento eliminado es:")
pila.traverse()
print("El ultimo elemento es:")
pila.peek()

pila.getbalanceo()

print("La pila invertida es:", pila.getinvertir())


