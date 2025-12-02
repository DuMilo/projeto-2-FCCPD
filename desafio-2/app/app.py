import sqlite3
import os
from datetime import datetime

DB_PATH = "/data/banco_persistente.db"

def init_db():

    db_exists = os.path.exists(DB_PATH)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    if not db_exists:
        print("--- [AVISO] Arquivo de banco não encontrado. Criando um novo... ---")
    else:
        print("--- [SUCESSO] Banco de dados existente encontrado! ---")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS acessos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    return conn

def main():
    print(f"Iniciando aplicação. Procurando banco em: {DB_PATH}")
    
    conn = init_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM acessos")
    registros = cursor.fetchall()
    
    print("\n=== HISTÓRICO DE ACESSOS (Do volume) ===")
    if not registros:
        print("Nenhum registro anterior encontrado (Primeira execução ou volume vazio).")
    else:
        for reg in registros:
            print(f"ID: {reg[0]} | Data: {reg[1]}")
    print("========================================\n")

    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO acessos (timestamp) VALUES (?)", (agora,))
    conn.commit()
    print(f"Novo acesso registrado: {agora}")
    
    conn.close()

if __name__ == "__main__":
    main()