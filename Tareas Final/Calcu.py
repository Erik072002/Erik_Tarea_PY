class calculadora (object):

    def __init__(self, inicializar):
            self.__v = [None] * inicializar
            self.__Nitems = 0

    def push (self, item):
        self.__v[self.__Nitems] = item
        self.__Nitems += 1

    def pop (self):
        if self.__Nitems > 0:
            self.__Nitems -=1
            return self.__v[self.__Nitems]
        else:
            print("La pila esta vacia")
            return None

    def traverse (self):
        for j in range(self.__Nitems):
            print(self.__v[j])

    def calculadora (self):
        for num in range (self.__Nitems -1, -1, -1):
            token = self.__v[num]  # Obtenemos el elemento actual

            if str(token).isdigit():  # Verificar si es un número
                self.push(int(token))  # Empujar de nuevo como número
            else:  # Si es un operador, se procesan los dos últimos números
                b = self.pop()
                a = self.pop()
                if a is None or b is None:
                    print("No hay suficientes elementos para operar.")
                    return
                # Realizar la operación
                if token == '+':
                    self.push(a + b)
                elif token == '-':
                    self.push(a - b)
                elif token == '/':
                    if b != 0:  # Verificar división por cero
                        self.push(a / b)
                    else:
                        print("Error: División por cero.")
                        return
                elif token == '*':
                    self.push(a * b)

        resultado = self.pop()
        if self.__Nitems == 0:
            return resultado
        else:
            print("Error: La expresión no se evaluó correctamente.")
            return None
