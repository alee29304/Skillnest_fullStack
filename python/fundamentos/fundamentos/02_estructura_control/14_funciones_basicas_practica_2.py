# Funciones básicas práctica 2

#1. -Ejercicio 1 -----------------
#
# Calcula experiencia
def multiplica_por_2(num):
    result = []
    for i in range(num + 1):
        result.append(i * 2)
    return result
result1 = multiplica_por_2(5)
print(result1)
# Debe retornar: [0, 2, 4, 6, 8, 10]



#2. - Ejercicio 2 --------------
#
# Analiza publicaciones
def suma_y_resta():
   pass

suma_y_resta([120, 115])
# Imprime: 235 y retorna: 5



#3. -Ejercicio 3 -----------------
#
# Puntaje ajustado
def sumatoria_menos_longitud():
    pass

sumatoria_menos_longitud([10, 5, 3, 7])
# Suma total = 25, longitud = 4, debe retornar: 21



# Ajusta visualizaciones
valores_multiplicados_segundo([100, 3, 50, 20])
# Imprime: 4 y retorna: [300, 9, 150, 60]

valores_multiplicados_segundo([100])
# Imprime: 1 y retorna: []


# Genera precio fijo
valor_multiplicado_longitud(5, 2)
# Debe retornar: [10, 10]

valor_multiplicado_longitud(7, 5)
# Debe retornar: [35, 35, 35, 35, 35]