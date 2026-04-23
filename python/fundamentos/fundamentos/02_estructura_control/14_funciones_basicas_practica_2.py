import os
# Funciones básicas práctica 2


# Ejercicio 1 -----------------
#
# Calcula experiencia
def multiplica_por_2(num):
    result = []
    for i in range(num + 1):
        result.append(i * 2)
    return result
def ejercicio1():
 result1 = multiplica_por_2(5)
 print(result1)
# Debe retornar: [0, 2, 4, 6, 8, 10]



# Ejercicio 2 --------------
#
# Analiza publicaciones
def suma_y_resta(list):
   suma = list[0] + list[1]
   resta = list[0] - list[1]
   print(f"Suma: {suma}")
   return resta

def ejercicio2():
 resta = suma_y_resta([120, 115])
 print(f"Resta: {resta}")
# Imprime: 235 y retorna: 5



# Ejercicio 3 -----------------
#
# Puntaje ajustado
def sumatoria_menos_longitud(sumatoria):
    total = sum(sumatoria)
    longitud = len(sumatoria)
    resultado = total - longitud
    print(f"Total = {total}, Longitud = {longitud}")
    return resultado

def ejercicio3():
    retornar = sumatoria_menos_longitud([10, 5, 3, 7])
    print(f"El resultado del retorno es: {retornar}")
# Suma total = 25, longitud = 4, debe retornar: 21



# Ejercicio 4 -------------
#
# Ajusta visualizaciones
def valores_multiplicados_segundo(lista):
   if len(lista) < 2:
      print(len(lista))
      return []
   else:
      segEle = lista[1]
      nueva_lista = []
      for num in lista:
         nueva_lista.append(num * segEle)
         longitud = len(nueva_lista)
         print(longitud)
         return nueva_lista
      
def ejercicio4():
   
 result1 = valores_multiplicados_segundo([100, 3, 50, 20])
 print(result1)
 print()
    # Imprime: 4 y retorna: [300, 9, 150, 60]
 result2 = valores_multiplicados_segundo([100])
 print(result2)
    # Imprime: 1 y retorna: []



# Ejercicio 5 --------------
#
# Genera precio fijo
def valor_multiplicado_longitud(a, b):
   multList = []
   for i in range(0, b):
      multList.append(a * b)
      return multList

def ejercicio5():
 result1 = valor_multiplicado_longitud(5, 2)
 print(f"Resultado 1: {result1}")
# Debe retornar: [10, 10]
 result2 = valor_multiplicado_longitud(7, 5)
 print(f"Resultado 2: {result2}")
# Debe retornar: [35, 35, 35, 35, 35]


def limpiar_consola():
    os.system('cls')

# Menú de navegación para ejercicios
continuar = True
while continuar:
    print("\n--- Ejercicios Python ---")
    print("--- Ejercicio 1: ---")
    print("--- Ejercicio 2: ---")
    print("--- Ejercicio 3: ---")
    print("--- Ejercicio 4: ---")
    print("--- Ejercicio 5: ---")
    opcion = input("\nElige una opción (1-5) (0 para salir) = ")
    if opcion =="1":
        limpiar_consola()
        print("\nEjecutando ejercicio 1: ")
        ejercicio1()
    elif opcion =="2":
        limpiar_consola()
        print("\nEjecutando ejercicio 2: ")
        ejercicio2()
    elif opcion =="3":
        limpiar_consola()
        print("\nEjecutando ejercicio 3: ")
        ejercicio3()
    elif opcion =="4":
        limpiar_consola()
        print("\nEjecutando ejercicio 4: ")
        ejercicio4()
    elif opcion =="5":
        limpiar_consola()
        print("\nEjecutando ejercicio 5: ")
        ejercicio5()
    else:
        limpiar_consola()
        print("Opción no válida, intenta otra vez")