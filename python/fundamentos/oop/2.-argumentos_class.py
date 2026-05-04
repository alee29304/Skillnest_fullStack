class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar

# Creación de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 10000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000, 20000)
ale = Usuario("Alexander", "Pino", "alexander@gmail.com", 5000, 10000)

# Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel


# -----------------------------------
# --- Tarea rápida
'''
Crear una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
- Crear 3 instancias para la clase con distintos estudiantes
- Imprimir el nombre y apellido concatenado + especialidad
'''

class Estudiante:
    def __init__(self, nombre, apellido, rut, especialidad, fecha_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

# Creación de instancias
carlos = Estudiante("Carlos", "Pinto Jr", "22.954.100-3", "Programación", "23/05/2007")
joaquin = Estudiante("Joaquín", "Gómez", "23.560.219-5", "Logística", "06/10/2008")
enrique = Estudiante("Enrique", "Gonzalez", "22.758.099-2", "Contabilidad", "19/02/2007")

# Imprimir
print(f"{carlos.nombre} {carlos.apellido} estudia: {carlos.especialidad}")
print(f"{joaquin.nombre} {joaquin.apellido} estudia: {joaquin.especialidad}")
print(f"{enrique.nombre} {enrique.apellido} estudia: {enrique.especialidad}")
