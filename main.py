from app.utils.logger import configurar_logging
from app.auth.authentication import validar_usuario
from app.services.event_service import coletar_eventos

def main():
    configurar_logging()
    access_token = validar_usuario()
    coletar_eventos(access_token)

if __name__ == "__main__":
    main()
