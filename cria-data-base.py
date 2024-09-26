# create_database.py

import os
import sqlite3

# Caminho do banco de dados
DATABASE_PATH = os.path.join("db", "controle_usuarios.db")

def criar_base_de_dados():
    """Cria a base de dados e as tabelas necessárias se não existirem."""
    # Cria o diretório da base de dados se não existir
    if not os.path.exists('db'):
        os.makedirs('db')

    # Conecta ao banco de dados (será criado se não existir)
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        # Criação da tabela usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Criação da tabela pagamentos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pagamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                valor REAL NOT NULL,
                status TEXT NOT NULL,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
            )
        ''')

        # Salva as mudanças e fecha a conexão
        conn.commit()
        conn.close()
        print(f"Base de dados criada em: {DATABASE_PATH}")
    except sqlite3.OperationalError as e:
        print(f"Erro ao abrir a base de dados: {e}")

if __name__ == "__main__":
    criar_base_de_dados()
