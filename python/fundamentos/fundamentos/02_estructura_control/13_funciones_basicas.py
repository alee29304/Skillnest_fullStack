"""
Funciones básicas 1.
"""

# 1. Función que retorna la cantidad de logros desbloqueados en un videojuego.
def total_logros_desbloqueados():
    return 7

print(total_logros_desbloqueados())

# Variables | Valores
# Salida: 7

# 2. Función que indica la cantidad de mensajes enviados en un grupo de chat de tu juego online.
def mensajes_en_chat():
    return 2450

# Variables | Valores

# Salida: 2450

# 3. Intentamos sumar el resultado de una función que no existe al de 'mensajes_en_chat'.
print(cantidad_de_dias_en_el_anio() + mensajes_en_chat())

# Función que podría retornar la temporada en que alcanzaste un rango especial en un MOBA (por ejemplo, 2022 o 2021).
def temporada_rango_especial():
    return 2022
    return 2021  # ¿Se llega a ejecutar esta línea?

print(temporada_rango_especial())

# Variables | Valores

# Salida: 2022
# El primer print muestra un error ya que no tiene una variable definida.
# El segundo return no se llega a ejecutar debido a que es estructuralmente inaccesible.


# 4. Cantidad de listas de reproducción que sigues en una plataforma de música.
# Observa que la función 'retorna' 12, pero hay un print(15) después. ¿Se ejecuta?
def total_playlists():
    return 12
    print(15)

print(total_playlists())

# Variables | Valores

# Salida: 12
# El print muestra error ya que está estructuralmente inaccesible


# 5. Función que muestra el número de episodios vistos de tu serie favorita,
# pero únicamente imprime su valor, sin retornarlo.
def episodios_serie_favorita():
    print(24)

x = episodios_serie_favorita()
print(x)

# Variables | Valores
# x

# Salida: 24, None
# X no imprime nada ya que no retorna ningún valor.

# 6. Función que "suma" los puntos obtenidos al compartir y al dar 'like' en una red social.
# Pero la función utiliza print en lugar de return. ¿Cómo afecta eso si queremos combinar los resultados?
def suma_puntos(a, b):
    print(a + b)

print(suma_puntos(10, 5) + suma_puntos(4, 3))

# Variables | Valores
# a         | 10 - 4
# b         | 5 - 3
# Salida: 15, 7
# La función genera error ya que no tiene return.

# 7. Función para concatenar dos "tags" de redes sociales, aunque se concatenan en orden inverso.
def combinar_tags(tag1, tag2):
    return str(tag2) + str(tag1)

print(combinar_tags("#Verano", "#Diversión"))

# Variables | Valores
# tag1      | #Verano
# tag2      | #Diversión

# Salida: #Diversión#Verano


# 8. Supongamos que 'a' representa el conteo de reproducciones de un video viral.
# Dependiendo del valor, devuelve un número distinto (p. ej., un ID de categoría).
def conteo_reproducciones_video():
    a = 560000
    print(a)
    if a < 180000:
        return 33
    else:
        return 46
    return 21  # ¿Se alcanza a ejecutar?

print(conteo_reproducciones_video())

# Variables | Valores
# a         | 560000

# Si es menor a 180000
# Salida: 33

# Si es mayor
# Salida: 46
# return 21 no se ejecuta ya que es estructuralmente inaccesible.


# 9. Duración de una suscripción premium: 365 días (si se cumplen ciertas condiciones) o 12 meses.
# El tercer 'return' (52 semanas) está después del else. ¿Lo veremos?
def duracion_suscripcion(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52

print(duracion_suscripcion(1, 3))
print(duracion_suscripcion(7, 4))
print(duracion_suscripcion(7, 4) + duracion_suscripcion(1, 3))

# Variables | Valores
# a         | 1 - 7 - 7 - 1
# b         | 3 - 4 - 4 - 3

# Salida: 365, 12, 377
# return 52 no se ejecuta ya que es estructuralmente inaccesible.


# 10. Suma de propinas que recibes en un juego de simulación (p.ej. "Cafetería Virtual").
# Nota que hay dos return, pero el segundo no se ejecuta nunca.
def suma_propinas(a, b):
    return a + b
    return 157

print(suma_propinas(3, 4))

# Variables | Valores
# a         | 3
# b         | 4

# Salida: 7
# return 157 no se ejecuta ya que es estructuralmente inaccesible.


# 11. Variable global que cuenta cuántas horas de juego llevas en total.
# Dentro de la función se define otra variable con el mismo nombre.
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)

print(horas_de_juego)
mostrar_horas_local()
print(horas_de_juego)

# Variables | Valores
# horas_de_juego | 150 - 350

# Salida: 150, 350, 350, 150


# 12. Similar al anterior, pero la función retorna el valor local 'horas_de_juego'.
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)
    return horas_de_juego

print(horas_de_juego)
mostrar_horas_local()
print(horas_de_juego)

# Variables | Valores
# horasdejuego | 150 - 350

# Salida: 150, 350, 150, 350, 150


# 13. Ahora reasignamos la variable global con el valor que retorna la función.
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)
    return horas_de_juego

print(horas_de_juego)
horas_de_juego = mostrar_horas_local()
print(horas_de_juego)

# Variables | Valores
# horasdejuego | 150 - 350

# Salida: 150, 350, 150, 350, 150, None, 150


# 14. Una función que primero muestra la cantidad de seguidores en tu canal, luego llama a otra función para mostrar "Likes".
def mostrar_seguidores():
    print("Seguidores: 300")
    mostrar_likes()
    print("Finalizando conteo")

def mostrar_likes():
    print("Likes: 120")

mostrar_seguidores()

# Variables | Valores

# Salida: Seguidores: 300, Finalizando conteo, Likes: 120


# 15. Función que muestra "Reproducciones" de un tema musical y recibe un valor de otra función,
# luego retorna un número que podría ser un "ID" final de procesamiento.
def mostrar_reproducciones():
    print("Reproducciones: 5000")
    a = calcular_incremento()
    print(a)
    return 4

def calcular_incremento():
    print("Incremento calculado: ")
    return 1

b = mostrar_reproducciones()
print(b)