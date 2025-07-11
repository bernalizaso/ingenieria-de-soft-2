from flask import Flask, request, jsonify, render_template
from services.clima_service import ClimaService
from services.email_api import MockEmailAPI

app = Flask(__name__)
clima_service = ClimaService()
email_service = MockEmailAPI()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/clima/actual', methods=['GET'])
def estado_actual():
    return jsonify(clima_service.get_estado_actual())

@app.route('/clima/historial', methods=['GET'])
def historial():
    return jsonify(clima_service.get_historial())

@app.route('/clima/temperatura', methods=['POST'])
def modificar_temperatura():
    data = request.get_json()
    accion = data.get('accion')
    valor = float(data.get('valor', 1))
    if accion == 'subir':
        result = clima_service.modificar_temperatura(valor)
    elif accion == 'bajar':
        result = clima_service.modificar_temperatura(-valor)
    else:
        return jsonify({'error': 'Acción inválida'}), 400
    return jsonify(result)

@app.route('/clima/humedad', methods=['POST'])
def modificar_humedad():
    data = request.get_json()
    accion = data.get('accion')
    valor = float(data.get('valor', 1))
    if accion == 'subir':
        result = clima_service.modificar_humedad(valor)
    elif accion == 'bajar':
        result = clima_service.modificar_humedad(-valor)
    else:
        return jsonify({'error': 'Acción inválida'}), 400
    return jsonify(result)

@app.route('/clima/alerta', methods=['POST'])
def enviar_alerta():
    data = request.get_json()
    destinatario = data.get('destinatario')
    asunto = data.get('asunto')
    estado = clima_service.get_estado_actual()
    mensaje = f"[Datos Actuales del Data Center]\nTemperatura: {estado['temperatura']}C\nHumedad: {estado['humedad']}%"
    email_service.enviar_email(destinatario, asunto, mensaje)
    return jsonify({'status': 'Alerta enviada (mock)'})

if __name__ == '__main__':
    app.run(port=8000, debug=True)
