datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]
# Cambiar puntaje (ejercicio 1)
print(datos[2]["nombre"])
datos[2]["puntaje"] = 75
print(datos[2]["puntaje"])

# Creación de la función (ejercicio 2)
def puntaje_carlos():
    for i in datos:
        print(f"{datos[0]['nombre']} obtuvo {datos[0]['puntaje']} puntos")
        break
puntaje_carlos()

# Creación de función para imprimir valores (ejercicio 3)
def recibir_datos(nombre):
    ingresar = input("Ingrese el dato: ")
    for i in datos:
     if ingresar == i["nombre"]:
        print(f"{i['nombre']} obtuvo {i['puntaje']} puntos")
recibir_datos("nombre")


# 1. Cambiar el puntaje de Pedro a 75
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores

