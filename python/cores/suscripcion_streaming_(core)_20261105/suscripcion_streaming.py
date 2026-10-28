class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion = "Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = 0
        self.saldo_pendiente = self.saldo_pendiente + self.costo_mensual

    def realizar_pago(self, monto):
        """Reduce el saldo pendiente según el monto pagado."""
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            return
        self.saldo_pendiente = self.saldo_pendiente - monto
        print(f"Pago realizado: ${monto}")

    def cambiar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción y actualiza el costo mensual."""
        if nuevo_tipo not in self.costos_suscripcion:
            print("Tipo de suscripción inválido!")
            return
        self.tipo_suscripcion = nuevo_tipo
        self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
        self.saldo_pendiente = self.saldo_pendiente + self.costo_mensual
        print(f"Suscripción de usuario {self.usuario} cambiada correctamente:\nNueva suscripción: {self.tipo_suscripcion}\nNuevo costo mensual: ${self.costo_mensual}")

    def ver_contenido_exclusivo(self):
        """Permite ver contenido exclusivo según el tipo de suscripción."""
        if self.tipo_suscripcion == "Gratis":
            print(f"Este contenido requiere suscripcion Estándar o superior...")
            cambiar = input("Desea cambiar su tipo de suscripción?(S/N): ")
            if cambiar == "S" or cambiar == "s":
                print(f"1. Estándar: $5.99\n2. Premium: $10.99")
                nuevoTipo = input("Ingrese el nombre del plan: ")
                self.cambiar_suscripcion(nuevoTipo)
            else:
                print("Ok")
        else:
            print(f"Reproduciendo contenido exclusivo para {self.usuario}...")

    def mostrar_info_suscripcion(self):
        """Muestra la información de la suscripción del usuario."""
        print(f"Mostrando información de {self.usuario}:")
        print(f"Tipo de suscripción: {self.tipo_suscripcion}\nCosto mensual: ${self.costo_mensual}\nSaldo pendiente: ${self.saldo_pendiente}")

# --- Pruebas ---
usuario1 = SuscripcionStreaming("Randy", "Gratis")
usuario2 = SuscripcionStreaming("Juan", "Estándar")
usuario3 = SuscripcionStreaming("Jonathan", "Premium")

# Usuario 1: Intenta ver contenido exclusivo, mejora su suscripción y paga su saldo.
usuario1.ver_contenido_exclusivo()
usuario1.realizar_pago(5.99)
usuario1.mostrar_info_suscripcion()

# Usuario 2: Ve contenido exclusivo, cambcambia su suscripción a Premium y paga dos veces.
usuario2.ver_contenido_exclusivo()
usuario2.cambiar_suscripcion("Premium")
usuario2.realizar_pago(5.00)
usuario2.realizar_pago(11.98)
usuario2.mostrar_info_suscripcion()

# Usuario 3: Intenta pagar una cantidad menor a su saldo pendiente y ve contenido exclusivo.
usuario3.realizar_pago(5.00)
usuario3.ver_contenido_exclusivo()
usuario3.mostrar_info_suscripcion()