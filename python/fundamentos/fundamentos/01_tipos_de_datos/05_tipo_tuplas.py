# Ejemplo
tupla_letras = ("a", "e", "i", "o", "u")
tupla_sin_parentesis = "a", "e", "i", "o", "u"

# Cualquier tipo de dato
gato = ("Miau", 5, "persa", False)
print(gato[0]) #Imprime: Miau

gato = gato + ("4.1",)
print(gato) #Imprime: ('Miu', 5, 'persa', False, '4.1')

# Tuplas dentro de funciones 
def suma_multiplicacion(x, y):
   suma = x + y
   multiplicacion = x * y
   return (suma, multiplicacion)

print(suma_multiplicacion(10, 5))