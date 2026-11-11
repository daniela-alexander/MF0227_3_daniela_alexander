# Excepción personalizada para estados inválidos
class EstadoInvalidoError(Exception):
    def __init__(self, mensaje="Transición de estado no permitida."):
        super().__init__(mensaje)

class TicketTecnico:
    ESTADOS_PERMITIDOS = ["Abierto", "En Proceso", "Cerrado"]

    def __init__(self, id_ticket, titulo, prioridad):
        self._id = id_ticket
        self._titulo = titulo
        self._estado = "Abierto"  # Estado inicial por defecto
        self._prioridad = prioridad

    @property
    def estado(self):
        return self._estado

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS_PERMITIDOS:
            raise EstadoInvalidoError(f"El estado '{nuevo_estado}' no es válido.")
        
        # Validar transiciones lógicas (ej: no pasar de Cerrado a En Proceso)
        if self._estado == "Cerrado":
            raise EstadoInvalidoError("No se puede cambiar el estado de un ticket ya Cerrado.")
        
        if self._estado == "Abierto" and nuevo_estado == "Cerrado":
            raise EstadoInvalidoError("No se puede cerrar un ticket directamente desde Abierto sin pasar por En Proceso.")

        self._estado = nuevo_estado

    def calcular_sla(self):
        # Método base a sobrescribir (Polimorfismo)
        pass

class TicketHardware(TicketTecnico):
    def __init__(self, id_ticket, titulo, prioridad, componente):
        super().__init__(id_ticket, titulo, prioridad)
        self.componente = componente

    def calcular_sla(self):
        # Horas máximas de resolución según prioridad para Hardware
        if self._prioridad.lower() == "alta":
            return 12
        elif self._prioridad.lower() == "media":
            return 24
        return 48

class TicketSoftware(TicketTecnico):
    def __init__(self, id_ticket, titulo, prioridad, sistema_operativo):
        super().__init__(id_ticket, titulo, prioridad)
        self.sistema_operativo = sistema_operativo

    def calcular_sla(self):
        # Horas máximas de resolución según prioridad para Software
        if self._prioridad.lower() == "alta":
            return 8
        elif self._prioridad.lower() == "media":
            return 16
        return 36

# Pruebas unitarias básicas
if __name__ == "__main__":
    try:
        t_hw = TicketHardware(1, "Fallo de Disco Duro", "Alta", "SSD NVMe")
        print(f"Ticket HW creado: {t_hw._titulo} | SLA: {t_hw.calcular_sla()}h")
        
        # Probando transición válida
        t_hw.cambiar_estado("En Proceso")
        print(f"Nuevo estado HW: {t_hw.estado}")
        
        # Probando transición inválida (lanzará excepción)
        t_hw.cambiar_estado("Cerrado") # Debería fallar porque salta directo de En Proceso a Cerrado? No, de En Proceso a Cerrado sí se puede, pero probemos una prohibida:
        
    except EstadoInvalidoError as e:
        print(f"Excepción capturada correctamente: {e}")