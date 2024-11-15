def filtrar_e_invertir(numeros, S):
    resultado = []
    
    # Recorrer cada número en la lista
    for numero in numeros:
        digitos_filtrados = []
        
        # Convertir el número a cadena para recorrer cada dígito
        for digito in str(numero):
            # Convertir el dígito en entero
            d = int(digito)
            # Solo agregar el dígito si es menor que S
            if d < S:
                digitos_filtrados.append(d)

        # Si el número aún tiene dígitos válidos, lo agregamos
        if digitos_filtrados:
            # Reconstruimos el número a partir de los dígitos filtrados
            numero_filtrado = int("".join(map(str, digitos_filtrados)))
            resultado.append(numero_filtrado)
    
    # Invertir el resultado
    resultado.reverse()
    
    # Imprimir el resultado
    print("Resultado:", resultado)

# Solicitar al usuario que ingrese los números 
entrada = input("Ingrese los números separados por comas: ")
S = 7

# Convertir la entrada en una lista de enteros
numeros = list(map(int, entrada.split(',')))

# Llamar a la función con los números ingresados
filtrar_e_invertir(numeros, S)
