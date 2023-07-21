flag = True
arreglo = [] # arreglo vacio
suma = 0


while flag:
    numero = input('Introduzca un número: ')
    if numero == "fin":
        print("\nNúmero mayor de los elementos: ", max(arreglo))
        print("Número mínimo de los elementos: ", min(arreglo))
        flag = False
    else:
        try:
            numero = int(numero)
            arreglo.append(numero)
        except:
            print("Entrada inválida")