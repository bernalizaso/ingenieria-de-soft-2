from models.clima import Clima
from repositories.climate_repo import ClimateRepoAPI
from datetime import datetime

class ClimaController:
    def __init__(self):
        self.clima_actual = Clima(25.0, 60.0)
        self.repo = ClimateRepoAPI()

    def get_estado_actual(self):
        return self.clima_actual.to_dict()

    def set_temperatura(self, temperatura: float):
        self.clima_actual.set_temperatura(temperatura)
        self._guardar_registro()

    def set_humedad(self, humedad: float):
        self.clima_actual.set_humedad(humedad)
        self._guardar_registro()

    def modificar_temperatura(self, delta: float):
        self.clima_actual.set_temperatura(self.clima_actual.get_temperatura() + delta)
        self._guardar_registro()

    def modificar_humedad(self, delta: float):
        self.clima_actual.set_humedad(self.clima_actual.get_humedad() + delta)
        self._guardar_registro()

    def get_historial(self):
        return [r.to_dict() for r in self.repo.obtener_registros()]

    def _guardar_registro(self):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.repo.agregar_registro(
            self.clima_actual.get_temperatura(),
            self.clima_actual.get_humedad(),
            fecha
        )
