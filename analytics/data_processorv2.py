import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging

# Configurações do servidor SMTP
SMTP_HOST = 'smtp-relay.brevo.com'
SMTP_PORT = 465
SMTP_USERNAME = 'chaos4455@gmail.com'
SMTP_PASSWORD = 'pZz9rCt2I5SdjKsY'

# Configurações do e-mail
SENDER_EMAIL = 'alert@rocketpix.com.br'
RECEIVER_EMAIL = 'evolucaoit@gmail.com'
SUBJECT = 'Relatório de Performance Sistema Pagamento Pix'

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função para salvar gráficos
def save_plot(fig, filename):
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')
    os.makedirs(output_dir, exist_ok=True)
    fig.savefig(os.path.join(output_dir, f"{filename}.png"))
    plt.close(fig)  # Fecha a figura

# Função para gerar gráfico de calor
def generate_heatmap(df, index_col, title, filename, color_map='RdYlGn_r'):
    try:
        pivot_table = df.pivot_table(values='transaction_amount', index=index_col, columns='date', aggfunc='sum', fill_value=0)
        plt.figure(figsize=(12, 8))
        sns.heatmap(pivot_table, annot=True, fmt='.2f', cmap=color_map, center=0)
        plt.title(title, fontsize=16, color='green')  # Título em verde
        plt.xlabel('Data', fontsize=14)
        plt.ylabel(index_col, fontsize=14)
        save_plot(plt.gcf(), filename)  # Passa a figura atual
    except KeyError as e:
        logging.error(f"Erro ao gerar o gráfico de calor para {index_col}: {e}")

# Função para gerar gráfico de linhas
def generate_line_chart(df, x_col, y_col, title, filename):
    try:
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df, x=x_col, y=y_col, marker='o', color='red')
        plt.title(title, fontsize=16, color='red')  # Título em vermelho
        plt.xlabel(x_col, fontsize=14)
        plt.ylabel(y_col, fontsize=14)
        plt.xticks(rotation=45)
        save_plot(plt.gcf(), filename)  # Passa a figura atual
    except Exception as e:
        logging.error(f"Erro ao gerar o gráfico de linhas para {y_col}: {e}")

# Função para gerar gráfico de barras
def generate_bar_chart(df, index_col, y_col, title, filename):
    try:
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df, x=index_col, y=y_col, palette='Set2')
        plt.title(title, fontsize=16, color='blue')  # Título em azul
        plt.xlabel(index_col, fontsize=14)
        plt.ylabel(y_col, fontsize=14)
        plt.xticks(rotation=45)
        save_plot(plt.gcf(), filename)  # Passa a figura atual
    except Exception as e:
        logging.error(f"Erro ao gerar o gráfico de barras para {y_col}: {e}")

# Função para enviar e-mail com anexos
def send_email_with_attachments(subject, body, attachment_paths):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    for attachment_path in attachment_paths:
        try:
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
                msg.attach(part)
        except FileNotFoundError:
            logging.error(f"Erro: O arquivo {attachment_path} não foi encontrado. Não será anexado.")

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)

# Função para carregar arquivos JSON
def load_json_files(data_directory):
    all_data = []
    for filename in os.listdir(data_directory):
        if filename.endswith('.json'):
            with open(os.path.join(data_directory, filename), 'r') as f:
                data = json.load(f)
                all_data.append(data)
    return all_data

# Função para converter JSON em DataFrame
def json_to_dataframe(json_data):
    return pd.json_normalize(json_data)

# Definir o diretório de dados
current_script_path = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(current_script_path, '..', 'output', 'events')

# Carregar os dados
data = load_json_files(data_directory)
if data:
    df = json_to_dataframe(data)

    # Verificar se a coluna de data existe e adicionar uma coluna de data
    if 'date_created' in df.columns:
        df['date'] = pd.to_datetime(df['date_created'])  # Usando a coluna 'date_created'
    else:
        logging.error("Erro: 'date_created' não encontrado nos dados. Verifique o arquivo JSON.")
        exit(1)  # Encerrar o programa

    # Gerar gráficos com base nos tipos de pagamento e outros parâmetros
    heatmap_files = []
    payment_types = df['payment_type_id'].unique()

    for payment_type in payment_types:
        # Gerar gráfico de calor
        generate_heatmap(df[df['payment_type_id'] == payment_type], 'payment_type_id', f'Mapa de Calor - Tipo de Pagamento {payment_type}', f'heatmap_payment_type_{payment_type}')
        heatmap_files.append(os.path.join(current_script_path, '..', 'reports', f'heatmap_payment_type_{payment_type}.png'))

        # Gerar gráfico de linha
        generate_line_chart(df[df['payment_type_id'] == payment_type], 'date', 'transaction_amount', f'Gráfico de Linhas - Pagamentos por Data {payment_type}', f'line_chart_payments_{payment_type}')
        heatmap_files.append(os.path.join(current_script_path, '..', 'reports', f'line_chart_payments_{payment_type}.png'))

        # Gerar gráfico de barras
        generate_bar_chart(df[df['payment_type_id'] == payment_type], 'date', 'transaction_amount', f'Gráfico de Barras - Pagamentos por Data {payment_type}', f'bar_chart_payments_{payment_type}')
        heatmap_files.append(os.path.join(current_script_path, '..', 'reports', f'bar_chart_payments_{payment_type}.png'))

    # Enviar e-mail com os gráficos gerados
    if heatmap_files:
        send_email_with_attachments(SUBJECT, 'Veja em anexo os relatórios de performance.', heatmap_files)
        logging.info("Relatório enviado com sucesso!")
    else:
        logging.warning("Nenhum gráfico foi gerado.")

else:
    logging.error("Nenhum dado encontrado para processar.")
