class EmailAPI:
    def enviar_email(self, destinatario: str, asunto: str, mensaje: str):
        raise NotImplementedError

class MockEmailAPI(EmailAPI):
    def enviar_email(self, destinatario: str, asunto: str, mensaje: str):
        print(f"\n=== Email Mock ===\nPara: {destinatario}\nAsunto: {asunto}\nMensaje: {mensaje}\n==================\n")
