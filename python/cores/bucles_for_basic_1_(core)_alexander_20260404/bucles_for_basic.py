# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
def generadorNiveles():
    for i in range(101):
        print(i)


# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
def potenciadoresEnergia():
    for i in range(2, 501, 2):
        print(i)


# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
def trampaEmojis():
    for i in range(1, 101):
        if i % 10 == 0:
            print("😃")
        elif i % 5 == 0:
            print("😆")

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
def sumaColosal():
    sumaTotal = 0
    for i in range(0, 500001, 2):
        sumaTotal += i
    print(f"Suma total: {sumaTotal}")

# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
def retrocesoTemporal():
    for anio in range(2024, -2, -3):
        print(f"Año: {anio}")


# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
def contadorDinamico():
    inicio = 3
    fin = 10
    salto = 2
    for nivel in range(inicio, fin + 1):
        if nivel % salto == 0:
            print(nivel)

# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10


continuar = True
while continuar:
    print("\n---Ejercicios Python---")
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    print("---Ejercicio 6---")
    opcion = input("\n---Elije una opción: (1-6) (0 para salir)")
    if opcion == "1":
        print("\nEjecutar ejercicio 1: ")
        generadorNiveles()
    elif opcion == "2":
        print("\nEjecutar ejercicio 2: ")
        potenciadoresEnergia()
    elif opcion == "3":
        print("\nEjecutar ejercicio 3: ")
        trampaEmojis()
    elif opcion == "4":
        print("\nEjecutar ejercicio 4: ")
        sumaColosal()
    elif opcion == "5":
        print("\nEjecutar ejercicio 5: ")
        retrocesoTemporal()
    elif opcion == "6":
        print("\nEjecutar ejercicio 6: ")
        contadorDinamico()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")