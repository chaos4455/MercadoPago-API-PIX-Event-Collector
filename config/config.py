import os
import yaml

# Carregar Configurações do Arquivo config.yaml
def carregar_configuracoes():
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    with open(config_path, "r") as arquivo_config:
        return yaml.safe_load(arquivo_config)

# Configurações Centralizadas a partir do config.yaml
config = carregar_configuracoes()

# Ajustando todos os caminhos para o diretório correto
CHAVE_SECRETA_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "chave_secreta.key")
CHAVE_API_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "api.key")
URL_PAYMENTS_SEARCH = config['url_payments_search']
CONTROLE_RECIBOS_PATH = os.path.join(os.path.dirname(__file__), "..", "output", "controle_recibos.json")
MINUTOS_DE_BUSCA = config['minutos_de_busca']
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "controle_usuarios.db")
LICENCA_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "data.lic")
ID_POS_VALIDO = config['id_pos_valido']
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "output")
EVENTS_PATH = os.path.join(OUTPUT_PATH, "events")
