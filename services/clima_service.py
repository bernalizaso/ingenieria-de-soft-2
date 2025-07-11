from models.clima import Clima
from models.registro_climatico import RegistroClimatico
from repositories.climate_repo import ClimateRepo
from datetime import datetime

class ClimaService:
    def __init__(self, repo=None):
        self.clima_actual = Clima(25.0, 60.0)
        self.repo = repo or ClimateRepo()

    def get_estado_actual(self):
        return self.clima_actual.to_dict()

    def modificar_temperatura(self, delta: float):
        self.clima_actual.set_temperatura(self.clima_actual.get_temperatura() + delta)
        self._guardar_registro()
        return self.get_estado_actual()

    def modificar_humedad(self, delta: float):
        self.clima_actual.set_humedad(self.clima_actual.get_humedad() + delta)
        self._guardar_registro()
        return self.get_estado_actual()

    def get_historial(self):
        return [r.to_dict() for r in self.repo.obtener_registros()]

    def _guardar_registro(self):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.repo.agregar_registro(
            self.clima_actual.get_temperatura(),
            self.clima_actual.get_humedad(),
            fecha
        )
