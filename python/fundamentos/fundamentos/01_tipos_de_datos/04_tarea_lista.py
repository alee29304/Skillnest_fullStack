""" Actividad: Gestor de inventario
1- Creación: Crear una lista llamada inventario que contenga los siguientes
articulos: "Laptop", "Ratón", "Monitor", "Cable HDMI"
2- Expansión: Utiliza el método correspondiente para agregar "Impresora" y "Teclado" al final
de la lista
3- Conteo: Utiliza la función integrada para mostrar cuantos elementos totales hay en la lista
4- Acceso y modificación: Modifica "Teclado" por "Teclado mécanico"
5- Slicing: Crea una nueva lista llamada "Promoción", debe contener solo los tres primeros elementos
de la lista "Inventario"
6- Mostrar la lista de inventario ordenada alfabeticamente
7- Elimina el último elemento de la lista inventario mostrando el elemento eliminado y la lista final
"""

inventario = ["Laptop", "Ratón", "Monitor", "Cable HDMI"];
inventario.append("Impresora")
inventario.append("Teclado")
inventario[5] = "Teclado mécanico"
print(inventario)
print(len(inventario))

promocion = [(inventario)[:4]]
print(promocion)

inventario.sort()
print(inventario)

eliminado = inventario.pop()
print("Articulo eliminado:", eliminado)
print(inventario)