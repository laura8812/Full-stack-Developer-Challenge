def cuadrados_ordenados(matriz, S):
    SS = S * 11
    resultado = []
    
    # Calcular los cuadrados y agregar los que están en el rango
    for num in matriz:
        cuadrado = num * num
        if 0 <= cuadrado <= SS:
            resultado.append(cuadrado)
    
    # Ordenar el resultado en orden ascendente usando el método burbuja
    for i in range(len(resultado) - 1):
        for j in range(len(resultado) - i - 1):
            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]

    # Imprimir el resultado
    print("Resultado:", resultado)

# Solicitar al usuario que ingrese la matriz de números 
entrada = input("Ingrese los números separados por comas: ")
S = 7

# Convertir la entrada en una lista de enteros
matriz = list(map(int, entrada.split(',')))

# Llamar a la función con la matriz ingresada
cuadrados_ordenados(matriz, S)
