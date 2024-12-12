from Suma import suma

maxSize = 10
suma = suma(maxSize)
cadena = [1,2,3,3,4,4,7,8,9,10]
#for j in range(1,11):
    #suma.insertar(j)


for k in cadena:
    suma.insertar(k)
suma.traverse()
max = 0
for j in cadena: #SEGUNDO EJERCICIO
    if j > max:
        max = j

min = max
for i in cadena: #SEGUNDO EJERCICIO
    if i < min:
        min = i

print("El valor maximo es", max)
print("El valor minimo es", min)

print("La suma de los numeros es", suma.suma())

print("El numero maximo es:", suma.getmax())
print("El numero minimo es:", suma.getmin())
print("La cadena invertida es:", suma.getinver())
print(suma.buscar())
print("La cadena sin duplicados")
suma.getduplicados()
suma.traverse()
