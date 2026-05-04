''' 6- Crear una función que reciba una lista de edades y clasifique a las personas en tres grupos: menores de edad, adultos y adultos mayores (60+).
 Debe mostrar la cantidad de personas en cada grupo. '''

def solicitar_edad(cantidad):
    menores = 0
    adultos = 0
    adultos_mayores = 0

    for i in range(cantidad):
        edad = int(input("Ingrese su edad: "))
        if edad < 18:
            menores += 1
        elif edad < 60:
            adultos += 1
        else:
            adultos_mayores += 1
    return menores, adultos, adultos_mayores

def resultado_ejercicio():
    cantidad = int(input("Ingrese la cantidad de edades: "))
    menores, adultos, adultos_mayores = solicitar_edad(cantidad)
    print(f"Menores: {menores}")
    print(f"Adultos: {adultos}")
    print(f"Adultos mayores: {adultos_mayores}")

resultado_ejercicio()
