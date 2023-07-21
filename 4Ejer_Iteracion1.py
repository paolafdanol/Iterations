flag = True
arreglo = [] # arreglo vacio
suma = 0


while flag:
    numero = input('Introduzca un número: ')
    if numero == "fin":
        print("\nTotal de suma de los elementos: " + str(sum(arreglo)))
        print("Cantidad de elementos: " + str(len(arreglo)))
        print("Promedio de los elementos: ", (sum(arreglo)/len(arreglo)))
        flag = False
    else:
        try:
            numero = int(numero)
            arreglo.append(numero)
        except:
            print("Entrada inválida")

