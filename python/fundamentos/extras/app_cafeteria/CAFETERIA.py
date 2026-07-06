class CafeteriaCliente:

    total_clientes= []

    def __init__(self, nombre, puntos=0, saldo=0, membresia="Bronce"):
        self.nombre = nombre
        self.puntos_acumulados = puntos
        self.saldo_pendiente = saldo
        self.tipo_membresia = membresia

        CafeteriaCliente.total_clientes.append(self)

    def realizar_compra(self, monto):
        self.saldo_pendiente += monto
        self.puntos_acumulados += int(monto // 10)
        print(f"{self.nombre} realizo una compra de {monto}")
    
    def pagar_saldo(self, monto):
        if monto <= 0:
            print("El monto a pagar debe ser mayor que 0.")
        elif monto >= self.saldo_pendiente:
            print(f"{self.nombre} ha pagado su saldo pendiente.")
            self.saldo_pendiente = 0
        else:
            self.saldo_pendiente -= monto
            print(
            f"{self.nombre} ha pagado {monto} de su saldo pendiente. "
            f"Deuda restante: {self.saldo_pendiente}"
        )

    @classmethod
    def mostrar_total_clientes(cls):
        return len(cls.total_clientes)
    
    @staticmethod
    def validar_membresia(tipo):
        if tipo in ("Bronce", "Plata", "Oro"):
            return True
        else:
            return False

c1 = CafeteriaCliente("Jose", 0, 0, "Diamante")
c2 = CafeteriaCliente("Felipe", 10, 10, "Plata")
c3 = CafeteriaCliente("Sofia", 10, 50, "Oro")

#nombres
c1.nombre
print(f"Nombre del cliente: {c1.nombre}")
c2.nombre
print(f"Nombre del cliente: {c2.nombre}")
c3.nombre
print(f"Nombre del cliente: {c3.nombre}")

#validacion de mem
c1.realizar_compra(500)
print(f"Total de clientes registrados: {CafeteriaCliente.mostrar_total_clientes()}")
print(f"Membresia Valida: {CafeteriaCliente.validar_membresia(c1.tipo_membresia)}")

c2.realizar_compra(500)
print(f"Total de clientes registrados: {CafeteriaCliente.mostrar_total_clientes()}")
print(f"Membresia Valida: {CafeteriaCliente.validar_membresia(c2.tipo_membresia)}")

c3.realizar_compra(500)
print(f"Total de clientes registrados: {CafeteriaCliente.mostrar_total_clientes()}")
print(f"Membresia Valida: {CafeteriaCliente.validar_membresia(c3.tipo_membresia)}")

#Saldo pendiente
c1 = CafeteriaCliente("Jose", saldo=0)
c1.realizar_compra(500)
c1.pagar_saldo(200)
print(f"Deuda final de {c1.nombre}: {c1.saldo_pendiente}")

c2 = CafeteriaCliente("Felipe", saldo=0)
c2.realizar_compra(1500)
c2.pagar_saldo(2500)
print(f"Deuda final de {c2.nombre}: {c2.saldo_pendiente}")

print(f"Total de clientes: {CafeteriaCliente.mostrar_total_clientes()}")