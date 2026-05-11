class SuscripcionStreaming:
   costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

   def __init__(self, usuario, tipo_suscripcion="Gratis"):
       self.usuario = usuario
       self.tipo_suscripcion = tipo_suscripcion
       self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
       self.saldo_pendiente = self.costo_mensual

   def realizar_pago(self, monto):
       """Reduce el saldo pendiente según el monto pagado."""
       reducir_monto = min(monto, self.saldo_pendiente)
       self.saldo_pendiente -= reducir_monto

   def cambiar_suscripcion(self, tipo_nuevo):
       """Cambia el tipo de suscripción y actualiza el costo mensual."""
       if tipo_nuevo in self.costos_suscripcion:
           self.tipo_suscripcion = tipo_nuevo
           self.saldo_pendiente = self.costos_suscripcion[tipo_nuevo]

   def ver_contenido_exclusivo(self):
       """Permite ver contenido exclusivo según el tipo de suscripción."""
       if self.tipo_suscripcion == "Gratis":
           return "No tienes acceso a contenido exclusivo."
       elif self.tipo_suscripcion == "Estándar":
           return "Acceso a contenido exclusivo estándar."
       elif self.tipo_suscripcion == "Premium":
           return "Acceso a todo el contenido exclusivo"

   def mostrar_info_suscripcion(self):
       """Muestra la información de la suscripción del usuario."""
       return (
           f"Usuario: {self.self.usuario}, "
           f"Tipo de suscripción: {self.self.tipo_suscripcion}, "
           f"Costo mensual: {self.costo_mensual}, "
           f"Saldo pendiente: {self.saldo_pendiente}")

''' Crea 3 usuarios con diferentes tipos de suscripción.
Haz que el primer usuario intente ver contenido exclusivo, mejore su suscripción y pague su saldo.
Haz que el segundo usuario vea contenido exclusivo, cambie su suscripción a Premium y pague dos veces.
Haz que el tercer usuario intente pagar una cantidad menor a su saldo pendiente y vea contenido exclusivo.
'''

jorge = SuscripcionStreaming("Estándar")
pablo = SuscripcionStreaming("Premium")
federico = SuscripcionStreaming("Gratis")

print("Jorge")
jorge.ver_contenido_exclusivo()
jorge.mejorar_suscripcion("Premium")
jorge.realizar_pago(20)

 
print("Pablo")
pablo.ver_contenido_exclusivo()
pablo.mejorar_suscripcion("Premium")
pablo.realizar_pago(10)
pablo.realizar_pago(20)


print("Federico")
federico.realizar_pago(5)
federico.ver_contenido_exclusivo()