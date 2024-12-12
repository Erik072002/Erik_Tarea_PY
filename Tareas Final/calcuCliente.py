from Calcu import calculadora

MaxSize = 10

calc = calculadora(MaxSize)
expresion = "3 4 + 5 * 2 -"

# Recorrer la expresión y procesar cada token
for token in expresion.split():
    if token.isdigit():  # Si es un número, conviértelo a entero y empújalo a la pila
        calc.push(int(token))
    else:  # Si es un operador, empújalo como cadena
        calc.push(token)
calc.traverse()
calc.pop()
calc.traverse()
calc.calculadora()