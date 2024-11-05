from SimpleStack import Stack
import string

def is_palindrome(input_string): #EJERCICIO 4.2
    stack = Stack(100)  # Crea una pila para contener las letras

    # Filtra el input_string para eliminar caracteres no alfabéticos y convertir a minúsculas
    filtered_string = ''.join(char.lower() for char in input_string if char.isalpha())

    # Apila cada letra en la pila
    for letter in filtered_string:
        if not stack.isFull():
            stack.push(letter)

    reverse = ''  # Inicializa la cadena revertida

    # Revierte la cadena sacando elementos de la pila
    while not stack.isEmpty():
        reverse += stack.pop()

    # Compara la cadena original filtrada con la cadena revertida
    return filtered_string == reverse

# Prueba del programa
input_string = "A man, a plan, a canal, Panama."
if is_palindrome(input_string):
    print(f'"{input_string}" es un palíndromo.')
else:
    print(f'"{input_string}" no es un palíndromo.')