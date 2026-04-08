"""
Tipos de datos primitivos
Estos son los elementos básicos de un lenguaje. La mayoría de los lenguajes comparten estos en común.
"""

# Booleanos
mayor_edad = True
tiene_bigote = False

# Númericos
mayoria_edad = 18
altura = 1.72

# Strings 
frase = "Anita lava la tina"

# Listas 
lista_vacia = []
gatos = ["Garfield", "Silvestre", "Hello Kitty"]
print(gatos[2]) #Imprime: Silvestre
gatos[1] = "Tom"
gatos.append("Felix")
print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty', 'Felix']
gatos.pop()
print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty']
gatos.pop(1)
print(gatos) #Imprime: ['Garfield', 'Hello Kitty']

# Tuplas
perro = ("Scooby Doo", "Gran Danés", "Scooby Galletas", 7)
print(perro[0]) #Imprime: Scooby Doo
perro[2] = "comida de perro" #ERROR: Las tuplas no pueden ser modificadas (TypeError: 'tuple' object does not support item assignment)

# Diccionarios 
diccionario_vacio = {}
persona = {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False}
persona['nombre'] = 'Valeria'  # Actualiza si el valor de la llave existente
persona['hobbies'] = ['jugar videojuegos', 'programación'] 

# Agrega esa clave-valor si no existía previamente
print(persona)

# Imprime: {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}
altura = persona.pop('altura')  # Elimina la clave indicada y devuelve el valor
print(altura)    # Imprime: 1.71
print(persona) 

# salida: {'nombre': 'Carmen', 'edad': 31, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']} 

print(type(3.1416)) #Imprime: <class 'float'>
print(type(persona)) #Imprime <class 'dict'>

print(len(persona)) #Imprime: 4 (la cantidad de pares de clave-valor)
print(len("Me encanta programar")) #Imprime: 20