class Clima:
    def __init__(self, temperatura: float, humedad: float):
        self.temperatura = temperatura
        self.humedad = humedad

    def set_temperatura(self, temperatura: float):
        self.temperatura = temperatura

    def set_humedad(self, humedad: float):
        self.humedad = humedad

    def get_temperatura(self) -> float:
        return self.temperatura

    def get_humedad(self) -> float:
        return self.humedad

    def to_dict(self):
        return {
            'temperatura': self.temperatura,
            'humedad': self.humedad
        }

    @staticmethod
    def from_dict(data):
        return Clima(data['temperatura'], data['humedad'])
