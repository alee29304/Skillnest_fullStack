# Creación de la clase usuario - Entidad
class Usuario:
    def __init__(self):
       self.nombre = "Nariyoshi"
       self.apellido = "Miyagi"
       self.email = "miyagi@codingdojo.la"
       self.limite_credito = 30000
       self.saldo_pagar = 0

# Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
ale = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre)
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

# Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000

print(daniel.nombre) #Imprime: Daniel

# Valores a nueva instancia
ale.nombre = "Alexander"
ale.apellido = "Pino"
ale.email = "alexander@gmail.com"
ale.limite_credito = 1000
ale.saldo_pagar = 20000

# Imprimir nombre de cada instancia
print(miyagi.nombre)
print(daniel.nombre)
print(ale.nombre)