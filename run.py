import time
import sys
import logging
from os.path import dirname, abspath
from colorama import init, Fore, Style
from utils.logger import configurar_logging
from threading import Thread

# Adiciona o caminho do diretório base (my_flask_app) ao sys.path
sys.path.append(dirname(dirname(abspath(__file__))))

# Importa os módulos necessários
from app.services.payment_service import coletar_eventos, validar_usuario
from app.config.config import (
    CHAVE_SECRETA_PATH,
    CHAVE_API_PATH,
    URL_PAYMENTS_SEARCH,
    CONTROLE_RECIBOS_PATH,
    MINUTOS_DE_BUSCA,
    DATABASE_PATH,
    LICENCA_PATH,
    ID_POS_VALIDO,
    OUTPUT_PATH,
    EVENTS_PATH
)

# Importa o Flask e as rotas da API
from app.api.event_sender import app as flask_app

# Inicializa o Colorama
init(autoreset=True)

# Configuração do Logging
configurar_logging()

# Função para logar eventos
def log_evento(mensagem, nivel='INFO'):
    if nivel == 'INFO':
        logging.info(mensagem)
        print(Fore.GREEN + "✔️ " + Style.RESET_ALL + mensagem)
    elif nivel == 'ERROR':
        logging.error(mensagem)
        print(Fore.RED + "❌ " + Style.RESET_ALL + mensagem)
    else:
        logging.warning(mensagem)
        print(Fore.YELLOW + "⚠️ " + Style.RESET_ALL + mensagem)

# Função que inicia a API Flask
def iniciar_api_flask():
    log_evento("Iniciando a API Flask...", 'INFO')
    flask_app.run(host='0.0.0.0', port=5000)

# Função para executar os processadores de dados
def executar_processador(processador):
    while True:
        try:
            exec(f'from app.analytics.{processador} import main as processador_main')
            processador_main()  # Chama a função principal de cada processador
            log_evento(f"{processador} executado com sucesso.", 'INFO')
        except Exception as e:
            log_evento(f"Ocorreu um erro ao executar {processador}: {str(e)}", 'ERROR')
        time.sleep(60)  # Aguarda 1 minuto antes de executar novamente

# Função principal de coleta de eventos
def main():
    log_evento("Iniciando o programa...", 'INFO')

    # Valida o usuário
    access_token = validar_usuario()
    if access_token:
        log_evento("Usuário validado com sucesso.", 'INFO')
        
        while True:
            try:
                coletar_eventos(access_token)
                log_evento("Coleta de eventos realizada com sucesso.", 'INFO')
                time.sleep(1)  # Ajuste o intervalo conforme necessário
            except Exception as e:
                log_evento(f"Ocorreu um erro: {str(e)}", 'ERROR')
                time.sleep(1)  # Aguarda um pouco antes de tentar novamente

if __name__ == "__main__":
    # Inicia a API Flask em uma thread separada para não bloquear o loop principal
    api_thread = Thread(target=iniciar_api_flask)
    api_thread.daemon = True  # Garante que a thread seja finalizada junto com o programa principal
    api_thread.start()

    # Inicia threads para os processadores de dados
    processador1_thread = Thread(target=executar_processador, args=('data_processorv1',))
    processador1_thread.daemon = True
    processador1_thread.start()

    processador2_thread = Thread(target=executar_processador, args=('data_processorv2',))
    processador2_thread.daemon = True
    processador2_thread.start()

    # Executa o loop principal de coleta de eventos
    main()
