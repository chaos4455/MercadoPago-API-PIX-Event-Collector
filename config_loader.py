import os
import yaml

def carregar_configuracoes():
    # Define o caminho para o arquivo config.yaml dentro da pasta config
    config_path = os.path.join(os.path.dirname(__file__), "config", "config.yaml")
    
    # Abre e carrega as configurações do arquivo YAML
    with open(config_path, "r") as arquivo_config:
        return yaml.safe_load(arquivo_config)

# Carrega as configurações centralizadas a partir do config.yaml
config = carregar_configuracoes()

# Ajusta todos os caminhos para o diretório correto
CHAVE_SECRETA_PATH = os.path.join(os.path.dirname(__file__), "config", "chave_secreta.key")
CHAVE_API_PATH = os.path.join(os.path.dirname(__file__), "config", "api.key")
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "controle_usuarios.db")
CONTROLE_RECIBOS_PATH = os.path.join(os.path.dirname(__file__), "..", "output", "controle_recibos.json")
EVENTS_PATH = os.path.join(os.path.dirname(__file__), "..", "output", "events")

# Defina as variáveis que você precisa importar
URL_PAYMENTS_SEARCH = config.get('url_payments_search', 'http://default.url')  # Defina uma URL padrão
MINUTOS_DE_BUSCA = config.get('minutos_de_busca', 5)  # Define um valor padrão de 5 minutos, se não estiver definido

# Se necessário, você pode imprimir ou logar as configurações para verificação
if __name__ == "__main__":
    print("Configurações Carregadas:")
    print(f"URL_PAYMENTS_SEARCH: {URL_PAYMENTS_SEARCH}")
    print(f"CHAVE_SECRETA_PATH: {CHAVE_SECRETA_PATH}")
    print(f"CHAVE_API_PATH: {CHAVE_API_PATH}")
    print(f"DATABASE_PATH: {DATABASE_PATH}")
    print(f"CONTROLE_RECIBOS_PATH: {CONTROLE_RECIBOS_PATH}")
    print(f"EVENTS_PATH: {EVENTS_PATH}")
    print(f"MINUTOS_DE_BUSCA: {MINUTOS_DE_BUSCA}")
