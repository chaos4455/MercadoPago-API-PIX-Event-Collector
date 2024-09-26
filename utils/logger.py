import logging
import os
import yaml

# Configuração do Logging
def configurar_logging():
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Função para carregar Configurações do Arquivo config.yaml
def carregar_configuracoes():
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    with open(config_path, "r") as arquivo_config:
        return yaml.safe_load(arquivo_config)
