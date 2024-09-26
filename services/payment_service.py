import os
import json
import base64
import logging
import requests
import sqlite3
import yaml
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from utils.logger import carregar_configuracoes

# Configuração do Logging
logging.basicConfig(level=logging.INFO)

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

# Função para obter o nome do computador
def obter_nome_computador():
    return os.environ.get("COMPUTERNAME") or os.environ.get("HOSTNAME")

# Função para criar o banco e tabelas necessárias
def criar_banco_e_tabelas():
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                codigo_usuario TEXT PRIMARY KEY,
                limite_cupons INTEGER,
                status TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contador (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_hora TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hostname (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE
            )
        ''')
        conn.commit()

# Função para obter limite e contador
def obter_limite_contador():
    codigo_usuario = obter_codigo_usuario()
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT limite_cupons FROM usuario WHERE codigo_usuario = ?', (codigo_usuario,))
        limite_cupons = cursor.fetchone()

        if limite_cupons is None:
            logging.error(f"Limite de cupons não encontrado para o usuário {codigo_usuario}.")
            exit()

        cursor.execute('SELECT COUNT(*) FROM contador')
        contador = cursor.fetchone()[0]

    return {'limite': limite_cupons[0], 'contador': contador}

# Função para carregar chave do arquivo
def carregar_chave(caminho_chave):
    if os.path.exists(caminho_chave):
        with open(caminho_chave, "rb") as arquivo:
            return arquivo.read()
    logging.error(f"Arquivo {caminho_chave} não encontrado.")
    return None

# Função para descriptografar chave
def descriptografar_chave(chave_criptografada, chave_secreta):
    try:
        cipher = Fernet(chave_secreta)
        return cipher.decrypt(chave_criptografada).decode()
    except Exception as e:
        logging.error(f"Falha na descriptografia da chave API: {e}")
        return None

# Função para obter código do usuário
def obter_codigo_usuario():
    user_id_path = os.path.join(os.path.dirname(__file__), "..", "config", "user.id")
    if os.path.exists(user_id_path):
        with open(user_id_path, "r") as arquivo:
            codigo_usuario_mascarado = arquivo.read().strip()
        return base64.b64decode(codigo_usuario_mascarado.encode()).decode()
    
    logging.error("Arquivo user.id não encontrado.")
    exit()

# Função para validar usuário
def validar_usuario():
    criar_banco_e_tabelas()
    
    codigo_usuario = obter_codigo_usuario()
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT status FROM usuario WHERE codigo_usuario = ?', (codigo_usuario,))
        resultado = cursor.fetchone()

    if resultado:
        status = resultado[0]
        if status == 'ativo':
            chave_secreta = carregar_chave(CHAVE_SECRETA_PATH)
            chave_api_criptografada = carregar_chave(CHAVE_API_PATH)
            if chave_secreta and chave_api_criptografada:
                chave_api = descriptografar_chave(chave_api_criptografada, chave_secreta)
                if chave_api:
                    logging.info(f"Usuário {codigo_usuario} está ativo. Chave API carregada com sucesso.")
                    return chave_api
                logging.error("Falha ao descriptografar a chave API.")
                exit()
            logging.error("Falha ao carregar chave API ou chave secreta.")
            exit()
        logging.error(f"Usuário {codigo_usuario} está inativo.")
        exit()
    
    logging.error(f"Usuário {codigo_usuario} não encontrado no banco de dados.")
    exit()

# Função para validar hostname
def validar_hostname(nome_computador_atual):
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT nome FROM hostname WHERE nome = ?', (nome_computador_atual,))
        resultado = cursor.fetchone()
        if resultado:
            logging.info("Hostname válido.")
        else:
            cursor.execute('INSERT INTO hostname (nome) VALUES (?)', (nome_computador_atual,))
            conn.commit()
            logging.info(f"Hostname {nome_computador_atual} cadastrado com sucesso.")

# Função para incrementar contador
def incrementar_contador_local():
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contador (data_hora) VALUES (?)', (datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),))
        conn.commit()

# Função para garantir que o diretório e o arquivo de controle existam
def garantir_diretorio_e_controle():
    if not os.path.exists(EVENTS_PATH):
        os.makedirs(EVENTS_PATH)
    if not os.path.exists(CONTROLE_RECIBOS_PATH):
        with open(CONTROLE_RECIBOS_PATH, "w") as controle_recibos_file:
            json.dump({}, controle_recibos_file)

# Função para coletar eventos
def coletar_eventos(access_token):
    info_contador = obter_limite_contador()

    if not info_contador:
        logging.error("Falha ao obter limite e contador. Encerrando o programa.")
        exit()

    limite = info_contador['limite']
    contador = info_contador['contador']

    if contador >= limite:
        logging.info("Limite de emissão mensal atingido. Acione o suporte para upgrade do seu plano!")
        return

    nome_computador_atual = obter_nome_computador()
    if not nome_computador_atual:  
        logging.warning("Nome do computador não encontrado. A coleta de eventos não será realizada.")
        return

    logging.info(f"Nome do computador identificado: {nome_computador_atual}")
    validar_hostname(nome_computador_atual)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    
    end_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    begin_date = (datetime.utcnow() - timedelta(minutes=MINUTOS_DE_BUSCA)).strftime("%Y-%m-%dT%H:%M:%SZ")

    params_payments = {
        "sort": "date_created",
        "criteria": "desc",
        "range": "date_created",
        "begin_date": begin_date,
        "end_date": end_date,
    }

    response_payments = requests.get(URL_PAYMENTS_SEARCH, headers=headers, params=params_payments)

    if response_payments.status_code == 200:
        payments = response_payments.json().get("results", [])
        controle_recibos = carregar_controle_recibos()

        garantir_diretorio_e_controle()  # Garante que o diretório e o arquivo de controle existam

        for payment in payments:
            if processar_pagamento(payment, controle_recibos):
                controle_recibos[payment.get("id")] = payment
                salvar_evento_bruto(payment)

        salvar_controle_recibos(controle_recibos)
        incrementar_contador_local()
        logging.info("Processo de coleta de eventos finalizado com sucesso.")
    else:
        logging.error(f"Erro ao coletar pagamentos. Código de status: {response_payments.status_code}.")

def carregar_controle_recibos():
    if os.path.exists(CONTROLE_RECIBOS_PATH):
        with open(CONTROLE_RECIBOS_PATH, "r") as controle_recibos_file:
            return json.load(controle_recibos_file)
    return {}

def processar_pagamento(payment, controle_recibos):
    payment_id = payment.get("id")
    if payment_id in controle_recibos:
        logging.info(f"Pagamento com ID {payment_id} já processado.")
        return False

    # Aqui você pode adicionar lógica adicional para processar o pagamento
    logging.info(f"Processando pagamento ID {payment_id}.")
    return True

def salvar_evento_bruto(payment):
    payment_id = payment.get("id")
    payment_file_path = os.path.join(EVENTS_PATH, f"payment_{payment_id}.json")
    
    with open(payment_file_path, "w") as payment_file:
        json.dump(payment, payment_file, indent=4)
    logging.info(f"Evento bruto salvo em: {payment_file_path}")

def salvar_controle_recibos(controle_recibos):
    with open(CONTROLE_RECIBOS_PATH, "w") as controle_recibos_file:
        json.dump(controle_recibos, controle_recibos_file)
    logging.info("Controle de recibos salvo com sucesso.")

if __name__ == "__main__":
    try:
        access_token = validar_usuario()
        coletar_eventos(access_token)
    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado: {e}")
