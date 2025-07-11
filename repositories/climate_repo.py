import sqlite3
from models.registro_climatico import RegistroClimatico

class ClimateRepo:
    """Clase para manejar el repositorio de datos climáticos."""

    def __init__(self, db_path: str = 'clima.db'):
        """Inicializa el repositorio con la ruta de la base de datos."""
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Inicializa la base de datos y crea la tabla si no existe."""
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                temperatura REAL,
                humedad REAL,
                fecha TEXT
            )''')
            conn.commit()

    def agregar_registro(self, temperatura: float, humedad: float, fecha: str):
        """Agrega un registro climático a la base de datos."""
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('INSERT INTO registros (temperatura, humedad, fecha) VALUES (?, ?, ?)',
                      (temperatura, humedad, fecha))
            conn.commit()

    def obtener_registros(self):
        """Obtiene todos los registros climáticos de la base de datos."""
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('SELECT temperatura, humedad, fecha FROM registros')
            rows = c.fetchall()
            return [RegistroClimatico(temp, hum, fecha) for temp, hum, fecha in rows]
