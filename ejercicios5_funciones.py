# funcion de conversion de temperatura
def convertir_temperatura(valor, de_unidad, a_unidad):
    # Convertir todas las unidades a minúsculas para facilitar la comparación
    de_unidad = de_unidad.lower()
    a_unidad = a_unidad.lower()
    
    if de_unidad == "celsius":
        if a_unidad == "fahrenheit":
            return (valor * 9/5) + 32
        elif a_unidad == "kelvin":
            return valor + 273.15
        elif a_unidad == "celsius":
            return valor
        else:
            return "Unidad de destino no reconocida."
    
    elif de_unidad == "fahrenheit":
        if a_unidad == "celsius":
            return (valor - 32) * 5/9
        elif a_unidad == "kelvin":
            return (valor - 32) * 5/9 + 273.15
        elif a_unidad == "fahrenheit":
            return valor
        else:
            return "Unidad de destino no reconocida."
    
    elif de_unidad == "kelvin":
        if a_unidad == "celsius":
            return valor - 273.15
        elif a_unidad == "fahrenheit":
            return (valor - 273.15) * 9/5 + 32
        elif a_unidad == "kelvin":
            return valor
        else:
            return "Unidad de destino no reconocida."
    
    else:
        return "Unidad de origen no reconocida."

# Ejemplo de uso
valor = 100
print(f"{valor}°C a Fahrenheit: {convertir_temperatura(valor, 'Celsius', 'Fahrenheit')}°F")
print(f"{valor}°F a Celsius: {convertir_temperatura(valor, 'Fahrenheit', 'Celsius')}°C")
print(f"{valor}°C a Kelvin: {convertir_temperatura(valor, 'Celsius', 'Kelvin')}K")
print(f"{valor}K a Celsius: {convertir_temperatura(valor, 'Kelvin', 'Celsius')}°C")
