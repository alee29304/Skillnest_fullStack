"""En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)

for num in range(1, 100 + 1):
    print(num)

# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)

for num in range(1, 500 + 1):
    if num % 2 == 0:
        print(num)

# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)

for num in range(1, 100 + 1):
    if num % 5 == 0:
        print(num)
    if num % 10 == 0:
        print(num)

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí)

suma_total = 0

for numero in range(0, 500000, + 1):
    if numero % 2 == 0:
        suma_total += numero
        print(numero)

print(f"La suma total es: {suma_total}")

# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)

for año in range(2024, -1, -3):
    print(año)

# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)

inicio = 3
fin = 20
salto = 2

print(f"Buscando múltiplos de {salto} entre {inicio} y {fin}:")

for i in range(inicio, fin + 1):
    if i % salto == 0:
        print(i)

# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10