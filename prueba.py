''' 6- Crear una función que reciba una lista de edades y clasifique a las personas en tres grupos: menores de edad, adultos y adultos mayores (60+).
 Debe mostrar la cantidad de personas en cada grupo. '''

def veces_repetidas():
    cantidad = int(input("Ingrese la cantidad de edades: "))

    adultos_mayores = 0
    adultos = 0
    menores = 0
    
    while (cantidad):
        edad = int(input("Ingrese su edad: "))
        if edad < 18:
            menores += 1
        elif edad < 60:
            adultos += 1
        else:
            adultos_mayores += 1
            print(f"Menores: {menores}")
            print(f"Adultos: {adultos}")
            print(f"Adultos mayores: {adultos_mayores}")
veces_repetidas()