def cambio_minimo_imposible(monedas):
    # Ordenamos las monedas
    monedas.sort()
    
    # Inicializamos el cambio mínimo imposible
    cambio_minimo_imposible = 1
    
    # Recorremos cada moneda
    for moneda in monedas:
        # Si la moneda actual es mayor que el cambio mínimo imposible
        # significa que hemos encontrado una cantidad que no podemos formar
        if moneda > cambio_minimo_imposible:
            break
        
        # Si no, actualizamos el cambio mínimo imposible
        cambio_minimo_imposible += moneda
    
    return cambio_minimo_imposible

# Solicitar al usuario que ingrese las monedas
entrada = input("Ingrese los valores de las monedas separados por comas: ")

# Convertir la entrada en una lista de enteros
monedas = list(map(int, entrada.split(',')))

# Llamar a la función y mostrar el resultado
resultado = cambio_minimo_imposible(monedas)
print("La cantidad mínima de cambio que no se puede dar es:", resultado)
