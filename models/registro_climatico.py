from datetime import datetime

class RegistroClimatico:
    def __init__(self, temperatura: float, humedad: float, fecha: str = None):
        self.temperatura = temperatura
        self.humedad = humedad
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            'temperatura': self.temperatura,
            'humedad': self.humedad,
            'fecha': self.fecha
        }

    @staticmethod
    def from_dict(data):
        return RegistroClimatico(data['temperatura'], data['humedad'], data['fecha'])
