#Diccionario en Python
estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
#Imprimir el nombre de estudiante
print(estudiante["nombre"]) #Imprime: Gonzalo

estudiante["nombre"] = "Vicente"
print(estudiante["nombre"]) #Imprime: Vicente

estudiante["nombre"] = "Juanjo"
print(estudiante["nombre"]) #Imprime: Juanjo

paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Peru"
paises["ARG"] = "Argentina"
print(paises)

#condicion para buscar elementoe insertar si no existe
if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
   print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
   paises["CRI"] = "Costa Rica"

#Eliminar valores de diccionarios
valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
print(valor_removido)
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}
print(paises)

#Diccionario Pintor
pintor = { "nombre": "Frida Kahlo", 
          "pais": "México", 
          "fecha_nacimiento": "6 de julio de 1907"}

#Diccionario aninados
escuela = {
   "nombre": "Coding Dojo LATAM",
   "profesores": [
       {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
       {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
       {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
   ]
}
