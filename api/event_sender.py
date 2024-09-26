import os
import json
import time
import threading
from flask import Flask, jsonify, send_file
from flask_cors import CORS

# Inicializa o Flask
app = Flask(__name__)
CORS(app)

# Diretório onde os eventos serão armazenados
EVENTS_DIR = os.path.join(os.path.dirname(__file__), "..", "output", "events")

# Função para verificar e listar os eventos no diretório
def listar_eventos():
    eventos = []
    if os.path.exists(EVENTS_DIR):
        arquivos = [f for f in os.listdir(EVENTS_DIR) if f.endswith(".json")]
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(EVENTS_DIR, arquivo)
            with open(caminho_arquivo, 'r') as f:
                evento = json.load(f)
                eventos.append(evento)
                print(f"📄 Evento encontrado e listado: {arquivo}")
    return eventos

# Função para monitorar novos eventos a cada 1 segundo
def monitorar_eventos():
    while True:
        eventos = listar_eventos()
        if eventos:
            print("📦 Novos eventos detectados.")
        time.sleep(1)  # A cada 1 segundo verifica se há novos eventos

# Endpoint para listar os eventos
@app.route('/api/events', methods=['GET'])
def servir_eventos():
    eventos = listar_eventos()
    return jsonify(eventos), 200 if eventos else 204  # 204: Sem conteúdo se não houver eventos

# Endpoint para servir um evento específico (arquivo bruto)
@app.route('/api/events/<event_id>', methods=['GET'])
def servir_evento_especifico(event_id):
    caminho_arquivo = os.path.join(EVENTS_DIR, f"payment_{event_id}.json")  # Certifique-se de que o formato do nome do arquivo está correto
    if os.path.exists(caminho_arquivo):
        return send_file(caminho_arquivo, mimetype='application/json')
    return jsonify({"message": "Evento não encontrado"}), 404

# Inicializa o monitoramento dos eventos
if __name__ == '__main__':
    print("🚀 API de eventos iniciada...")
    monitorar_eventos_thread = threading.Thread(target=monitorar_eventos)
    monitorar_eventos_thread.start()  # Inicia o monitoramento em paralelo
    app.run(host='0.0.0.0', port=5000)  # Porta da API Flask
