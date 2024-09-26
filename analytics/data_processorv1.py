import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import plotly.express as px

# Configurações do servidor SMTP
smtp_host = 'smtp-relay.brevo.com'
smtp_port = 465
smtp_username = 'chaos4455@gmail.com'
smtp_password = 'pZz9rCt2I5SdjKsY'

# Configurações do e-mail
sender_email = 'alert@rocketpix.com.br'
receiver_email = 'evolucaoit@gmail.com'
subject = 'Relatório de Performance Sistema Pagamento Pix'

# Função para carregar todos os arquivos JSON
def load_json_files(directory):
    try:
        files = [f for f in os.listdir(directory) if f.endswith('.json') and f.startswith('payment_')]
        data = []
        for file in files:
            with open(os.path.join(directory, file), 'r') as f:
                data.append(json.load(f))
        return data
    except FileNotFoundError:
        print(f"Erro: O diretório {directory} não foi encontrado.")
        return []
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return []

# Função para transformar dados JSON em DataFrame
def json_to_dataframe(data):
    df = pd.json_normalize(data)  # Normaliza a estrutura dos dados
    # Corrigir possíveis aninhamentos na coluna transaction_amount
    if 'transaction_amount' in df.columns:
        df['transaction_amount'] = df['transaction_amount'].apply(
            lambda x: x if isinstance(x, (int, float)) else (x[0] if x else 0)
        )
    return df

# Função para salvar os gráficos
def save_plot(fig, filename):
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')
    os.makedirs(output_dir, exist_ok=True)
    fig.write_image(os.path.join(output_dir, f"{filename}.png"))

# Função para gerar gráficos de calor
def generate_heatmaps(df):
    if 'transaction_amount' not in df.columns:
        print("Erro: A coluna 'transaction_amount' não foi encontrada nos dados.")
        return

    metrics = [
        ('payment_type_id', 'currency_id'),
        ('payment_type_id', 'date'),
        ('currency_id', 'date'),
    ]

    for idx, (index_col, column_col) in enumerate(metrics):
        if index_col in df.columns and column_col in df.columns:
            pivot_table = df.pivot_table(
                values='transaction_amount',
                index=index_col,
                columns=column_col,
                aggfunc='sum',
                fill_value=0
            )

            fig = px.imshow(pivot_table,
                             title=f'Montante Total por {index_col} e {column_col}',
                             labels={'color': 'Montante Total (BRL)'},
                             color_continuous_scale='Viridis')
            save_plot(fig, f'heatmap_{idx + 1}_{index_col}_{column_col}')
        else:
            print(f"Erro: Uma das colunas '{index_col}' ou '{column_col}' não existe no DataFrame.")

# Função para enviar e-mail com anexo
def send_email_with_attachment(subject, body, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
            msg.attach(part)

        with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
    except FileNotFoundError:
        print(f"Erro: O arquivo de anexo {attachment_path} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Definir o diretório correto
current_script_path = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(current_script_path, '..', 'output', 'events')

# Verificação do diretório de dados
print(f"Tentando acessar o diretório: {data_directory}")
if not os.path.exists(data_directory):
    print(f"Erro: O diretório {data_directory} não foi encontrado.")
    print("Conteúdo do diretório atual:")
    print(os.listdir(os.path.dirname(data_directory)))  # Listando o diretório pai para ver o que está lá
else:
    # Carregar os dados e gerar os gráficos
    data = load_json_files(data_directory)
    if data:
        df = json_to_dataframe(data)
        generate_heatmaps(df)

        # Enviar e-mail com todos os gráficos gerados
        reports_directory = os.path.join(current_script_path, '..', 'reports')
        if os.path.exists(reports_directory):
            for filename in os.listdir(reports_directory):
                if filename.endswith('.png'):
                    attachment_path = os.path.join(reports_directory, filename)
                    send_email_with_attachment(subject, 'Veja em anexo o relatório de performance.', attachment_path)
            print("Relatório enviado com sucesso!")
        else:
            print("Erro: O diretório de relatórios não foi encontrado.")
    else:
        print("Nenhum dado encontrado para processar.")
